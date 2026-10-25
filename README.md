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

## Cobertura GA4 (25 de octubre de 2026)
- Se añadió `G-D0YXTL06LN` (propiedad `401557991`, flujo «Mi Moodle») a los repositorios de **57 subdominios** en `movidasst.com`.
- Inventario por dominio y archivo: [cobertura-ga4.json](./cobertura-ga4.json).
- El JavaScript compartido `https://www.movidasst.com/analytics.js?v=20261025` y su CSS pertenecen a `movidasst/principal`.
- Las mediciones están supeditadas al consentimiento de cada visitante. Por privacidad el `page_view` registra el origen (dominio) sin parámetros de la URL ni títulos personales.
- Se han verificado las modificaciones en GitHub, **pero no todavía su publicación efectiva, la carga en navegadores ni el ingreso de eventos en GA4**.
- La propiedad reporta zona horaria `America/Los_Angeles`; confirmar si debe modificarse desde Administrar de GA4.
- En GA4, revisar informes por dimensión «Nombre de host» (`hostname`) en los próximos días, el reporte de Realtime, Tag Assistant, los filtros internos y los ajustes de medición mejorada.
- `movidasst.org` (Moodle) ya enviaba datos al flujo y no se editó desde GitHub.
