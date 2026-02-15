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

![Rendimiento Agentes](../../graficos/agent_performance_mockup.png)

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

![Alertas Push](../../graficos/push_alerts_mockup.png)

---

## 3.4. Errores Comunes en la Navegación

* **"Los datos no cambian"**: Verifique que no tiene un filtro "olvidado" en el panel lateral. Use el botón **"Restablecer Filtros"** (icono de la goma de borrar) para volver al estado inicial.
* **"El mapa de calor se ve gris"**: Es un problema de carga de la API de mapas. Refresque el navegador (`F5`) o verifique su conexión a internet.
* **"Gráficos superpuestos"**: Esto ocurre si el zoom del navegador no es el 100%. Verifique la configuración de zoom en su navegador Chrome/Edge.

---

## 3.5. Anatomía de la Interfaz de Power BI

Entender los elementos de la interfaz le permitirá navegar con mayor fluidez:

```
┌─────────────────────────────────────────────────────────────────┐
│  🏠 CMI-DAC  │  📁 Workspace  │  🔍 Buscar  │  👤 Usuario    │
├─────────────────────────────────────────────────────────────────┤
│  ← → ⟳ Navegación        │  📅 Filtro Fecha  │  🔔 Alertas   │
├──────────────┬──────────────────────────────────────────────────┤
│              │  📊 KPI Principal: GCI = €450,000               │
│  📄 Páginas  │  ────────────────────────────────────────────   │
│              │                                                  │
│  • General   │  ┌──────────────┐  ┌──────────────┐            │
│  • Agentes   │  │  Gráfico 1   │  │  Gráfico 2   │            │
│  • Cartera   │  │  [Barras]    │  │  [Línea]     │            │
│  • Cliente   │  └──────────────┘  └──────────────┘            │
│  • Procesos  │                                                  │
│              │  ┌────────────────────────────────┐             │
│  🎛️ Filtros   │  │  Tabla Detalle                │             │
│              │  │  [Datos transaccionales]       │             │
│  📆 Fecha    │  └────────────────────────────────┘             │
│  🏢 Oficina  │                                                  │
│  👤 Agente   │                                                  │
│              │                                                  │
└──────────────┴──────────────────────────────────────────────────┘
```

### 🎯 Elementos Clave

| Elemento | Función | Ubicación |
|----------|---------|-----------|
| **Barra de Navegación Superior** | Cambiar entre workspaces, buscar dashboards | Top |
| **Panel de Páginas** | Listar todas las pestañas del informe | Izquierda |
| **Panel de Filtros** | Aplicar filtros globales o por página | Derecha (desplegable) |
| **Área de Visualización** | Muestra gráficos y tablas | Centro |
| **Breadcrumbs** | Navegación jerárquica | Debajo barra superior |
| **Botones de Acción** | Exportar, compartir, actualizar | Top-derecha de cada visual |

---

## 3.6. Atajos de Teclado Esenciales

Aumenta tu productividad con estos atajos:

### Windows / Linux

| Atajo | Acción |
|-------|--------|
| `Ctrl + S` | Guardar cambios (solo modo edición) |
| `Ctrl + F` | Buscar en página |
| `Ctrl + Shift + F` | Modo pantalla completa |
| `Ctrl + P` | Imprimir o exportar a PDF |
| `Ctrl + E` | Exportar datos del visual seleccionado |
| `Ctrl + Alt + V` | Pegar formato de visual |
| `F5` | Refrescar página |
| `Ctrl + F5` | Refrescar y limpiar caché |
| `Esc` | Cancelar selección actual |
| `Ctrl + Z` | Deshacer (modo edición) |
| `Tab` | Navegar entre visuales |

### macOS

| Atajo | Acción |
|-------|--------|
| `Cmd + S` | Guardar cambios |
| `Cmd + F` | Buscar |
| `Cmd + Shift + F` | Pantalla completa |
| `Cmd + P` | Imprimir/exportar |
| `Cmd + R` | Refrescar |

