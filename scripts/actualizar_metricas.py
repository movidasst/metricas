"""Actualiza exclusivamente resumen-ecosistema.json; credencial solo desde secret."""
import base64, copy, datetime as dt, json, os, time, urllib.request
from zoneinfo import ZoneInfo
import google.auth.transport.requests
from google.oauth2 import service_account

PROPERTIES = ("414669681", "401557991")
END = dt.datetime.now(ZoneInfo("America/Santiago")).date() - dt.timedelta(days=1)
START = END - dt.timedelta(days=27)
PATH = "repos/movidasst/metricas/contents/resumen-ecosistema.json"
def dates(a,b):
    return [(a+dt.timedelta(days=i)).isoformat() for i in range((b-a).days+1)]
def count(v):
    n=int(v)
    if str(n)!=str(v) or n<0: raise ValueError("Conteo inválido")
    return n
def github(path, method="GET", body=None):
    req=urllib.request.Request("https://api.github.com/"+path, data=None if body is None else json.dumps(body).encode(), method=method, headers={"Authorization":"Bearer "+os.environ["GH_TOKEN"],"Accept":"application/vnd.github+json","Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=60) as r: return json.load(r)
def report(prop,a,b,metrics,dimensions=()):
    body={"dateRanges":[{"startDate":str(a),"endDate":str(b)}],"metrics":[{"name":m} for m in metrics],"dimensions":[{"name":d} for d in dimensions],"keepEmptyRows":True,"limit":100000}
    req=urllib.request.Request("https://analyticsdata.googleapis.com/v1beta/properties/"+prop+":runReport",data=json.dumps(body).encode(),headers={"Authorization":"Bearer "+credentials.token,"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=90) as r: data=json.load(r)
    raw=data.get("rows",[])
    if not raw or len(raw)!=data.get("rowCount"): raise ValueError("Informe vacío o truncado")
    result=[]
    for row in raw:
        vals={k:count(v["value"]) for k,v in zip(metrics,row["metricValues"])}
        vals.update({k:v["value"] for k,v in zip(dimensions,row.get("dimensionValues",[]))})
        result.append(vals)
    return result
def normalized(v): return dt.datetime.strptime(v,"%Y%m%d").date().isoformat()
def recent():
    total=dict(users=0,sessions=0,views=0,engaged_sessions=0)
    groups={k:{} for k in ("daily","countries","devices","channels")}
    for prop in PROPERTIES:
        rr=report(prop,START,END,["activeUsers","sessions","screenPageViews","engagedSessions"])
        if len(rr)!=1: raise ValueError("Total ambiguo")
        r=rr[0]
        if r["engagedSessions"]>r["sessions"]: raise ValueError("Tasa inválida")
        for out,key in (("users","activeUsers"),("sessions","sessions"),("views","screenPageViews"),("engaged_sessions","engagedSessions")): total[out]+=r[key]
        for out,dimension in (("daily","date"),("countries","country"),("devices","deviceCategory"),("channels","sessionDefaultChannelGroup")):
            rows=report(prop,START,END,["sessions"],[dimension])
            if out=="daily" and sorted(normalized(r["date"]) for r in rows)!=dates(START,END): raise ValueError("Cobertura reciente incompleta: "+prop)
            for row in rows:
                name=normalized(row[dimension]) if out=="daily" else row[dimension] or "Sin especificar"
                groups[out][name]=groups[out].get(name,0)+row["sessions"]
    total["engagement_rate"]=total["engaged_sessions"]/total["sessions"] if total["sessions"] else 0
    return dict(date_from=str(START),date_to=str(END),total=total,daily=[dict(date=k,sessions=v) for k,v in sorted(groups.pop("daily").items())],**{key:[dict(name=k,sessions=v) for k,v in sorted(values.items(),key=lambda x:(-x[1],x[0]))] for key,values in groups.items()})
def calculate(old,new_recent,errors):
    data=copy.deepcopy(old)
    if new_recent: data["recent"]=new_recent
    try:
        cutoff=dt.date.fromisoformat(old.get("views_date_to",old["date_to"]))
        if cutoff>END: raise ValueError("Corte futuro")
        if cutoff<END:
            start=cutoff+dt.timedelta(days=1)
            added=0
            for prop in PROPERTIES:
                rows=report(prop,start,END,["screenPageViews"],["date"])
                if sorted(normalized(r["date"]) for r in rows)!=dates(start,END): raise ValueError("Cobertura acumulada incompleta: "+prop)
                added+=sum(r["screenPageViews"] for r in rows)
            data["total"]["views"]=count(old["total"]["views"])+added
            data["views_date_to"]=str(END)
    except Exception as e: errors.append("Acumulado: "+str(e))
    return data
if __name__=="__main__":
    secret=os.environ.get("GA4_SERVICE_ACCOUNT_JSON","")
    if not secret: raise SystemExit("Falta el secret GA4_SERVICE_ACCOUNT_JSON y acceso Lector a ambas propiedades.")
    credentials=service_account.Credentials.from_service_account_info(json.loads(secret),scopes=["https://www.googleapis.com/auth/analytics.readonly"])
    credentials.refresh(google.auth.transport.requests.Request())
    errors=[]
    try: new_recent=recent()
    except Exception as e:
        new_recent=None
        errors.append("Recent: "+str(e))
    for attempt in range(3):
        f=github(PATH+"?ref=main")
        old=json.loads(base64.b64decode(f["content"]))
        run_errors=list(errors)
        data=calculate(old,new_recent,run_errors)
        if data==old: break
        try:
            github(PATH,"PUT",{"branch":"main","sha":f["sha"],"message":"Actualizar métricas GA4 al "+str(END),"content":base64.b64encode((json.dumps(data,ensure_ascii=False,indent=2)+"\n").encode()).decode()})
            # GITHUB_TOKEN commits do not automatically trigger Pages builds.
            github("repos/movidasst/metricas/pages/builds","POST",{})
            break
        except urllib.error.HTTPError as e:
            if e.code!=409 or attempt==2: raise
    else: raise RuntimeError("Conflicto persistente")
    for i in range(24):
        try:
            with urllib.request.urlopen("https://metricas.movidasst.com/resumen-ecosistema.json?v="+str(time.time()),timeout=20) as r: live=json.load(r)
            if live==data: break
        except Exception: pass
        time.sleep(5)
    else: run_errors.append("No se confirmó la publicación pública")
    print("Corte de vistas:",data.get("views_date_to"),"Vistas:",data["total"]["views"])
    if run_errors: raise SystemExit("; ".join(run_errors))
