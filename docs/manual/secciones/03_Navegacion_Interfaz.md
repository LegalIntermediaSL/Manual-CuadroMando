# 3. Guía de Navegación e Interfaz de Usuario

Este manual describe cómo sacar el máximo partido a la interfaz de Power BI diseñada para el CMI-DAC. La experiencia de usuario se ha optimizado para ser simple, intuitiva y rápida, permitiendo moverse entre miles de datos en cuestión de segundos.

---

## 3.1. Estructura General del Dashboard: La Jerarquía de la Información

El Cuadro de Mando se organiza bajo una arquitectura de "Embudo de Datos", permitiendo al usuario pasar de lo macro a lo micro en tres niveles:

### 🏠 Nivel 1: El Cuadro de Mando Ejecutivo (La Gran Imagen)

* **Pestaña**: `Visión General`
* **Propósito**: Consultar en 5 segundos el estado de la empresa.
* **Elementos Visuales Críticos**:
  * **Tarjetas de Gran Formato**: Muestra el GCI real vs. Presupuesto.
  * **Sparklines (Mini-gráficos de tendencia)**: Ubicados bajo las tarjetas para ver si el KPI está subiendo o bajando sin mirar tablas.
  * **Semáforos de Desempeño**: Círculos de color (Verde/Amarillo/Rojo) que indican el estado de salud sin leer números.

### 👤 Nivel 2: Analítica Táctica (El Rendimiento del Equipo)

* **Pestaña**: `Análisis de Agentes` y `Cartera`
* **Propósito**: Identificar qué piezas del engranaje están funcionando.
* **Gráficos Clave**:
  * **Gráfico de Embudo (Funnel)**: Visualiza la pérdida de eficiencia desde que entra un lead hasta que se cierra el contrato. Vital para detectar dónde "se nos escapan" los clientes.
  * **Treemap (Mapa de Árbol)**: Categoriza la cartera por volumen de precio. Los cuadros más grandes representan las zonas con más stock.

### � Nivel 3: Analítica Operativa (El Dato Atómico)

* **Pestaña**: `Detalle Transaccional`
* **Propósito**: Auditoría y verificación de datos.
* **Interactividad**: Tablas dinámicas con capacidad de ordenación por cualquier columna (Precio Medio, Comisión, Fecha).

---

## 3.2. Dominando la Interactividad: "Data Storytelling"

A diferencia de un informe en PDF, el CMI-DAC permite "interrogar" a los datos.

### 🖱️ El Poder del Filtrado Cruzado (Cross-Filtering)

Al hacer clic en cualquier elemento visual (ej. el sector "Pisos" de un gráfico circular), **automáticamente todos los demás gráficos de la página se recalculan** para mostrar solo la información relativa a "Pisos".

* **Sugerencia Estratégica**: Seleccione "Pisos" y luego en el gráfico de zonas haga clic en "Centro". Verá instantáneamente cuántos pisos tiene en el centro, quién es el mejor agente en ese nicho y qué margen neto dejan esas operaciones.

### 🔍 Tooltips Dinámicos (Ventanas Emergentes)

Al pasar el cursor sobre un punto de datos (ej. una barra de un agente), no solo verá un número. Hemos configurado **Visual Tooltips**: una pequeña ventana que muestra un mini-informe del historial de ese agente en los últimos 6 meses, sin necesidad de cambiar de página.

---

## 3.3. Configuración y Guardado de Vistas (Bookmarks)

Cada directivo tiene sus propias necesidades. El sistema permite personalizar la navegación:

1. **Vistas Personales**: Si usted siempre filtra por "Oficina Norte" y "Venta", puede guardar esa configuración como un **Bookmark Personal**.
2. **Exportación Selectiva**: Si necesita un gráfico para una presentación de PowerPoint, use el icono de "Exportar a PowerPoint" o "Captura de Visual" en la cabecera del gráfico.
3. **Alertas de Datos**: Configure alertas en las tarjetas de KPI principales. Por ejemplo: "Avisarme al correo si el GCI supera los 100.000€ este mes".

---

## 3.4. Errores Comunes en la Navegación

* **"Los datos no cambian"**: Verifique que no tiene un filtro "olvidado" en el panel lateral. Use el botón **"Restablecer Filtros"** (icono de la goma de borrar) para volver al estado inicial.
* **"El mapa de calor se ve gris"**: Es un problema de carga de la API de mapas. Refresque el navegador (`F5`) o verifique su conexión a internet.
* **"Gráficos superpuestos"**: Esto ocurre si el zoom del navegador no es el 100%. Verifique la configuración de zoom en su navegador Chrome/Edge.
