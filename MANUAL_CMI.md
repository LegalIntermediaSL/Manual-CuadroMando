# Manual del Proyecto Cuadro de Mando Integral (CMI-DAC)

> 📊 **Manual Completo v2.5** - Documentación exhaustiva del Cuadro de Mando Integral para División de Agentes Consultores S.L.
> Última actualización: Febrero 2026

---

## 🎯 Acerca de Este Manual

Este manual documenta de forma integral el **CMI-DAC** (Cuadro de Mando Integral - Data Analytics Center), una herramienta estratégica de Business Intelligence diseñada específicamente para el sector inmobiliario. El manual está estructurado en **10 secciones** que cubren desde la introducción estratégica hasta la integración con otros sistemas.

**Audiencia**: Dirección, Mandos Intermedios, Agentes Comerciales, Equipo IT y Administradores de Sistema.

---

## 📚 Índice General

### [1. Introducción y Contexto Estratégico](docs/manual/secciones/01_Introduccion.md)

- 1.1. ¿Qué es el CMI-DAC?
- 1.2. Problema de Negocio que Resuelve
- 1.3. Audiencia Objetivo del Manual
- 1.4. Preguntas de Negocio Clave que Responde
- 1.5. Filosofía: De la Intuición a la Decisión Basada en Datos
- 1.6. Evolución Histórica del Proyecto
- 1.7. Beneficios Medibles Obtenidos
- 1.8. Cómo Leer Este Manual

### [2. Acceso y Requisitos de Sistema](docs/manual/secciones/02_Acceso_Requisitos.md)

- 2.1. URL de Acceso y Credenciales
- 2.2. Requisitos Técnicos (Hardware, Software, Red)
- 2.3. Compatibilidad con Navegadores y Dispositivos
- 2.4. Seguridad y Autenticación (SSO con Azure AD)
- 2.5. Row-Level Security (RLS): Qué Puedes Ver Según tu Rol
- 2.6. Proceso de Alta de Nuevos Usuarios
- 2.7. Recuperación de Contraseñas y Soporte Técnico
- 2.8. Política de Uso Aceptable

### [3. Guía de Navegación e Interfaz](docs/manual/secciones/03_Navegacion_Interfaz.md)

- 3.1. Mapa Conceptual del Dashboard
- 3.2. Tour Visual: Anatomía de una Página
- 3.3. Navegación entre Páginas
- 3.4. Sistema de Filtros (Globales, Locales, Cross-filtering)
- 3.5. Interactividad Avanzada: Tooltips Dinámicos y Drill-through
- 3.6. Marcadores y Favoritos
- 3.7. Exportación de Datos y Gráficos
- 3.8. Acceso Móvil: Power BI Mobile App
- 3.9. Personalización de Vista
- 3.10. Atajos de Teclado y Trucos de Productividad

### [4. Diccionario de Indicadores (KPIs)](docs/manual/secciones/04_Diccionario_KPIs.md)

- 4.1. Marco Conceptual: Balanced Scorecard (BSC)
- 4.2. Perspectiva Financiera (6 KPIs)
- 4.3. Perspectiva del Cliente (5 KPIs)
- 4.4. Perspectiva de Procesos Internos (5 KPIs)
- 4.5. Perspectiva de Aprendizaje y Crecimiento (4 KPIs)
- 4.6. Interpretación de Umbrales (Verde, Amarillo, Rojo)
- 4.7. Leading vs. Lagging Indicators
- 4.8. Matriz de Priorización de KPIs

### [5. Escenarios de Uso (Casos Prácticos)](docs/manual/secciones/05_Escenarios_Uso.md)

- 5.1. Caso Práctico #1: Análisis de Cierre Mensual
- 5.2. Caso Práctico #2: Evaluación de Desempeño Individual
- 5.3. Caso Práctico #3: Análisis de Rentabilidad por Zona
- 5.4. Caso Práctico #4: Detección de Inmuebles Zombi
- 5.5. Caso Práctico #5: Comparativa Temporal (YoY, MoM)
- 5.6. Caso Práctico #6: Análisis de Conversión del Funnel
- 5.7. Caso Práctico #7: Proyección de Objetivos Trimestrales
- 5.8. Caso Práctico #8: Identificación de Mejores Prácticas
- 5.9. Workflows para Cada Rol (CEO, Director, Agente)

### [6. Arquitectura Técnica y Mantenimiento](docs/manual/secciones/06_Arquitectura_Mantenimiento.md)

