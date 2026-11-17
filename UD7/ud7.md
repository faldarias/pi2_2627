---
title: "UD7. Infraestructura de red: Lógicos y Físicos"
subtitle: "Módulo: Proyecto Intermodular II. ASIR"
author: "Paco Aldarias"
date: "15 de noviembre de 2026"
lang: es
---

# Unidad 7: Infraestructura de red: Lógicos y Físicos

## Objetivos

* Aprender a visualizar y documentar la estructura técnica de una aplicación o sistema.
* Comprender la importancia y diferencias entre la infraestructura física y lógica de una red informática, y aprender a representar y diseñar ambos tipos mediante diagramas específicos para poder planificar, administrar y mantener redes de manera eficiente y segura en entornos profesionales como ASIR.

---

## 1. La importancia de la visualización

> *"Una imagen vale más que mil palabras"*. En el mundo de la tecnología, un buen diagrama vale más que mil líneas de código o documentación.

Los diagramas técnicos son herramientas esenciales para:

* **Comunicar:** Explicar diseños complejos a otros miembros del equipo, a los *stakeholders* o a futuros desarrolladores.
* **Planificar:** Diseñar la estructura de un sistema antes de empezar a construirlo.
* **Analizar:** Identificar posibles cuellos de botella, puntos de fallo o problemas de seguridad.
* **Documentar:** Dejar un registro claro de cómo está construido un sistema.

---

## 2. Introducción a la infraestructura de red

La **infraestructura de red** es el conjunto de componentes físicos y lógicos que permiten la comunicación y el intercambio de datos entre dispositivos dentro de una red informática.

* Es fundamental para el funcionamiento de cualquier sistema informático.
* Nos permite compartir recursos, acceder a servicios y conectarnos a internet.

### Diferencia clave

* **Infraestructura física:** Los elementos tangibles (hardware).
* **Infraestructura lógica:** La configuración y protocolos que permiten la comunicación.

---

## 3. Infraestructura física de red

La infraestructura física incluye todos los elementos materiales que conforman la red.

### Componentes

* **Cables:** UTP (par trenzado), fibra óptica, coaxial.
* **Dispositivos:** Switches, routers, puntos de acceso, servidores, estaciones de trabajo.
* **Otros:** Racks, paneles de parcheo, canalizaciones.

### Topologías físicas

* **Estrella:** Todos los dispositivos conectados a un punto central (switch).
* **Bus:** Todos los dispositivos conectados a un único cable.
* **Anillo:** Cada dispositivo conectado al siguiente formando un círculo.
* **Malla:** Dispositivos interconectados de forma redundante.

#### Ejemplos visuales de topologías

**Topología Estrella:**
```text
      [PC1]
        |
     [Switch]
      /    \
  [PC2]    [PC3]
```

**Topología Bus:**
```text
[PC1]---[PC2]---[PC3]---[PC4]
```

**Topología Anillo:**
```text
[PC1]---[PC2]
  |       |
[PC4]---[PC3]
```

**Topología Malla:**
* Cada nodo conectado a varios otros para redundancia.

### Importancia

* Una buena infraestructura física asegura la calidad y estabilidad de la red.
* Es importante planificar la ubicación de los dispositivos y el cableado para evitar interferencias y facilitar el mantenimiento.

---

## 4. Infraestructura lógica de red

La infraestructura lógica es el diseño virtual que permite que los dispositivos se comuniquen.

### Componentes

* **Protocolos:** Conjunto de reglas para la comunicación (TCP/IP, DHCP, DNS).
* **Direccionamiento IP:** Asignación de direcciones para identificar dispositivos.
* **Subredes:** División lógica para organizar y segmentar la red.
* **VLANs:** Redes virtuales para segmentar tráfico dentro de la misma infraestructura física.

### Topologías lógicas

* No necesariamente coinciden con la topología física.
* **Ejemplo:** Una VLAN puede agrupar dispositivos físicamente dispersos.

---

## 5. Diagramas de red

### ¿Para qué sirven los diagramas de red?

* Son representaciones visuales que muestran cómo está diseñada una red.
* Ayudan a entender, planificar, administrar y solucionar problemas.
* Facilitan la comunicación entre técnicos y clientes.

### Tipos de diagramas

#### Diagrama físico
Muestra la ubicación real de los dispositivos y el cableado.

```text
[Servidor1]---(UTP)---[Switch]---(Fibra)---[Router]---(ISP)
                         |
                       (UTP)
                         |
                       [PC1]
```

#### Diagrama lógico
Muestra cómo se comunican los dispositivos, incluyendo IPs, subredes y protocolos.

```text
[PC1 192.168.1.10 VLAN10] \
                           [Switch]---[Router 192.168.1.1]
[PC2 192.168.2.10 VLAN20] /
```