---

## 3.7. Gestos Táctiles (Tablet / Pantalla Touch)

El CMI está optimizado para pantallas táctiles en salas de reuniones y la pantalla de gran formato Samsung Flip.

![Samsung Flip](../../graficos/samsung_flip_mockup.png)

El CMI está optimizado para pantallas táctiles en salas de reuniones:

| Gesto | Acción |
|-------|--------|
| **Tap (1 dedo)** | Seleccionar elemento |
| **Double Tap** | Zoom en visual |
| **Tap prolongado** | Mostrar menú contextual |
| **Swipe horizontal (2 dedos)** | Cambiar de página |
| **Pinch (pellizco)** | Zoom in/out en mapas |
| **Drag (arrastrar)** | Mover mapa o scroll |
| **Tap en espacio vacío** | Deseleccionar filtros |

### 💡 Tip: Modo Presentación Táctil

Para reuniones en pantalla grande:

1. Activar modo pantalla completa (`Ctrl + Shift + F`)
2. Ocultar panel de filtros (ícono `>>` en la barra lateral)
3. Usar "Spotlight" para resaltar visuales específicos
4. Activar "Focus Mode" en un gráfico clave (botón `⛶`)

---

## 3.8. Mapa Completo de Páginas del Dashboard

El CMI-DAC se estructura en **8 páginas principales**:

### 🏠 Página 1: Visión General (Executive Summary)

**Audiencia**: CEO, Dirección
**Tiempo de lectura**: 30 segundos
**Elementos clave**:

* 🎯 Tarjeta GCI vs. Objetivo (grande, centrada)
* 📈 Sparklines de tendencia trimestral
* 🚦 Semáforos de las 4 perspectivas BSC
* 🗓️ Comparativa YoY

**Cuándo usarla**: Primera consulta del día, reuniones de estrategia

---

### 👥 Página 2: Análisis de Agentes

**Audiencia**: Jefes de Equipo, RRHH
**Tiempo de análisis**: 5-10 minutos
**Elementos clave**:

* 📊 Ranking de productividad (Top 10)
* 🎭 Matriz de desempeño (Captación vs. Cierre)
* 📉 Embudo de conversión individual
* 🎯 Comparativa agente vs. media del equipo

**Cuándo usarla**: Preparación de evaluaciones 1-on-1, detección de formación

---

### 🏡 Página 3: Cartera de Inmuebles

**Audiencia**: Coordinador de Ventas, Marketing
**Tiempo de análisis**: 10 minutos
**Elementos clave**:

* 🗺️ Mapa geográfico de inventario
* ⏱️ Distribución de DOM (Days on Market)
* 💰 Treemap por zona y precio
* 📋 Tabla de "inmuebles zombi" (>180 días)

**Cuándo usarla**: Auditoría semanal de inventario, ajustes de precio

---

### 🤝 Página 4: Perspectiva del Cliente

**Audiencia**: Director Comercial, Marketing
**Tiempo de análisis**: 8 minutos
**Elementos clave**:

* 🌟 NPS Score y evolución
* 📊 Funnel de conversión de leads
* 💶 CAC (Coste de Adquisición) por canal
* 📈 Ratio precio conseguido vs. inicial

**Cuándo usarla**: Planificación de campañas, análisis ROI marketing

---

### ⚙️ Página 5: Procesos Internos

**Audiencia**: Director de Operaciones
**Tiempo de análisis**: 10 minutos
**Elementos clave**:

* 🔄 Ciclo de vida promedio de una operación
* 📉 Tasa de caída (fall-through rate)
* 🎯 % de exclusivas en cartera
* ⏲️ Tiempo promedio de respuesta a leads

**Cuándo usarla**: Identificación de cuellos de botella, mejora de procesos

---

### 🚀 Página 6: Aprendizaje y Crecimiento

