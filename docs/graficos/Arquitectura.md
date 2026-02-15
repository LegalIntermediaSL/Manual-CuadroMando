# Diagrama de Arquitectura del Sistema CMI-DAC

Este gráfico describe la arquitectura técnica, desde las fuentes de datos hasta la visualización final.

```mermaid
graph TD
    subgraph Fuentes [Fuentes de Datos]
        CRM[CRM Inmobiliario]
        XLS[Excel Históricos]
        PORT[Portales Inmobiliarios]
    end

    subgraph ETL [Capa de Procesamiento - Python]
        Extract[Extracción API/CSV]
        Transform[Limpieza y Validación]
        Load[Carga PostgreSQL]
    end

    subgraph Almacenamiento [Nube - Digital Ocean]
        DB[(PostgreSQL DB)]
    end

    subgraph Visualizacion [Capa de Negocio]
        PBI[Power BI Service]
        Mobile[App Móvil]
        WEB[Portal Web]
    end

    CRM --> Extract
    XLS --> Extract
    PORT --> Extract
    Extract --> Transform
    Transform --> Load
    Load --> DB
    DB --> PBI
    PBI --> Mobile
    PBI --> WEB

    style DB fill:#336791,color:#fff
    style ETL fill:#f9f,stroke:#333,stroke-width:2px
```

## Descripción de Componentes

1. **Fuentes**: Datos crudos de diversas plataformas.
2. **ETL**: Scripts Python ejecutados mediante CRON en Digital Ocean.
3. **Base de Datos**: PostgreSQL para almacenamiento robusto y seguro.
4. **Power BI**: Motor de visualización y modelado de datos.
