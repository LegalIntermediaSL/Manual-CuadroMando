# Anexo III: Manual Básico de Power BI para Usuarios de Negocio

Este anexo sirve como guía rápida para usuarios que se enfrentan por primera vez a Microsoft Power BI dentro del entorno del CMI-DAC.

---

## 1. Introducción al Ecosistema Power BI

### 1.1. ¿Qué es Power BI?

**Microsoft Power BI** es la solución líder mundial en *Business Intelligence* y análisis de datos empresarial (Líder en el Cuadrante Mágico de Gartner durante más de 15 años consecutivos).

No es un simple programa, sino una **plataforma unificada** que permite conectar cientos de fuentes de datos, prepararlos, analizarlos y presentarlos mediante informes visuales interactivos.

### 1.2. El Fabricante: Microsoft

Al ser un producto de Microsoft, se integra nativamente con todo el ecosistema de la empresa:

* Inicia sesión con su cuenta de **Office 365**.
* Exporta datos a **Excel** con un clic.
* Permite incrustar informes en **Teams** o SharePoint.

### 1.3. Licenciamiento Corporativo

El proyecto **CMI-DAC** opera bajo el modelo de licencia **Power BI Pro**, que habilita las funciones de colaboración segura y actualización automática en la nube.

Esta licencia es gestionada, suministrada y facturada íntegramente a través de la consultora: **T*Posiciona**.

---

## 2. Los 3 Pilares de Power BI

Power BI no es una sola aplicación, sino un conjunto de tres herramientas que trabajan en cadena:

1. **Power BI Desktop (El Taller)** 🛠️
    * Es un programa de escritorio (Windows).
    * **Función**: Aquí es donde el equipo técnico (Desarrolladores) *conecta* los datos, *crea* las fórmulas DAX y *diseña* los gráficos.
    * *El usuario final no suele usar esta herramienta.*

2. **Power BI Service (La Nube)** ☁️
    * Es el portal web (`app.powerbi.com`).
    * **Función**: Aquí es donde se *publica* el informe para que el CEO y los Jefes de Equipo lo consulten desde cualquier navegador. Es donde se configuran las alertas y las actualizaciones automáticas.

3. **Power BI Mobile (La App)** 📱
    * Aplicación para iOS y Android.
    * **Función**: Permite consumir los datos "on-the-go", ideal para reuniones fuera de la oficina o revisiones rápidas.

---

## 3. Conceptos Clave de la Interfaz

Al acceder al cuadro de mando, encontrará tres zonas principales de interacción:

### 2.1. El Lienzo (Canvas)

Es la zona central donde aparecen los gráficos, mapas y tarjetas de datos.

* **Interactividad**: Casi todo lo que ve es "clicable". Si hace clic en una barra de un gráfico, el resto de la página se filtrará para mostrar datos solo de esa categoría.

### 2.2. Panel de Navegación (Izquierda)

Permite moverse entre las diferentes páginas del informe (Overview, Agentes, Inmuebles, Financiero).

* *Nota: En la versión web, estas pestañas pueden aparecer en la parte inferior.*

### 2.3. Panel de Filtros (Derecha)

Es una barra lateral colapsable que permite refinar los datos.

* **Filtros de Página**: Afectan solo a la pantalla actual.
* **Filtros de Informe**: Afectan a todas las páginas del cuadro de mando.

---

## 3. Funcionalidades Básicas para el Usuario

### 3.1. Tooltips (Información sobre herramientas)

Pase el ratón por encima de cualquier punto de un gráfico sin hacer clic. Aparecerá una pequeña ventana emergente (negra o blanca) con detalles precisos de ese punto de datos.

* *Ejemplo: Al pasar el ratón sobre un mes en el gráfico de ventas, verá la cifra exacta y el % de variación respecto al año anterior.*

### 3.2. Drill-Through (Obtención de detalles)

Esta es una de las funciones más potentes. Permite "taladrar" un dato para ver qué hay debajo.

* **Cómo usarlo**: Haga clic derecho sobre una barra de un agente o una zona -> Seleccione "Obtener detalles" -> Elija la página de destino (ej. "Ficha de Agente").
* **Resultado**: Le llevará a una página detallada filtrada *exclusivamente* por el elemento sobre el que hizo clic.

### 3.3. Modo de Enfoque (Focus Mode)

Si un gráfico es demasiado pequeño:

1. Pase el ratón por la esquina superior derecha del gráfico.
2. Haga clic en el icono de "Enfoque" (un cuadrado con flechas salientes).
3. El gráfico ocupará toda la pantalla para un análisis detallado.

---

## 4. Exportación de Datos

¿Necesita los datos en Excel para trabajar con ellos?

1. Haga clic en los tres puntos (`...`) en la esquina superior derecha de cualquier visualización (tabla o gráfico).
2. Seleccione **Exportar datos**.
3. Elija el formato:
    * **Datos resumidos**: Lo que ve en el gráfico.
    * **Datos subyacentes**: (Si está habilitado) Todos los registros fila a fila que componen ese gráfico.
4. Se descargará un archivo `.csv` o `.xlsx` en su ordenador.

---

## 5. Aplicación Móvil

Power BI tiene una app nativa para iOS y Android.

* Descárguela desde la App Store o Google Play.
* Inicie sesión con sus credenciales corporativas.
* El CMI-DAC tiene una versión "Mobile Layout" optimizada para verse en vertical en su teléfono.

---

## 6. Glosario de Iconos Comunes

| Icono | Nombre | Función |
| :---: | :--- | :--- |
| 🔄 | **Restablecer filtros** | Devuelve la página a su estado original, borrando todas sus selecciones. |
| 🔖 | **Marcador** | Guarda la vista actual (con sus filtros aplicados) para acceder luego. |
| 📤 | **Compartir** | Permite enviar el informe por correo o Teams a otro compañero autorizado. |
| 🔔 | **Suscribirse** | Configura el envío automático de un PDF del informe a su email cada mañana. |