**Audiencia**: RRHH, Formación
**Tiempo de análisis**: 5 minutos
**Elementos clave**:

* 📚 Horas de formación por agente
* 💻 Tasa de adopción tecnológica (CRM)
* 😊 eNPS (Employee Net Promoter Score)
* 🔄 Tasa de rotación del equipo

**Cuándo usarla**: Planificación de formación, estrategia de retención

---

### 🔍 Página 7: Detalle Transaccional

**Audiencia**: Contabilidad, Auditoría
**Tiempo de análisis**: Variable (búsqueda específica)
**Elementos clave**:

* 📋 Tabla completa de operaciones
* 🔍 Búsqueda y filtrado avanzado
* 📥 Exportación selectiva
* 🧮 Cálculos personalizados

**Cuándo usarla**: Verificación de datos, auditorías, reconciliación

---

### 📊 Página 8: Comparativas Temporales

**Audiencia**: CFO, Analistas
**Tiempo de análisis**: 15 minutos
**Elementos clave**:

* 📅 YoY (Year-over-Year) por KPI
* 📈 Tendencias de largo plazo (3 años)
* 🎯 Cumplimiento de objetivos histórico
* 🔮 Proyecciones basadas en tendencia

**Cuándo usarla**: Presentaciones a inversores, planificación estratégica

---

## 3.9. Técnicas Avanzadas de Navegación

![Interfaz de Gestos](../../graficos/gesture_interface_mockup.png)

### 🎨 Uso de Highlight y Cross-Filtering

**Cross-Filtering** (Filtrado Cruzado):

```
1. Haga clic en "Madrid" en el gráfico de Zonas
2. TODOS los gráficos de la página se actualizan para mostrar solo Madrid
3. Haga clic en espacio vacío para quitar el filtro
```

**Highlight** (Resaltado):

```
1. Mantenga pulsado Ctrl (Cmd en Mac)
2. Haga clic en "Madrid" en el gráfico de Zonas
3. Los demás gráficos RESALTAN Madrid pero mantienen el contexto total
4. Útil para comparar sin perder visión general
```

### 🔍 Modo Focus y Drill-Through

**Focus Mode** (Modo Enfoque):

* Clic en el icono `⛶` de cualquier visual
* El gráfico se expande a pantalla completa
* Ideal para presentaciones o análisis profundo
* Presione `Esc` para salir

**Drill-Through** (Navegar a detalle):

```
Ejemplo:
1. En página "General", clic derecho en el agente "Carlos Gómez"
2. Seleccionar "Drill through" → "Detalle de Agente"
3. Se abre nueva página con el análisis completo de Carlos
4. Botón ← para volver a la vista anterior
```

### 🎯 Drill-Down Jerárquico

Algunos gráficos permiten "bajar" de nivel:

```
Año → Trimestre → Mes → Semana → Día
```

**Uso**:

1. Hacer doble clic en una barra/sector
2. El gráfico "baja" un nivel en la jerarquía
3. Botón ↑ (ir arriba) para volver al nivel superior

---

## 3.10. Personalización de Vistas con Bookmarks

Los **bookmarks** (marcadores) permiten guardar configuraciones de filtros y vistas:

### Crear un Bookmark Personal

1. Configurar la página como desea (filtros, zoom, etc.)
2. Clic en **Ver** → **Marcadores** → **Agregar**
3. Nombrar el bookmark (ej. "Mi Vista Semanal")
4. El bookmark queda guardado en tu perfil

### Tipos de Bookmarks

| Tipo | Descripción | Uso |
|------|-------------|-----|
| **Personal** | Solo tú lo ves | Vistas personalizadas recurrentes |
| **Compartido** | Lo ve todo el equipo | Vistas estándar para reuniones |
| **Con Datos** | Guarda también el estado de datos | Análisis histórico |
| **Sin Datos** | Solo guarda configuración visual | Plantillas de análisis |

