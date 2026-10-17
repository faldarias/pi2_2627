# UD3. Solución orientativa de la tarea de análisis de requisitos

**Módulo:** Proyecto Intermodular II (PI2)  
**Ciclo:** Administración de Sistemas Informáticos en Red (ASIR), 2.º curso  
**Tipo de actividad:** Material de apoyo para una tarea no evaluable.

---

## Consideraciones

Estas respuestas son orientativas. Puede haber otras soluciones válidas si son coherentes con el enunciado, distinguen los hechos de las hipótesis y proponen comprobaciones claras. En un proyecto real, las personas interesadas deben validar los requisitos y las decisiones pendientes.

El caso trata de mejorar la red de un aula con equipos de alumnado y profesorado, una impresora, una red administrativa y servicios internos. Se sabe que el alumnado no debe acceder a los recursos administrativos y que el profesorado necesita la impresora y una carpeta compartida. Aún faltan decisiones sobre equipos, servicios accesibles, permisos, presupuesto y disponibilidad.

## Solución de la actividad 1. Personas interesadas y aclaraciones

**Personas interesadas posibles:**

- **Alumnado:** necesita utilizar los ordenadores y los servicios autorizados durante las clases.
- **Profesorado:** necesita impartir las actividades, utilizar la impresora y acceder a los materiales compartidos.
- **Equipo de mantenimiento o administración de sistemas:** necesita administrar la infraestructura, diagnosticar incidencias y mantener la documentación.
- **Dirección del centro:** decide el alcance, las prioridades y los recursos disponibles.
- **Responsable de protección de datos o seguridad, si existe:** asesora sobre el acceso a información y las medidas de protección.

**Preguntas que conviene resolver:**

1. ¿Qué servicios internos necesita utilizar el alumnado y cuáles deben quedar restringidos?
2. ¿El profesorado y el alumnado deben tener permisos distintos para la impresora y la carpeta compartida?
3. ¿Qué equipos pueden reutilizarse y qué presupuesto o restricciones de compra existen?
4. ¿Qué horario de servicio y qué interrupción máxima son aceptables para las clases?
5. ¿Desde qué equipos o ubicaciones podrá administrarse la red y quién tendrá autorización?

No se conoce si el switch actual admite la configuración necesaria ni la matriz completa de comunicaciones. Tampoco se conoce el objetivo de disponibilidad ni el presupuesto; por tanto, no corresponde elegir todavía un modelo de equipo, fijar un porcentaje de disponibilidad o definir una arquitectura concreta.

## Solución de la actividad 2. Requisitos

| ID | Tipo | Requisito candidato | Comprobación |
|:---|:---|:---|:---|
| RF-01 | Funcional | El profesorado podrá imprimir desde el equipo autorizado del aula en la impresora de red. | Ejecutar una impresión de prueba desde el equipo acordado y registrar el resultado. |
| RF-02 | Funcional | El alumnado no podrá acceder a los recursos administrativos definidos como restringidos. | Probar el acceso desde un equipo de alumnado a cada recurso incluido en la lista aprobada; el acceso debe denegarse. |
| RNF-01 | No funcional, seguridad | El acceso de administración a los equipos de red estará limitado a las personas y equipos autorizados. | Revisar la configuración y comprobar que un origen autorizado puede administrar y uno no autorizado no. Falta acordar la lista de personas y equipos. |
| RNF-02 | No funcional, disponibilidad | La conectividad del aula deberá satisfacer el nivel de disponibilidad acordado para el horario lectivo. | Medir la disponibilidad durante el periodo de observación acordado y compararla con el objetivo aprobado. El umbral y el periodo están pendientes. |

La carpeta compartida y los servicios internos requieren aclarar primero qué usuarios necesitan acceso y con qué permisos. No se deben convertir supuestos en requisitos aprobados.

## Solución de la actividad 3. Historias de usuario y aceptación

