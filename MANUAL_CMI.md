# Manual del Proyecto Cuadro de Mando Integral (CMI-DAC)

> ⚠️ Este manual documenta el proyecto alojado en el repositorio [CMI-DAC](../CMI-DAC).

## 📚 Índice General

1. [Introducción y Contexto Estratégico](#1-introducción-y-contexto-estratégico)
    1.1. Propósito del CMI
    1.2. Audiencia Objetivo
    1.3. Preguntas de Negocio Clave
2. [Acceso y Requisitos de Sistema](#2-acceso-y-requisitos-de-sistema)
    2.1. URL de Acceso y Credenciales
    2.2. Requisitos de Hardware y Red
    2.3. Seguridad y Permisos (RLS)
3. [Guía de Navegación e Interfaz](#3-guía-de-navegación-e-interfaz)
    3.1. Mapa del Menú Principal
    3.2. Uso de Filtros (Globales vs. Locales)
    3.3. Interactividad: Tooltips y Drill-through
4. [Diccionario de Indicadores (KPIs)](#4-diccionario-de-indicadores-kpis)
    4.1. Perspectiva Financiera
    4.2. Perspectiva del Cliente
    4.3. Perspectiva de Procesos Internos
    4.4. Perspectiva de Aprendizaje y Crecimiento
5. [Escenarios de Uso (Casos Prácticos)](#5-escenarios-de-uso-casos-prácticos)
    5.1. Análisis de Cierre Mensual
    5.2. Evaluación de Desempeño por Agente
6. [Arquitectura Técnica y Mantenimiento](#6-arquitectura-técnica-y-mantenimiento)
    6.1. Stack Tecnológico
    6.2. Modelo de Datos y Esquema
    6.3. Pipeline de Actualización (ETL)
    6.4. Gestión de Incidencias y Soporte
7. [Anexos](#7-anexos)
8. [Documentación Gráfica](#8-documentación-gráfica)

---

## 1. Introducción y Contexto Estratégico

*(Pendiente de desarrollo)*

## 2. Acceso y Requisitos de Sistema

*(Pendiente de desarrollo)*

## 3. Guía de Navegación e Interfaz

*(Pendiente de desarrollo)*

## 4. Diccionario de Indicadores (KPIs)

*(Pendiente de desarrollo)*

## 5. Escenarios de Uso (Casos Prácticos)

*(Pendiente de desarrollo)*

## 6. Arquitectura Técnica y Mantenimiento

### 6.1. Stack Tecnológico

El proyecto se basa en una arquitectura moderna y escalable:

- **Frontend**: Microsoft Power BI (Visualización) y Streamlit (Panel de Administración).
- **Backend**: Python 3.11+ (ETL, API, Scripts de Mantenimiento).
- **Base de Datos**: PostgreSQL 15 (Managed Database en Digital Ocean) con conexión SSL obligatoria.
- **Infraestructura**: Docker y Docker Compose para orquestación de servicios; Digital Ocean Droplets (Ubuntu 24.04 LTS) como servidor de aplicaciones.

### 6.2. Modelo de Datos y Esquema

La base de datos `cmi_realty` utiliza un enfoque híbrido:

1. **Capa Física (Tablas)**: Almacena los datos crudos y normalizados tras el proceso ETL.
    - `operaciones_inmobiliaria`: Tabla transaccional maestra.
    - `contactos`, `agentes`, `inmuebles`: Tablas dimensionales base.
2. **Capa Lógica (Vistas)**: Transforma los datos en un **Modelo en Estrella (Star Schema)** optimizado para Power BI.
    - `fact_operaciones`: Tabla de hechos enriquecida con métricas pre-calculadas (ej. `dias_ciclo_venta`).
    - `dim_calendario`: Generada dinámicamente para inteligencia temporal.
    - `dim_agentes`, `dim_contactos`, `dim_inmuebles`: Dimensiones limpias para filtrado.

*(Para el detalle campo por campo, consultar el [Anexo I: Diccionario de Datos](docs/anexos/Diccionario_Datos.md))*

### 6.3. Pipeline de Actualización (ETL)

El script maestro `run_pipeline.py` orquesta la actualización:

1. **Extract**: Lee datos de fuentes locales (CSV) o APIs.
2. **Transform**: Limpia datos, normaliza fechas y valida tipos.
3. **Load**: Carga datos en PostgreSQL mediante `load_data_to_postgresql.py` (TRUNCATE + INSERT).
4. **Verify**: Ejecuta tests de integridad (`verify_dax_logic.py`) y genera un reporte de salud.

### 6.4. Gestión de Incidencias y Soporte

- **Bitácora**: Todo cambio debe registrarse en `Bitacora_Seguimiento.md`.
- **Monitorización**: El sistema incluye scripts de alerta (`check_fact_cols.py`) que notifican si el esquema de la base de datos cambia inesperadamente.

## 7. Anexos

En esta sección se detallan documentos técnicos específicos y referencias adicionales.

- [Anexo I: Diccionario de Datos Detallado](docs/anexos/Diccionario_Datos.md)
- [Anexo II: Guía de Despliegue en Digital Ocean](docs/anexos/Guia_Despliegue.md)
- [Anexo III: Estructura de Directorios del Repositorio](docs/anexos/Estructura_Directorios.md)
- [Anexo IV: Guía de Elaboración de Manuales](docs/complementos/GUIA_ELABORACION_MANUALES.md)

## 8. Documentación Gráfica

Repositorio de diagramas, capturas de pantalla y esquemas visuales del proyecto.

- [Diagramas de Arquitectura](docs/graficos/Arquitectura.md)
- [Mockups de Paneles](docs/graficos/Mockups.md)
- [Capturas del Sistema Final](docs/graficos/Screenshots.md)
