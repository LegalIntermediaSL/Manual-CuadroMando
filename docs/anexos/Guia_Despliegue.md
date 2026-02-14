# 🚀 Guía de Despliegue en Digital Ocean (Anexo II)

Este documento detalla el procedimiento técnico para desplegar y mantener la infraestructura del CMI-DAC en la nube, asegurando alta disponibilidad y seguridad para la conexión con Power BI.

## 1. Arquitectura de Despliegue

El sistema utiliza una arquitectura híbrida optimizada para costes y rendimiento:

* **Proveedor Cloud**: Digital Ocean.
* **Base de Datos**: PostgreSQL Gestionado (Managed Database).
* **Servidor de Aplicaciones (ETL)**: Droplet (VPS) con Ubuntu 24.04 LTS.

---

## 2. Aprovisionamiento de Recursos

### 2.1. Base de Datos Gestionada (PostgreSQL)

1. Acceder al panel de Digital Ocean -> **Databases** -> **Create Database Cluster**.
2. **Motor**: PostgreSQL 15 (o superior).
3. **Plan**: Basic Node (1 GB RAM / 10 GB Storage) - Suficiente para el volumen actual.
4. **Región**: Seleccionar la más cercana (ej. Amsterdam o Londres) para minimizar latencia.
5. **Seguridad (Trusted Sources)**:
    * Añadir la IP del Droplet de Aplicaciones.
    * Añadir la IP fija de la oficina (si existe).
    * **Importante**: Descargar el certificado CA (`ca-certificate.crt`) necesario para la conexión SSL.

### 2.2. Servidor de Aplicaciones (Droplet)

1. **Crear Droplet**: Ubuntu 24.04 LTS x64.
2. **Plan**: Basic (Regular Intel) - 1 GB / 1 CPU.
3. **Autenticación**: Configurar clave SSH para acceso root.
4. **Firewall**:
    * Inbound: SSH (22) solo desde IPs autorizadas.
    * Outbound: Todo permitido (para conectar a APIs externas).

---

## 3. Configuración del Entorno

### 3.1. Preparación del Droplet

Conectarse vía SSH y ejecutar:

```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python y dependencias de sistema
sudo apt install python3-pip python3-venv postgresql-client -y

# Clonar el repositorio (usando Deploy Key o Token)
git clone https://github.com/Organizacion/CMI-DAC.git /opt/cmi-dac
```

### 3.2. Variables de Entorno (.env)

Crear el archivo `.env` en la raíz del proyecto con las credenciales de la base de datos gestionada:

```ini
DB_HOST=private-db-postgresql-nyc1-12345.do-user.db.digitalocean.com
DB_PORT=25060
DB_NAME=defaultdb
DB_USER=doadmin
DB_PASSWORD=xxxx_password_seguro_xxxx
# Ruta al certificado CA descargado
DB_SSL_ROOT_CERT=/opt/cmi-dac/certs/ca-certificate.crt
```

---

## 4. Proceso de Despliegue y Actualización

### 4.1. Carga Inicial de Datos

Ejecutar el pipeline de ETL manualmente para poblar la base de datos:

```bash
cd /opt/cmi-dac
source venv/bin/activate
pip install -r requirements.txt
python run_pipeline.py
```

### 4.2. Automatización (Cron)

Para mantener los datos actualizados, configurar una tarea programada (cronjob) que ejecute el pipeline cada noche:

```bash
# Editar crontab
crontab -e

# Añadir línea para ejecución diaria a las 05:00 AM
0 5 * * * cd /opt/cmi-dac && /opt/cmi-dac/venv/bin/python run_pipeline.py >> /var/log/cmi_etl.log 2>&1
```

---

## 5. Conexión con Power BI

1. **Obtener Connection String**: Desde el panel de Digital Ocean, copiar los datos de conexión (Connection details).
2. **Power BI Desktop**:
    * Origen: **Base de datos PostgreSQL**.
    * Servidor: `[host]:[puerto]`
    * Base de datos: `defaultdb`
3. **Certificado SSL**:
    * Es posible que Power BI requiera instalar el certificado CA de Digital Ocean en el almacén de certificados de confianza de Windows local si no se usa una CA pública.

## 6. Mantenimiento y Monitoreo

* **Logs**: Revisar `/var/log/cmi_etl.log` para verificar la ejecución correcta del ETL.
* **Backups**: Digital Ocean realiza copias de seguridad automáticas diarias (Point-in-Time Recovery) de la base de datos gestionada. No se requiere configuración adicional.