**Historia 1:** Como docente, quiero imprimir desde el equipo del aula para disponer de copias de los materiales necesarios para la clase.

**Criterios de aceptación posibles:**

- Desde el equipo del profesorado autorizado se envía un documento de prueba y la impresora lo recibe.
- El resultado de la prueba queda registrado indicando equipo de origen, impresora, fecha y resultado.
- Un equipo de alumnado no obtiene acceso de administración a la impresora. El acceso a funciones ordinarias de impresión del alumnado queda pendiente de decisión porque el caso no especifica si debe permitirse.

**Historia 2:** Como responsable de sistemas, quiero restringir el acceso del alumnado a los recursos administrativos para proteger la información del centro.

**Comunicaciones basadas en el caso:** debe bloquearse el acceso de un equipo de alumnado a los recursos administrativos; debe permitirse el acceso del equipo del profesorado a la impresora. Para otros flujos, como el acceso del alumnado a Internet o a un servicio interno concreto, hace falta que el centro los confirme antes de definir la matriz de comunicaciones.

## Solución de la actividad 4. Preparación y finalización

**DoR posible para la historia de impresión:**

- identifica a la persona usuaria y el beneficio;
- especifica el equipo de origen y la impresora de destino;
- aclara si la impresión desde equipos del alumnado se permite o se bloquea;
- dispone de un método y un entorno de prueba;
- registra las dependencias, como la disponibilidad de la impresora y del equipo.

La historia no está completamente preparada mientras no se decida el acceso del alumnado y se confirme el entorno de prueba. El equipo puede avanzar en las partes ya claras, pero debe dejar visible esa cuestión pendiente.

**DoD posible para el equipo:**

- se cumplen los criterios de aceptación acordados;
- las pruebas se ejecutan y sus resultados quedan registrados;
- los cambios respetan las reglas de acceso aprobadas y se revisan;
- se actualizan los diagramas y procedimientos afectados.

La persona o grupo que representa al centro debe acordar los permisos y el alcance. Mantenimiento debe confirmar el entorno y los medios de prueba. La DoD es común al equipo; los criterios de aceptación concretan cada historia.

## Solución de la actividad 5. Estimación y priorización

Una estimación inicial posible sería:

| Historia | Talla orientativa | Motivo y cuestiones pendientes |
|:---|:---:|:---|
| A. Documentar topología y equipos | S | Puede ser acotada si existe acceso al aula y los equipos están identificados. Aclarar quién valida el diagrama y si hay que descubrir conexiones no documentadas. |
| B. Definir y probar la separación | L | Tiene valor de seguridad, pero depende de acordar la matriz de comunicaciones, conocer las capacidades de los equipos y preparar pruebas. Podría dividirse en análisis de flujos, diseño y validación. |
| C. Configurar supervisión | M | Requiere definir qué significa «conexión disponible», dónde se mide, quién recibe avisos y qué herramienta puede utilizarse. |

**Prioridad orientativa:** primero aclarar el alcance y documentar la topología (A), porque la información ayuda a tomar decisiones posteriores y puede tener pocas dependencias. Después, priorizar la definición de reglas y la separación (B) por su valor de seguridad, una vez resueltas las preguntas de alcance y compatibilidad. La supervisión (C) también aporta valor operativo y puede adelantarse si el centro necesita detectar cortes de forma inmediata. Un orden distinto es válido si se explicitan sus razones y dependencias.

**Pregunta para dividir B:** ¿podemos empezar identificando y aprobando los flujos necesarios entre el aula y los servicios internos antes de diseñar cómo bloquear los demás? Si esa tarea es demasiado amplia, se pueden separar los flujos por perfiles o servicios, manteniendo criterios de aceptación verificables para cada parte.

## Cierre

La clave del ejercicio no es coincidir exactamente con estas propuestas, sino justificar las decisiones, hacer visibles las dudas y no presentar como aprobado algo que todavía debe acordar el centro.
