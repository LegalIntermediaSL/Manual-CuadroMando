# 7. Glosario de Términos y Preguntas Frecuentes (FAQ)

Este capítulo sirve como referencia rápida para resolver dudas terminológicas y operativas comunes sin necesidad de recorrer todo el manual.

---

## 7.1. Glosario de Conceptos Clave

### 🅰️ Conceptos Analíticos (Business Intelligence)

* **Balanced Scorecard (BSC)**: Metodología de gestión estratégica que permite medir la evolución de una empresa desde cuatro perspectivas: Financiera, Cliente, Procesos y Aprendizaje.
* **CMI (Cuadro de Mando Integral)**: Herramienta visual que traduce la estrategia en indicadores medibles.
* **Dashboard**: Interfaz gráfica (en Power BI) que presenta los KPIs de forma visual e interactiva.
* **ETL (Extract, Transform, Load)**: Proceso técnico que extrae datos de fuentes sucias (Excel, CRM), los limpia y los carga en la base de datos oficial.
* **Leading Indicator (Indicador Adelantado)**: Métrica que predice resultados futuros (ej. la Captación hoy predice la Venta en 3 meses).
* **Lagging Indicator (Indicador Retardado)**: Métrica que mide resultados pasados (ej. el GCI de este mes).

### 🏠 Conceptos Inmobiliarios (Real Estate)

* **DOM (Days on Market)**: Tiempo que tarda una propiedad en venderse desde su publicación.
* **Exclusiva**: Mandato de venta único que permite a la agencia invertir recursos con garantía de retorno.
* **GCI (Gross Commission Income)**: Honorarios brutos generados por una operación.
* **Lead**: Persona interesada que deja sus datos de contacto para recibir información sobre un inmueble o servicio.
* **Listing**: Propiedad activa en cartera disponible para la venta o alquiler.
* **NOI (Net Operating Income)**: El beneficio neto tras pagar todos los gastos operativos del negocio.

---

## 7.2. Preguntas Frecuentes (FAQ)

### ❓ ¿Por qué no coinciden mis datos de Power BI con mi Excel personal?

**Respuesta**: Power BI se actualiza mediante un proceso ETL que filtra duplicados y valida datos. Si hay una diferencia, lo más probable es que su Excel personal contenga una operación que aún no ha sido marcada como "Cobrada" en el sistema oficial o no cumple con los criterios de integridad.

### ❓ ¿Con qué frecuencia se actualizan los gráficos?

**Respuesta**: Automáticamente cada madrugada a las 05:00 AM. Si necesita una actualización "en caliente" durante el día, debe solicitarla al administrador técnico.

### ❓ ¿Puedo descargar los datos a mi ordenador?

**Respuesta**: Sí, Power BI permite exportar casi cualquier visualización a **Excel o CSV**. Sin embargo, recuerde que el uso de estos datos está sujeto a la política de protección de datos (RGPD) de la empresa.

### ❓ ¿Qué significa si un KPI aparece en "Rojo"?

**Respuesta**: Significa que el valor actual está por debajo del 80% del objetivo marcado por la dirección para ese periodo. Requiere una revisión inmediata de la causa en la reunión de equipo.

### ❓ He detectado un error en un nombre de agente, ¿cómo lo cambio?

**Respuesta**: Los errores de datos "maestros" deben corregirse en la fuente de origen (CRM o Base de Datos DIM_AGENTES). Power BI reflejará el cambio automáticamente en la siguiente actualización nocturna.

---

## 7.3. Directorio de Soporte

Si tras consultar este manual sigue teniendo dudas técnicas o analíticas, contacte con:

* **Soporte Técnico (IT)**: <it@legalintermedia.com> (Problemas de acceso o conexión).
* **Analista de Datos**: <bi@posiciona.com> (Dudas sobre el cálculo de KPIs).
* **Dirección Comercial**: <comercial@legalintermedia.com> (Dudas sobre objetivos y estrategia).