- 6.1. Infraestructura Cloud y Base de Datos
- 6.2. Arquitectura de Datos y Flujo de Información
- 6.3. Modelo de Base de Datos y Esquema (Star Schema)
- 6.4. Pipeline de Actualización Automática (ETL)
- 6.5. Monitorización y Mantenimiento Proactivo
- 6.6. Estrategia de Respaldo Híbrida
- 6.7. Plan de Continuidad de Negocio (Disaster Recovery)
- 6.8. Auditoría y Seguridad de la Información
- 6.9. Control de Versiones y Evolución del Software
- 6.10. Stack Tecnológico Detallado
- 6.11. Procesos ETL Documentados
- 6.12. Guía de Comandos de Mantenimiento
- 6.13. Procedimientos de Backup y Recuperación
- 6.14. Monitoreo y Observabilidad
- 6.15. Seguridad: Hardening del Sistema
- 6.16. Escalabilidad y Proyecciones de Crecimiento
- 6.17. Documentación para Desarrolladores

### [7. Glosario de Términos y Preguntas Frecuentes (FAQ)](docs/manual/secciones/07_Glosario_FAQ.md)

- 7.1. Glosario de Conceptos Clave
- 7.2. Preguntas Frecuentes Ampliadas (FAQ)
  - Sobre los Datos y Actualización
  - Sobre Acceso y Permisos
  - Sobre KPIs y Métricas
  - Sobre Navegación e Interfaz
  - Sobre Exportación y Compartición
  - Sobre Problemas Técnicos
  - Sobre Estrategia y Uso del CMI
- 7.3. Glosario Avanzado de Términos Específicos del Sector
- 7.4. Errores Comunes y Soluciones Rápidas
- 7.5. Recursos Adicionales y Formación
- 7.6. Directorio de Soporte Ampliado
- 7.7. Changelog de este Manual
- 7.8. Agradecimientos y Créditos

### [8. Casos de Éxito y Testimonios](docs/manual/secciones/08_Casos_Exito_Testimonios.md)

- 8.1. Métricas Globales de Impacto
- 8.2. Caso de Éxito #1: Oficina Norte - Transformación en 90 Días
- 8.3. Caso de Éxito #2: Agente "Rescatada" - De Bottom 3 a Top 5
- 8.4. Caso de Éxito #3: Decisión Estratégica Basada en Datos
- 8.5. Testimonios por Rol
- 8.6. Impacto Cualitativo: Cultura Organizacional
- 8.7. Reconocimientos Externos
- 8.8. Lecciones Aprendidas: Qué Funcionó y Qué No
- 8.9. Retorno de Inversión (ROI) Documentado
- 8.10. Testimonios en Video
- 8.11. Carta de Agradecimiento de la Dirección
- 8.12. Tu Historia Puede Estar Aquí

### [9. Roadmap y Evolución Futura](docs/manual/secciones/09_Roadmap_Evolucion.md)

- 9.1. Filosofía de Evolución Continua
- 9.2. Versión Actual y Releases Históricos
- 9.3. Roadmap 2026: Próximos 12 Meses
  - Q1 2026: Consolidación y Optimización ✅
  - Q2 2026: Inteligencia Artificial y Predicción 🔄
  - Q3 2026: Movilidad y Accesibilidad
  - Q4 2026: Colaboración y Social Features
- 9.4. Visión 2027-2028: Largo Plazo
- 9.5. Funcionalidades Solicitadas por Usuarios
- 9.6. Experimentos en Fase Beta
- 9.7. Tecnologías Emergentes en Radar
- 9.8. Política de Depreciación de Features
- 9.9. Cómo Influir en el Roadmap
- 9.10. Plan de Migración para Grandes Cambios
- 9.11. Inversión Prevista 2026-2028
- 9.12. Compromiso de Transparencia
- 9.13. Visión 2030: El CMI del Futuro
- 9.14. Invitación a Co-Crear el Futuro

### [10. Integración con Otros Sistemas](docs/manual/secciones/10_Integracion_Sistemas.md)

- 10.1. Filosofía de Integración
- 10.2. Integraciones Actuales (Production)
  - CRM Inmobiliario
  - ERP Contable (A3 Software)
  - Microsoft 365 (Azure AD)
  - Portales Inmobiliarios (Idealista)
- 10.3. Integraciones en Desarrollo (Q2-Q3 2026)
  - Google Analytics
  - WhatsApp Business API
  - Plataforma de Formación
