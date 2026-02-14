# 3. Guía de Navegación e Interfaz de Usuario

Este manual describe cómo sacar el máximo partido a la interfaz de Power BI diseñada para el CMI-DAC. La experiencia de usuario se ha optimizado para ser simple, intuitiva y rápida, permitiendo moverse entre miles de datos en cuestión de segundos.

---

## 3.1. Estructura General del Dashboard

El Cuadro de Mando se organiza en **cuatro páginas principales**, accesibles desde las pestañas inferiores o el menú lateral de navegación (según la versión de Power BI):

### 🏠 1. Visión General (Overview)

* **Propósito**: Resumen ejecutivo de alto nivel para el CEO y Directores.
* **Contenido Clave**:
  * Tarjetas con los KPIs más importantes: GCI Total, Nº Operaciones, Rentabilidad.
  * Evolución mensual de ingresos y ventas.
  * Termómetros de cumplimiento de objetivos anuales.

### 👤 2. Análisis de Rendimiento por Agente

* **Propósito**: Comparar y evaluar el desempeño individual del equipo comercial.
* **Contenido Clave**:
  * Ranking de agentes por Ingresos (GCI) y Nº Operaciones.
  * Gráfico de dispersión (Scatter Plot) para identificar "Estrellas" (altos ingresos, muchas ventas) vs. "Bajo Rendimiento".
  * Métricas de actividad (Visitas, Llamadas, Captaciones).

### 🏘️ 3. Análisis de Cartera de Inmuebles

* **Propósito**: Gestión del stock y rotación de producto.
* **Propósito**: Gestión del stock y rotación de producto.
* **Contenido Clave**:
  * Distribución de la cartera por Tipo (Piso, Casa, Local) y Zona.
  * Análisis de "Días en Mercado" (DOM) para detectar propiedades estancadas.
  * Mapa interactivo de propiedades activas y vendidas.

### 💰 4. Análisis Financiero y Márgenes

* **Propósito**: Profundizar en la rentabilidad de las operaciones.
* **Contenido Clave**:
  * Desglose de costes directos vs. beneficio bruto.
  * Comisiones medias y Ticket Medio por tipo de operación.
  * Análisis de desviaciones presupuestarias.

---

### 🗺️ Diagrama de Navegación Lógica

```mermaid
graph TD
    Home[🏠 Visión General<br/>(Overview)]
    Agentes[👤 Análisis de Agentes]
    Inmuebles[🏘️ Análisis de Inmuebles]
    Finanzas[💰 Análisis Financiero]

    Home -->|Drill-Through| Detalle[📄 Ficha de Detalle de Operación]
    Agentes -->|Drill-Through| DetalleAgente[📄 Ficha de Detalle Agente]
    
    Home -.->|Navegación| Agentes
    Home -.->|Navegación| Inmuebles
    Home -.->|Navegación| Finanzas

    style Home fill:#bbdefb,stroke:#0d47a1,stroke-width:2px
    style Detalle fill:#fff9c4,stroke:#fbc02d,stroke-dasharray: 5 5
    style DetalleAgente fill:#fff9c4,stroke:#fbc02d,stroke-dasharray: 5 5
```

---

## 3.2. Panel de Filtros y Segmentación

La potencia del CMI reside en su capacidad de **filtrar** y **cruzar** datos al instante. En la parte derecha (o superior) encontrará el panel de control:

* **📅 Rango de Fechas (Time Intelligence)**:
  * Selector de año y mes: Permite ver datos "YTD" (Year-to-Date) o de un mes específico.
  * Botones rápidos: "Este Semestre", "Último Trimestre", "Año Anterior (Comparativa)".

* **🏢 Tipo de Operación**:
  * Selector simple para alternar entre "Venta", "Alquiler" o "Ambos".
  * Esto actualiza todos los KPIs financieros automáticamente.

* **📍 Ubicación Geográfica**:
  * Filtros jerárquicos por Provincia -> Ciudad -> Código Postal.

* **👥 Agente / Equipo**:
  * Lista desplegable para analizar un agente individual o comparar varios simultáneamente.

---

## 3.3. Interactividad Avanzada (Drill-Down y Cross-Filtering)

El diseño visual permite interactuar directamente con los gráficos, no solo mirarlos:

### 🖱️ Cross-Filtering (Filtrado Cruzado)

* **¿Qué es?**: Al hacer clic en una barra de un gráfico (ej. la barra de "Marzo" en ventas mensuales), **todo el resto de la página se filtra** por esa selección.
* **Ejemplo**: Si hace clic en el sector "Madrid" de un gráfico circular, la tabla de agentes mostrará solo las ventas de Madrid.
* **Deshacer**: Vuelva a hacer clic en el mismo elemento o en un espacio en blanco para quitar el filtro.

### 🔍 Drill-Through (Profundizar Detalles)

* **¿Qué es?**: Le permite saltar de un resumen general al detalle específico de una operación.
* **Cómo usarlo**:
    1. Haga clic derecho sobre una barra de un gráfico de agentes.
    2. Seleccione **"Obtener detalles" (Drill-through) -> Ver Ficha de Agente**.
    3. Esto le llevará a una página oculta con el detalle minucioso de todas las operaciones de ese agente.

### 👆 Tooltips (Información sobre Herramienta)

* Pase el ratón sobre cualquier punto de un gráfico para ver una ventana emergente con datos precisos (valores exactos, porcentajes de variación, etc.) que no caben en el visual principal.

---

## 3.4. Consejos para Reuniones Ejecutivas

* Use el **Modo Pantalla Completa** (icono de flechas en la barra inferior) para presentaciones sin distracciones.
* Utilice los **Marcadores** (Bookmarks) si ha guardado vistas específicas (ej. "Revisión Mensual Madrid") para acceder a ellas con un clic.
* En pantallas táctiles, use el gesto de "pellizcar" para hacer zoom en mapas o gráficos densos.
