# Métricas de La Movida de SST+

## Tablero público

[metricas.movidasst.com](https://metricas.movidasst.com/) muestra un **resumen general acumulado** con 4 pestañas: **General**, **Países**, **Dispositivos** y **Canales**. La interfaz es mobile-first y usa barra inferior sólida en dispositivos móviles.

Las cifras visibles se cargan de [resumen-ecosistema.json](./resumen-ecosistema.json), generado a partir de consultas verificadas a Google Analytics 4 vía Windsor.ai. En la vista pública no aparecen avisos sobre períodos históricos ni listados de subdominios.

## Agregación aplicada

- Fecha de consulta: **25 de octubre de 2026**.
- Período cubierto: **25 de octubre de 2024 al 24 de octubre de 2026**.
- Propiedad web principal: **414669681**, hostname `www.movidasst.com`, ID de etiqueta `G-WQMF05XMJL`.
- Propiedad de Moodle: **401557991**, hostname `movidasst.org`, ID de etiqueta `G-D0YXTL06LN`.
- Sesiones, vistas, sesiones con interacción y conteos de usuarios se **suman por propiedad**, según autorización expresa del administrador. La tasa de interacción se obtiene dividiendo sesiones con interacción por sesiones totales combinadas.
- La suma de usuarios por propiedad puede incluir a la misma persona en ambas; por ello el KPI se denomina solamente **Usuarios**, nunca **Usuarios únicos**.
- Países, dispositivos y canales agrupan sumando sus sesiones por categoría; algunas distribuciones de GA4 pueden no reconciliar exactamente con el total de sesiones, dependiendo de los resultados dimensionales de la API.
- El gráfico presenta los últimos 12 meses del período; el acumulado de tarjetas cubre todo el corte.

## Fuentes adicionales conservadas

- [historico-web-ga4.json](./historico-web-ga4.json) — extracción completa del período web principal de 2025.
- [snapshot-ga4.json](./snapshot-ga4.json) — extracción de Moodle correspondiente al período reciente anterior.
- [cobertura-ga4.json](./cobertura-ga4.json) — inventario técnico de los 57 subdominios que tienen instalado el cargador del flujo web, pendiente de verificar recepción de nuevos eventos.

La página es estática. Para actualizar las cifras publicadas, se debe repetir la consulta a GA4 y reemplazar `resumen-ecosistema.json`. La publicación efectiva debe verificarse en un navegador.
