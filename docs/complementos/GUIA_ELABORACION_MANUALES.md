# 📘 Guía Maestra para la Elaboración de Manuales de Cuadros de Mando (CMI)

Esta guía establece el estándar de calidad para la documentación y manuales de usuario de Cuadros de Mando Integral (CMI), Dashboards y Soluciones de Business Intelligence (BI).

> **Objetivo**: Transformar datos complejos en herramientas accesibles y accionables mediante una documentación que inspire confianza y autonomía.

---

## 🏗️ 1. Principios Fundamentales

Un buen manual de CMI no es solo un instructivo técnico; es una herramienta de **alfabetización de datos**.

1. **Enfoque en el Negocio, no en la Herramienta**: Explicar *qué* preguntar a los datos, no solo dónde hacer clic.
2. **Claridad Visual**: Una imagen (o GIF) vale más que mil palabras. Capturas de pantalla anotadas son obligatorias.
3. **Lenguaje Estratégico**: Usar la terminología del usuario final (Directivo, Comercial, Operativo), evitando jerga técnica (ETL, Esquemas, JOINS) salvo en anexos.
4. **Navegación Intuitiva**: Estructurar el manual como el propio dashboard: De lo general a lo particular.

---

## 📝 2. Estructura Recomendada del Manual

### I. Introducción y Contexto (¿Para qué sirve?)

- **Propósito**: ¿Qué decisiones de negocio ayuda a tomar este cuadro de mando?
- **Audiencia**: ¿A quién va dirigido? (Ej: "Este informe es para Directores Regionales y Jefes de Equipo").
- **Preguntas Clave**: Listar las preguntas de negocio que responde el CMI.
  - *Ejemplo: "¿Estamos alcanzando el objetivo de ventas trimestral?"*

### II. Acceso y Requisitos

- URL de acceso (enlace directo al Power BI Service / Tableau Server).
- Credenciales o roles necesarios (RLS - Row Level Security).
- Navegadores soportados y dispositivos recomendados (PC vs Tablet/Móvil).

### III. Mapa de Navegación (La Interfaz)

- **Home/Landing Page**: Explicación del menú principal.
- **Filtros Globales vs. Filtros de Página**: Diferenciar claramente qué afecta a todo el reporte y qué es local.
- **Interactividad**: Guía rápida sobre *Drill-through* (obtener detalles), *Tooltips* (ventanas emergentes al pasar el ratón) y *Cross-filtering* (filtrado cruzado).

### IV. Diccionario de Indicadores (El Corazón del CMI)

Cada KPI debe tener una ficha técnica simplificada:

- **Nombre**: (Ej: Tasa de Conversión)
- **Definición de Negocio**: (Ej: Porcentaje de leads que se convierten en clientes finales).
- **Frecuencia de Actualización**: (Diaria, Mensual, Tiempo Real).
- **Dueño del Dato**: (Departamento responsable).
- **Semáforos/Alertas**: ¿Qué significa que esté en rojo? (Ej: < 80% del objetivo).

### V. Escenarios de Uso (Casos Prácticos)

Ejemplos de análisis paso a paso:

1. *Caso A: Analizar el rendimiento de un agente específico.*
2. *Caso B: Investigar la caída de ventas en una región.*

### VI. Solución de Problemas (Troubleshooting)

- "¿Por qué no veo datos de hoy?" (Explicar latencia de actualización).
- "¿Por qué mis números no cuadran con el CRM?" (Aclarar diferencias metodológicas o ventanas temporales).
- Contacto de soporte técnico.

---

## 🎨 3. Consejos de Estilo y Visualización

### Uso de Capturas de Pantalla

- **Anotaciones**: Usar flechas rojas o recuadros para resaltar el botón o área mencionada.
- **Contexto**: Mostrar suficiente pantalla para que el usuario se ubique, pero recortar lo irrelevante.
- **Datos Sensibles**: **SIEMPRE** difuminar o usar datos ficticios en las capturas del manual público.

### Formato de Texto

- Usar **negritas** para elementos de la interfaz (botones, menús).
- Usar *cursivas* para nombres de métricas o variables.
- Usar bloques de nota (Callouts) para advertencias importantes.

> ⚠️ **Importante**: Recuerda limpiar los filtros antes de tomar capturas para el manual.

---

## 🔄 4. Mantenimiento del Manual

El manual es un documento vivo.

- **Versionado**: Alinear la versión del manual con la versión del Dashboard (v1.0, v1.1).
- **Feedback**: Incluir un enlace en el propio manual o dashboard para reportar errores o dudas.
- **Revisión Trimestral**: Verificar que las capturas de pantalla sigan coincidiendo con la realidad del reporte actual.

---

## ✅ Checklist de Validación

Antes de publicar el manual, verifica:

- [ ] ¿El lenguaje es comprensible para alguien que no sea técnico?
- [ ] ¿Todas las capturas de pantalla están actualizadas?
- [ ] ¿Los enlaces funcionan?
- [ ] ¿Está claro quién es el soporte en caso de dudas?
- [ ] ¿Se explica cómo exportar los datos (Excel/PDF)?
