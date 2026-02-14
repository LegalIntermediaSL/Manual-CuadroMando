# Anexo V: Infraestructura de Seguridad Física (NAS y SAI)

La soberanía y protección del dato no se limita a "la nube". La sede central alberga un núcleo de seguridad físico que actúa como última línea de defensa ante catástrofes.

---

## 1. Servidor NAS: La "Caja Negra"

Contamos con un servidor de almacenamiento en red (Network Attached Storage) **Synology DiskStation** configurado no como un simple disco duro disco, sino como un **servidor de backup inteligente**.

### 1.1. Especificacciones y Capacidad

* **Modelo**: Synology DS224+ (o superior).
* **Almacenamiento**: Discos en **RAID 1 (Espejo)**. Esto significa que si un disco físico se rompe (falla mecánica), el otro sigue funcionando sin perder ni un solo byte de información.
* **Aislamiento**: Este dispositivo NO es accesible desde internet público. Solo "habla" con el exterior bajo demanda y encriptado.

### 1.2. Misión Crítica: Inmutabilidad

La función más importante de este NAS no es guardar datos, sino **protegerlos contra Ransomware**.

* Los archivos de backup se marcan con tecnología **WORM (Write Once, Read Many)**.
* *Significado*: Ni siquiera el administrador, con la contraseña más alta, puede borrar o modificar un backup de los últimos 30 días. Si un virus entra en la red y trata de "secuestrar" los archivos, se encontrará con un muro de solo lectura.

---

## 2. Protección Eléctrica (SAI)

El NAS, el router y el switch principal están conectados a un **SAI (Sistema de Alimentación Ininterrumpida)** de la marca **APC / Eaton**.

### ¿Qué hace este "ladrillo negro"?

1. **Batería de Respaldo**:
    * Si se corta la luz por una tormenta o una obra en la calle, el SAI mantiene los equipos encendidos durante 15-30 minutos.
    * Esto da tiempo suficiente para guardar cambios y, lo más importante, cerrar ordenadamente las bases de datos.

2. **Pararrayos Digital (AVR)**:
    * Regula el voltaje automáticamente. Si la electricidad llega con "ruido" o picos (muy común en zonas industrializadas), el SAI "limpia" la corriente antes de que toque los delicados discos duros del NAS.

### Protocolo de Apagado Automático

El SAI está conectado por USB al NAS.

* Cuando la batería baja del 20%, el SAI envía una señal al NAS: *"Me estoy apagando"*.
* El NAS inicia un script de **apagado seguro**, desmontando volúmenes de datos para evitar corrupciones.
* Cuando vuelve la luz, el sistema se reinicia solo y reanuda sus tareas.

---

## 3. Mantenimiento Básico para Usuario

Aunque estos sistemas son autónomos, requieren una vigilancia mínima:

* **Luz Verde/Azul Fija**: ✅ Todo OK.
* **Pitido Constante (Beep... Beep...)**: ⚠️ Corte de luz (funcionando en batería).
* **Pitido Continuo Agudo**: 🚨 Fallo de batería o sobrecarga. Avisar a IT inmediatamente.
* **Test**: Cada 6 meses, se recomienda desenchufar el SAI de la pared durante 2 minutos para verificar que las baterías siguen reteniendo carga.