---

## 6. Diagramas físicos para ASIR

### Qué mostrar

* **Dispositivos:** Switches, routers, servidores, estaciones, puntos de acceso.
* Cableado y conexiones físicas.
* Ubicación física (salas, racks, pisos).
* Etiquetas de cables y puertos.

### Cómo representarlo

* Símbolos estándar para cada dispositivo.
* Líneas que representan los cables físicos.
* Notas o leyendas para aclarar tipos de cables (UTP, fibra, etc.).

### Ejemplo básico

```text
      [Servidor1]
           |
         (UTP)
           |
        [Switch]--------------------[Router]---(Internet)
         /    \
      (UTP)  (UTP)
       /        \
   [PC1]        [PC2]
```

### Importancia para ASIR

* Permite conocer dónde está cada componente.
* Facilita el mantenimiento físico y las ampliaciones.

---

## 7. Diagramas lógicos para ASIR

### Qué mostrar

* Direcciones IP asignadas a cada dispositivo.
* Subredes y máscaras de red.
* VLANs y su segmentación.
* Rutas y protocolos de comunicación.

### Cómo representarlo

* Representar dispositivos con sus nombres y direcciones IP.
* Indicar las VLANs y subredes con colores o etiquetas.
* Mostrar rutas entre subredes y conexiones lógicas.

### Ejemplo básico

```text
       VLAN10                             VLAN20
   192.168.1.0/24                     192.168.2.0/24
 [PC1 192.168.1.10]                 [PC2 192.168.2.10]
         |                                  |
         +------- VLAN 10 -- [Switch] -- VLAN 20 -------+
                                |
                             [Router]
                     192.168.1.1 / 192.168.2.1
```

* Aquí `PC1` y `PC2` están en VLANs distintas, aunque conectados al mismo switch.
* El router conecta ambas VLANs.

### Importancia para ASIR

* Facilita la gestión del direccionamiento IP.
* Ayuda a planificar la seguridad y el rendimiento.
* Fundamental para configurar correctamente dispositivos y servicios.

---

## 8. Diferencias clave entre diagramas físicos y lógicos

| Característica | Diagrama Físico | Diagrama Lógico |
| :--- | :--- | :--- |
| **¿Qué muestra?** | Ubicación real de equipos y cables | Comunicación entre dispositivos, IPs, VLANs |
| **Enfoque** | Hardware y conexiones tangibles | Configuración y flujo de datos |
| **Uso principal** | Instalación, mantenimiento físico | Administración, planificación de red |
| **Ejemplo** | Cable UTP, ubicación del switch | Subredes, rutas, VLANs |

### Cuándo usar cada uno

* **Diagrama físico:** Para instalación y reparación de cableado y equipos.
* **Diagrama lógico:** Para configuración, seguridad, segmentación y gestión de red.

---

## 9. Herramientas Comunes

* **Draw.io (ahora diagrams.net):** Gratuita, potente y se integra con herramientas como VS Code, Google Drive y GitHub. Es una opción excelente para todo tipo de diagramas.
* **Lucidchart:** Una herramienta online muy popular con muchas plantillas y funcionalidades colaborativas. Tiene una versión gratuita limitada.

---

## 10. Caso práctico básico (opcional)

Supongamos que tenemos una pequeña empresa con:
* Una sala de servidores con 2 servidores y un switch.
* Dos oficinas con PCs conectadas a través del switch.
* Un router para acceso a Internet.

### Diagrama físico
Muestra la ubicación de servidores, switch y cableado:

```text
[Servidor]---(UTP)---[Switch]---(UTP)---[PC1]
                        | \
                     (UTP) (Fibra)
                        |     \
                     [PC2]   [Router]---(Internet)
```

### Diagrama lógico
Muestra subredes para las oficinas, con VLANs que segmentan el tráfico y direcciones IP asignadas a cada PC y servidor:

* **VLAN10:** `192.168.1.0/24`
  * **Servidor:** `192.168.1.2`
  * **PC1:** `192.168.1.10`
* **VLAN20:** `192.168.2.0/24`
  * **PC2:** `192.168.2.10`
* **Router:** Conecta ambas VLANs para comunicación y acceso a internet.

## Ejercicios

Los enunciados y soluciones de los ejemplos están en el [fichero de ejercicios pdf](ud7-ejercicios.pdf).

---

## 11. Conclusión

* La infraestructura de red consta de dos partes: **física** y **lógica**, ambas indispensables.
* Los diagramas físicos y lógicos son herramientas clave para planificar, administrar y mantener redes.
* En **ASIR** es fundamental dominar ambas para poder diseñar, instalar y gestionar redes eficientes y seguras.

[Volver al índice principal](../index.html)

