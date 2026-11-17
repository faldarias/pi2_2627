# Ejercicios de la unidad 7

## Ejemplo 1. E-commerce

> **[Ejemplo 1. E-commerce]** Para su proyecto de e-commerce, diseñar un diagrama de la infraestructura en un proveedor cloud (AWS, Azure, Google Cloud) y un diagrama de red detallado con subredes, firewalls y balanceadores de carga.

### Solución sencilla: AWS

Se toma AWS como ejemplo. En la nube, el proveedor oculta los servidores y el cableado reales; por eso, el diagrama físico representa dónde se despliegan los servicios (región y zonas de disponibilidad), no el hardware concreto del centro de datos.

#### Diagrama físico (despliegue)

```text
                         INTERNET
                            |
                    [Internet Gateway]
                            |
                  [Balanceador de carga]
                    /                 \
       Zona de disponibilidad A   Zona de disponibilidad B
       [Servidor de aplicación]   [Servidor de aplicación]
                    \                 /
                  [Base de datos gestionada]
                     (red privada)
```

El balanceador y las dos instancias de aplicación reciben las peticiones de la tienda. La base de datos no se expone directamente a Internet.

#### Diagrama lógico (red y seguridad)

```text
Internet
   |
[Internet Gateway]
   |
VPC 10.0.0.0/16
   |
   +-- Subred pública A: 10.0.1.0/24 --+
   |                                    +-- [Balanceador HTTPS :443]
   +-- Subred pública B: 10.0.2.0/24 --+
                                            |
                              Firewall / grupo de seguridad:
                              permite HTTPS desde Internet
                                            |
                +---------------------------+---------------------------+
                |                                                       |
   Subred privada aplicación A:                         Subred privada aplicación B:
   10.0.11.0/24                                         10.0.12.0/24
   [Servidor aplicación :8080]                          [Servidor aplicación :8080]
                |                                                       |
                +---------------------------+---------------------------+
                                            |
                              Firewall / grupo de seguridad:
                              permite :8080 solo desde el balanceador
                                            |
                       Subredes privadas de base de datos
                       A: 10.0.21.0/24   B: 10.0.22.0/24
                       [Base de datos gestionada :3306]
                       Firewall: permite :3306 solo
                       desde los servidores de aplicación
```

Las subredes A y B pertenecen a zonas de disponibilidad distintas. Así, si una instancia de aplicación falla, el balanceador puede enviar las peticiones a la otra. La base de datos solo acepta conexiones desde la aplicación.

## Ejercicio 2. Red de un centro educativo

**Enunciado:** Un centro educativo tiene una zona de administración, aulas para el profesorado y el alumnado y una red Wi-Fi para visitantes. Diseñar los diagramas físico y lógico, separando las redes y evitando que los visitantes accedan a los equipos del centro.

### Solución: diagrama físico

```text
                         [Internet]
                             |
                      [Router/Firewall]
                             |
                      [Switch principal]
                    /         |          \
             [Servidor]   [Switch aula]   [Punto de acceso Wi-Fi]
                            /      \          /             \
                    [PC profes.] [PC alumnado] [Wi-Fi centro] [Wi-Fi visitas]
```

### Solución: diagrama lógico

```text
Internet
   |
[Router/Firewall]
   |
[Switch principal: VLAN 10, 20, 30 y 40]
   |
   +-- VLAN 10 Administración: 192.168.10.0/24
   +-- VLAN 20 Profesorado:    192.168.20.0/24
   +-- VLAN 30 Alumnado:       192.168.30.0/24
   +-- VLAN 40 Visitantes:     192.168.40.0/24
```

El router/firewall asigna la dirección `.1` como puerta de enlace de cada subred. Todas las redes pueden salir a Internet, pero la VLAN de visitantes no puede iniciar conexiones hacia las redes internas.

## Ejercicio 3. Web de una pequeña empresa

**Enunciado:** Una pequeña empresa tiene una web pública y una base de datos interna. Diseñar los diagramas físico y lógico para que los clientes puedan visitar la web, pero no acceder directamente a la base de datos.

### Solución: diagrama físico

```text
                         [Internet]
                             |
                      [Router/Firewall]
                             |
                       [Switch del rack]
                         /           \
                [Servidor web]   [Servidor de base de datos]
                    (DMZ)              (red interna)
```

### Solución: diagrama lógico

```text
Internet
   |
[Firewall]
   |-- DMZ: 172.16.10.0/24
   |      [Servidor web: 172.16.10.10]
   |
   +-- Red interna: 172.16.20.0/24
          [Base de datos: 172.16.20.10]
```

El firewall permite desde Internet únicamente HTTPS (puerto 443) hacia el servidor web. La base de datos no es accesible desde Internet y solo acepta conexiones desde el servidor web por el puerto necesario (por ejemplo, 3306).
