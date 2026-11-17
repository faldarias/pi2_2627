# Guía de Cisco Packet Tracer

## 1. ¿Qué es Packet Tracer?

Cisco Packet Tracer es un simulador de redes. Para poder compartir y abrir correctamente los archivos de prácticas, es importante utilizar la misma versión.

## 2. Descarga

Cisco Packet Tracer se puede descargar gratuitamente desde Cisco Networking Academy. Inicia sesión en NetAcad y accede a **NetAcad Legacy > Resources > Packet Tracer**.

[Página de descarga de Packet Tracer](https://legacy.netacad.com/portal/resources/packet-tracer)

## 3. Instalación en Ubuntu

Estas instrucciones corresponden a Ubuntu 24.04.2 LTS.

1. Descarga el instalador .deb desde la [página de Packet Tracer](https://legacy.netacad.com/portal/resources/packet-tracer).
2. Descarga la biblioteca `libgl1-mesa-glx_23.0.4-0ubuntu1.22.04.1_amd64.deb`. [Referencia sobre la biblioteca](https://www.reddit.com/r/Ubuntu/comments/1e3nlar/missing_libgl1mesaglx_when_installing_packet/?tl=es-es).
3. Instala la biblioteca desde la terminal:

   ```bash
   sudo dpkg -i libgl1-mesa-glx_23.0.4-0ubuntu1.22.04.1_amd64.deb
   ```

4. Instala Packet Tracer:

   ```bash
   sudo dpkg -i Packet_Tracerxxx.deb
   ```

5. Si quedan dependencias pendientes, ejecútalo desde la terminal:

   ```bash
   sudo apt --fix-broken install
   ```

## 4. Acceso a las líneas de comandos

- **PC:** abre **PC > Desktop > Command Prompt > Run**.
- **Router:** abre **Router > CLI**.

### Comandos para PC

| Acción | Comando |
|---|---|
| Consultar la configuración IP | `ipconfig` |
| Consultar la tabla de rutas | `route` |
| Consultar la ruta hasta un destino | `traceroute` |

### Comandos para router

| Acción | Comando |
|---|---|
| Consultar las interfaces y sus direcciones IP | `show ip interface brief` |
| Consultar las interfaces (forma abreviada) | `sh ip int bri` |
| Consultar la tabla de rutas | `show ip route` |
| Consultar la configuración actual | `show running-config` |
| Consultar la configuración actual (forma abreviada) | `sh run` |
| Consultar las listas de control de acceso (ACL) | `show access-lists` |
| Entrar en el modo privilegiado | `enable` |
| Entrar en el modo de configuración global | `configure terminal` |
| Entrar en una interfaz | `interface <id-int>` |
| Eliminar una lista ACL | `no ip access-list <numero>` |

## 5. Problemas de validación al abrir archivos

Al abrir un archivo de Packet Tracer, puede aparecer una solicitud de validación. En algunos casos, aunque el inicio de sesión parezca completarse, la aplicación sigue solicitándolo cada vez que se vuelve a abrir el archivo.

La solución indicada es iniciar sesión desde la nueva plataforma de NetAcad, en lugar de hacerlo desde NetAcad Legacy.


## 6. Curso básico

NetAcad ofrece un curso básico gratuito de Packet Tracer de aproximadamente dos horas, con opción de descargar el programa:

[Curso básico de Cisco Packet Tracer](https://www.netacad.com/es/courses/getting-started-cisco-packet-tracer?courseLang=es-XL)

Fuente adicional: [programas para simular redes](https://www.redeszone.net/tutoriales/redes-cable/programas-simular-red/).