### 💡 Bookmarks Recomendados por Rol

**CEO**:

* "Vista Matutina": GCI + YoY + Semáforos
* "Comparativa Oficinas": Ranking por oficina

**Jefe de Equipo**:

* "Mi Equipo Completo": Filtrado por su oficina
* "Alertas Semanales": Solo KPIs en rojo

**Agente**:

* "Mi Rendimiento": Solo sus propios datos
* "Comparativa Anónima": Su rendimiento vs. promedio

---

## 3.11. Exportación y Compartición de Datos

### 📥 Métodos de Exportación

| Formato | Uso Recomendado | Limitaciones |
|---------|-----------------|--------------|
| **PDF** | Presentaciones, informes impresos | Estático (no interactivo) |
| **PowerPoint** | Presentaciones ejecutivas | 1 visual por diapositiva |
| **Excel** | Análisis profundo, pivot tables | Máx. 150,000 filas |
| **CSV** | Importar a otros sistemas | Solo datos tabulares |
| **Imagen PNG** | Documentación, emails | Baja resolución en zoom |

### 🔗 Compartir un Dashboard

**Opción 1: Enlace Directo**

```
https://app.powerbi.com/groups/[workspace-id]/reports/[report-id]
```

* El destinatario DEBE tener permisos en el workspace

* No caduca
* Respeta Row-Level Security

**Opción 2: Publicar en Web** ⚠️

* Genera URL pública (PELIGRO: sin autenticación)
* Solo usar para datos no sensibles
* Requiere aprobación de administrador

**Opción 3: Suscripción por Email**

* Envía snapshot diario/semanal automático
* Formato PDF adjunto
* Configurable por página específica

---

## 3.12. Mejores Prácticas de Navegación

### ✅ Hacer

* **Empezar siempre por la Vista General** antes de profundizar
* **Usar filtros de fecha inteligentes** (Este Mes, Últimos 90 Días, YTD)
* **Verificar filtros activos** antes de tomar decisiones
* **Guardar bookmarks** de vistas recurrentes
* **Usar modo focus** para análisis profundo sin distracciones

### ❌ Evitar

* Navegar sin revisar qué filtros están aplicados
* Exportar datos masivos sin necesidad real
* Hacer zoom excesivo (>150%) que distorsiona visuales
* Mantener múltiples pestañas abiertas (consume RAM)
* Ignorar los tooltips (pasan información clave)

---

## 3.14. Consultas en Lenguaje Natural (Q&A)

El CMI permite "preguntar" a los datos en lenguaje humano (ej: "¿Cuál fue el agente con más cierres en Junio?").

![Preguntas y Respuestas](../../graficos/powerbi_qa.png)

---

## 3.15. Resolución de Problemas de Visualización

### 📊 "El gráfico muestra (Blank) o valores vacíos"

**Causas**:

* Datos realmente vacíos en ese filtro
* Campo calculado con error de fórmula
* Relación entre tablas rota

**Solución**:

1. Quitar todos los filtros y verificar si aparecen datos
2. Si persiste, reportar a IT con screenshot

### 🗺️ "El mapa no se visualiza correctamente"

![Vista de Mapa](../../graficos/map_mockup.png)

**Causas**:

* Geolocalización deshabilitada en el navegador
* API de Bing Maps bloqueada por firewall
* Coordenadas incorrectas en los datos

**Solución**:

1. Permitir geolocalización en configuración del navegador
2. Verificar conexión a internet
3. Usar visual alternativo (tabla o gráfico de barras)

### 🎨 "Los colores están diferentes a los de siempre"

**Causas**:

* Cambio de tema del informe por administrador
* Modo oscuro del sistema operativo
* Configuración de accesibilidad activa

**Solución**:

* Los colores son parte del diseño y solo pueden cambiarlos administradores
* Si afecta legibilidad, reportar a UX team
