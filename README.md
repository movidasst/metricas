# Métricas — La Movida de SST+

Portal: https://metricas.movidasst.com/

## Qué contiene
Sitio estático para consultar el informe de Looker Studio asociado al ecosistema y explicar cómo interpretar las métricas. Archivo principal: `index.html`.

## Informe vinculado
- ID del informe: `a52dba2d-8ef2-4dc1-9c74-20a2993627fc`
- Página: `YWYSF`
- Visor integrado: https://lookerstudio.google.com/embed/reporting/a52dba2d-8ef2-4dc1-9c74-20a2993627fc/page/YWYSF
- Informe externo: https://lookerstudio.google.com/reporting/a52dba2d-8ef2-4dc1-9c74-20a2993627fc/page/YWYSF

La web **no almacena, modifica ni inventa cifras**. Recargar el iframe no fuerza el refresco del origen de datos.

## Comprobaciones antes de publicar cifras
1. Abrir el informe con permisos adecuados y comprobar si el acceso público es intencionado.
2. Confirmar la fuente conectada (GA4 u otra), su identificador, su vigencia y el alcance exacto de dominios/subdominios.
3. Verificar período, zona horaria, filtros, tráfico interno y eventuales duplicaciones.
4. Comprobar en el origen la fecha efectiva de actualización; no afirmar "tiempo real" sin evidencia.
5. Verificar funcionamiento real de la página en móvil y escritorio después del despliegue.

Documentación oficial sobre frecuencia de actualización:
https://docs.cloud.google.com/looker/docs/studio/manage-data-freshness

## Experiencia de usuario
Interfaz responsive, navegación por pestañas (panel, indicadores y fuente), barra inferior fija en móvil, botón para abrir el informe, recarga del visor y pantalla completa cuando la plataforma lo permite.

## Limitaciones de esta revisión
Se verificó la estructura y el código en GitHub. No se logró confirmar la carga pública del subdominio, ni leer el contenido o la fuente interna del informe desde las herramientas disponibles.

**La Movida de SST+** · De la Reacción a la Prevención

## Propiedades verificadas y cobertura (25 de octubre de 2026)

- **Moodle (`movidasst.org`):** propiedad GA4 `401557991`, flujo `G-D0YXTL06LN` («Mi Moodle»), zona horaria actual `America/Los_Angeles`. Es la fuente del informe original de Looker Studio y del corte reciente del observatorio. Pendiente cambiarla a `America/Santiago` en Administrador de GA4.
- **Web principal (`www.movidasst.com`):** propiedad `414669681` (en GA4 aparece con el nombre confuso «movidasst.org»), flujo `G-WQMF05XMJL` («Movidasst»), zona horaria ya `America/Santiago`. Se recuperó el histórico del 25-jul-2025 al 30-dic-2025. Archivo: [historico-web-ga4.json](./historico-web-ga4.json).
- **Academia:** propiedad `413672304` conectada en Windsor.ai, pero sin datos devueltos para el período de dos años consultado.
- **57 subdominios `.movidasst.com`:** código GA4 web corregido para usar `G-WQMF05XMJL` mediante [analytics.js del HUB](https://github.com/movidasst/principal/blob/main/analytics.js), con consentimiento previo y URL de página despersonalizada. Inventario [cobertura-ga4.json](./cobertura-ga4.json).
- **Diagnóstico de etiqueta:** `https://www.movidasst.com/diagnostico-ga4.html` (publicación y recepción de evento aún pendientes de confirmar con pruebas en navegador y DebugView).
- **Tablero:** 5 pestañas (Resumen, Audiencia, Canales, Histórico web, Fuentes). No suma usuarios activos entre propiedades como si fueran personas únicas. El histórico de la web principal se presenta en una vista separada del corte reciente de Moodle, evitando aparentar una tendencia continua donde faltan registros.
- **Limitación de publicación:** cambios comprobados en los repositorios de GitHub, no verificada su publicación pública ni la llegada a GA4 de eventos de los nuevos subdominios.