- 10.4. Integraciones en Backlog (Futuras)
- 10.5. API del CMI: Integraciones Inversas
- 10.6. Casos de Uso de Integraciones
- 10.7. Arquitectura de Integración
- 10.8. Gestión de Errores de Integración
- 10.9. Mejores Prácticas de Integración
- 10.10. Solicitar Nueva Integración
- 10.11. Integraciones Rechazadas y Por Qué
- 10.12. Futuro: Integración Plug-and-Play
- 10.13. Monitoreo de Integraciones
- 10.14. Soporte para Integraciones

---

## 📖 Anexos y Documentación Complementaria

---

## 🚀 Inicio Rápido

Si es tu primera vez con el CMI-DAC:

1. 📖 **Lee primero**: [Sección 1 - Introducción](docs/manual/secciones/01_Introduccion.md)
2. 🔑 **Accede al sistema**: [Sección 2 - Acceso y Requisitos](docs/manual/secciones/02_Acceso_Requisitos.md)
3. 🧭 **Aprende a navegar**: [Sección 3 - Navegación e Interfaz](docs/manual/secciones/03_Navegacion_Interfaz.md)
4. 📊 **Comprende los KPIs**: [Sección 4 - Diccionario de KPIs](docs/manual/secciones/04_Diccionario_KPIs.md)
5. 💡 **Aplica casos prácticos**: [Sección 5 - Escenarios de Uso](docs/manual/secciones/05_Escenarios_Uso.md)

---

## 📋 Resumen Ejecutivo de Cada Sección

### 1. Introducción y Contexto Estratégico

Define qué es el CMI-DAC, por qué existe y cómo transforma la toma de decisiones en División de Agentes Consultores S.L. Explica la filosofía "data-driven" y los beneficios medibles obtenidos en el primer año.

### 2. Acceso y Requisitos de Sistema

Guía técnica para acceder al dashboard, requisitos de hardware/software, configuración de seguridad (SSO, RLS) y proceso de alta de usuarios.

### 3. Guía de Navegación e Interfaz

Tour visual completo del dashboard: anatomía de páginas, sistema de filtros, interactividad avanzada, exportación de datos y uso móvil.

### 4. Diccionario de Indicadores (KPIs)

Referencia completa de los 20 KPIs distribuidos en las 4 perspectivas del Balanced Scorecard, con fórmulas, interpretación y umbrales.

### 5. Escenarios de Uso (Casos Prácticos)

Guías paso a paso para situaciones reales: análisis de cierre mensual, evaluación de desempeño, detección de inmuebles zombi, comparativas temporales, etc.

### 6. Arquitectura Técnica y Mantenimiento

Documentación técnica completa: infraestructura cloud, modelo de datos, pipeline ETL, backups, seguridad, monitoreo y comandos de mantenimiento. **Destinado a IT.**

### 7. Glosario de Términos y FAQ

Diccionario de conceptos técnicos e inmobiliarios, más de 40 preguntas frecuentes resueltas, errores comunes y directorio de soporte.

### 8. Casos de Éxito y Testimonios

Historias reales de éxito tras implementar el CMI: métricas de impacto, testimonios por rol, análisis de ROI (592%) y reconocimientos externos.

### 9. Roadmap y Evolución Futura

Hoja de ruta estratégica 2026-2030: features planificadas, experimentos en beta, tecnologías emergentes, y cómo influir en el desarrollo del producto.

### 10. Integración con Otros Sistemas

Arquitectura de integraciones: CRM, ERP, Microsoft 365, portales inmobiliarios, APIs públicas, gestión de errores y solicitud de nuevas integraciones.

---

## 🛠️ Recursos Técnicos Adicionales

### Anexos

