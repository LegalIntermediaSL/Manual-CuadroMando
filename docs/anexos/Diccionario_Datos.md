# 📖 Diccionario de Datos Maestro - CMI-DAC

Este documento es la referencia oficial de la estructura de datos del proyecto **CMI-DAC**. Describe todas las tablas y campos presentes en la base de datos PostgreSQL (`cmi_realty`), diseñada para alimentar el Cuadro de Mando Integral en Power BI.

---

## 🏗️ Resumen del Modelo

El modelo sigue un esquema de **Estrella (Star Schema)** donde:

- **Tabla de Hechos**: `operaciones_inmobiliaria` (Transacciones)
- **Dimensiones**: `contactos` (Clientes), `agentes` (Personal), `inmuebles` (Propiedades).
- **Tablas de Apoyo**: `objetivos_agentes` (Metas) y `snapshot_mensual_operaciones` (Histórico).

---

## 1. Tabla: `operaciones_inmobiliaria`

Es la tabla principal que registra cada movimiento de venta o alquiler.

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id_operacion` | INT (PK) | Identificador único autoincremental de la operación. |
| `id_inmueble` | VARCHAR (FK) | Referencia a la tabla `inmuebles`. |
| `id_cliente` | VARCHAR (FK) | Referencia al `codigo_cliente` en la tabla `contactos`. |
| `fecha_captacion` | DATE | Fecha en la que se empezó a gestionar el inmueble. |
| `fecha_publicacion` | DATE | Fecha en la que se publicó en portales/web. |
| `fecha_venta` | DATE | Fecha de cierre de la operación (clave para KPIs financieros). |
| `tipo_operacion` | VARCHAR | 'Venta' o 'Alquiler'. |
| `tipo_inmueble` | VARCHAR | Piso, Chalet, Local, etc. |
| `provincia` | VARCHAR | Provincia de ubicación. |
| `ciudad` | VARCHAR | Ciudad de ubicación. |
| `superficie_m2` | NUMERIC | Metros cuadrados construidos. |
| `precio_venta_o_alquiler_eur` | NUMERIC | Precio final de la transacción. |
| `comision_eur` | NUMERIC | Comisión bruta generada para la empresa. |
| `costes_marketing_directo_eur`| NUMERIC | Gasto directo en publicidad para esta operación. |
| `id_agente_captador` | INT (FK) | ID del agente que consiguió la captación. |
| `id_agente_cierre` | INT (FK) | ID del agente que cerró la operación. |
| `fuente_lead` | VARCHAR | Origen del cliente (Idealista, Web, Referido). |
| `id_portal` | VARCHAR (FK) | ID del portal donde se originó el lead (ROI-P Tracking). |
| `en_exclusiva` | BOOLEAN | Indica si la gestión fue exclusiva (TRUE/FALSE). |

---

## 2. Tabla: `contactos`

Base de datos de Clientes y Leads.

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | INT (PK) | ID técnico interno. |
| `codigo_cliente` | VARCHAR (UK) | Código de negocio (ej. C001). Usado como enlace con operaciones. |
| `primer_nombre` | VARCHAR | Nombre del cliente. |
| `apellidos` | VARCHAR | Apellidos del cliente. |
| `tipo` | VARCHAR | Categoría (Cliente, Lead, Inversor). |
| `telefono` | VARCHAR | Teléfono de contacto. |
| `email` | VARCHAR | Correo electrónico. |
| `direccion` | TEXT | Dirección completa. |
| `origen` | VARCHAR | Fuente de donde provino el contacto. |
| `lead_score` | INT | Puntuación IA de probabilidad de cierre (0-100). |
| `fecha_creacion` | TIMESTAMP | Fecha de alta en el sistema. |

---

## 3. Tabla: `agentes`

Catálogo de la fuerza de ventas.

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | INT (PK) | Identificador único del agente. |
| `nombre` | VARCHAR (UK) | Nombre completo del agente (usado para visualización). |
| `email` | VARCHAR | Email corporativo. |
| `oficina` | VARCHAR | Oficina a la que pertenece (Madrid, Barcelona, etc.). |
| `puesto` | VARCHAR | Cargo (Asesor, Gerente, Captador). |
| `activo` | BOOLEAN | Indica si el agente está actualmente en la plantilla. |

---

## 4. Tabla: `inmuebles`

Inventario de propiedades gestionadas.

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id_inmueble` | VARCHAR (PK) | Referencia única de la propiedad (ej. REF-123). |
| `tipo_inmueble` | VARCHAR | Tipología (Piso, Ático, etc.). |
| `direccion` | VARCHAR | Dirección exacta. |
| `ciudad` | VARCHAR | Municipio. |
| `provincia` | VARCHAR | Provincia. |
| `superficie_m2` | NUMERIC | Tamaño del inmueble. |
| `precio_eur` | NUMERIC | Último precio de salida conocido. |
| `certificado_energetico`| CHAR(1) | Letra de eficiencia (A-G). |
| `esg_score` | INT | Puntuación de sostenibilidad (0-100). |

---

## 5. Tabla: `objetivos_agentes`

Define las metas que se comparan con los resultados reales.

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id_objetivo` | INT (PK) | ID único de la meta. |
| `id_agente` | INT (FK) | Referencia al agente. |
| `mes` | DATE | Mes al que aplica el objetivo (siempre día 1). |
| `monto_objetivo` | NUMERIC | Dinero en comisiones que debe generar. |
| `cantidad_operaciones_objetivo`| INT | Número de cierres esperados. |

---

## 6. Tabla: `snapshot_mensual_operaciones`

Tabla histórica para analizar la evolución del pipeline.

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id_snapshot` | INT (PK) | ID de registro. |
| `fecha_corte` | DATE | Último día del mes al que corresponde la foto. |
| `id_operacion` | INT (FK) | Referencia a la operación. |
| `estado_al_corte` | VARCHAR | En qué fase estaba la operación en esa fecha. |
| `dias_en_cartera` | INT | Tiempo que llevaba activa en ese momento. |