- [Anexo I: Diccionario de Datos Detallado](docs/anexos/Diccionario_Datos.md)
- [Anexo II: Guía de Despliegue en Digital Ocean](docs/anexos/Guia_Despliegue.md)
- [Anexo III: Manual Básico de Power BI](docs/anexos/Manual_PowerBI.md)
- [Anexo IV: Pantalla Interactiva Samsung 65"](docs/anexos/Pantalla_Tactil.md)
- [Anexo V: Infraestructura NAS y SAI](docs/anexos/Infraestructura_NAS_SAI.md)
- [Guía de Elaboración de Manuales](docs/complementos/GUIA_ELABORACION_MANUALES.md)

### Documentación Gráfica

- [Diagramas de Arquitectura](docs/graficos/Arquitectura.md)
- [Mockups de Paneles](docs/graficos/Mockups.md)
- [Capturas del Sistema Final](docs/graficos/Screenshots.md)

### Scripts y Código

El repositorio incluye scripts Python para ETL, mantenimiento y verificación de datos. Ver [README técnico del repositorio CMI-DAC](../CMI-DAC/README.md) para detalles de implementación.

---

## 📞 Contacto y Soporte

| Tipo de Consulta | Contacto | Horario | Tiempo Respuesta |
|------------------|----------|---------|------------------|
| **Acceso / Credenciales** | <it@dac-sl.es> | L-V 9-18h | 2-4 horas |
| **Cálculo de KPIs** | <bi@tposiciona.es> | L-V 9-14h | 24 horas |
| **Estrategia / Objetivos** | <comercial@dac-sl.es> | L-V 10-18h | 48 horas |
| **Propuestas de Mejora** | <bi@tposiciona.es> | Flexible | 2 semanas |
| **Emergencia (sistema caído)** | Guardia 24/7 | 24/7 | Inmediato |
| **Formación personalizada** | <rrhh@dac-sl.es> | L-V 9-14h | 1 semana |

---

## 🔄 Historial de Versiones del Manual

| Versión | Fecha | Cambios Principales |
|---------|-------|---------------------|
| **2.5** | Feb 2026 | ✅ Ampliación masiva: 10 secciones completas, +150 páginas de contenido |
| **2.2** | Dic 2025 | Mejoras en secciones 4 y 5, casos prácticos ampliados |
| **2.0** | Sep 2025 | Rediseño completo de estructura |
| **1.5** | May 2025 | Primera versión con secciones 1-7 |
| **1.0** | Abr 2025 | Versión inicial básica |

**Próxima revisión programada**: Agosto 2026

---

## 📊 Estadísticas del Manual

- **Páginas totales**: ~200 páginas
- **Diagramas Mermaid**: 25+
- **Ejemplos prácticos**: 50+
- **KPIs documentados**: 20
- **FAQs respondidas**: 40+
- **Casos de éxito**: 3 casos detallados
- **Testimonios**: 12 testimonios de usuarios reales

---

## 📝 Cómo Contribuir a Este Manual

Este manual es un documento vivo. Si detectas errores, tienes sugerencias de mejora o casos de uso adicionales que documentar:

1. **Erratas y correcciones**: Email a <bi@tposiciona.es> con referencia a la sección y línea
2. **Nuevos casos de uso**: Completa el [formulario de sugerencias](link-interno-sharepoint)
3. **Contribuciones técnicas**: Pull requests en el repositorio GitHub (solo equipo IT)

**Reconocimiento**: Las contribuciones significativas se reconocen en la sección de créditos.

---

## 🏆 Créditos

**Autor principal**: Equipo BI de T*Posiciona en colaboración con División de Agentes Consultores S.L.

**Colaboradores**:

- Equipo de Dirección de División de Agentes Consultores (definición estratégica)
- Usuarios beta (feedback y casos de uso reales)
- Equipo IT (documentación técnica)
- Diseñadores UX (diagramas y visualizaciones)

**Herramientas utilizadas**:

- Markdown + Mermaid (diagramas)
- Power BI + PostgreSQL (implementación)
- GitHub (control de versiones)

---

## 📜 Licencia y Derechos de Uso

© 2025-2026 División de Agentes Consultores S.L. y T*Posiciona. Todos los derechos reservados.

Este manual es **confidencial** y de uso exclusivo interno para empleados y colaboradores autorizados de División de Agentes Consultores S.L. Queda prohibida su distribución, reproducción o uso fuera de la organización sin autorización expresa por escrito.

**Clasificación de seguridad**: Confidencial - Uso Interno

---

## 🎯 Objetivo Final

> *"Transformar datos en decisiones, decisiones en acciones, y acciones en resultados medibles."*
>
> — Filosofía CMI-DAC

Este manual no es solo documentación técnica. Es una guía para construir una **cultura organizacional data-driven** donde cada decisión está informada por datos objetivos, cada resultado es medible, y cada miembro del equipo tiene visibilidad total sobre su contribución al éxito colectivo.

**¡Bienvenido al futuro de la gestión inmobiliaria basada en datos!** 🚀

---

*Última actualización: 15 de febrero de 2026*
*Manual CMI-DAC v2.5 - División de Agentes Consultores S.L.*
