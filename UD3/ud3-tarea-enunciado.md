# UD3. Tarea de análisis de requisitos para un proyecto ASIR

**Módulo:** Proyecto Intermodular II (PI2)  
**Ciclo:** Administración de Sistemas Informáticos en Red (ASIR), 2.º curso  
**Tipo de actividad:** No evaluable. Actividad de práctica y autoaprendizaje.  
**Tiempo orientativo:** 60-90 minutos  
**Entrega:** No se entrega ni tiene calificación.

---

## 1. Situación de partida

Un centro educativo quiere mejorar la infraestructura de red de una de sus aulas de informática. En el aula hay 24 ordenadores de alumnado, un equipo para el profesorado y una impresora de red. El centro también dispone de una red administrativa y de varios servicios internos. La conexión a Internet debe seguir funcionando durante las clases.

La dirección pide que los equipos del alumnado no puedan acceder a los recursos administrativos. El profesorado necesita acceder a la impresora y a una carpeta compartida con materiales de clase. El equipo de mantenimiento quiere poder administrar los equipos de red y comprobar si la conexión está disponible. Todavía no se ha decidido si se reutilizará el switch actual, qué servicios internos estarán accesibles desde el aula ni qué nivel de disponibilidad se considera suficiente.

El equipo de proyecto debe analizar las necesidades antes de elegir equipos, tecnologías o configuraciones. No se deben dar por aprobadas decisiones que el centro aún no ha tomado.

## 2. Objetivos de la práctica

Al terminar la actividad, deberías poder:

- distinguir requisitos funcionales y no funcionales;
- identificar personas interesadas y preguntas pendientes;
- redactar historias de usuario con criterios de aceptación comprobables;
- detectar si una historia está preparada para planificarse y proponer una definición de terminado;
- estimar trabajo de manera relativa y priorizarlo teniendo en cuenta valor, esfuerzo, riesgo y dependencias.

## 3. Actividades

### Actividad 1. Personas interesadas y aclaraciones

1. Identifica al menos cuatro personas o grupos interesados en el proyecto y explica qué necesitan o qué responsabilidad tienen.
2. Redacta cinco preguntas que el equipo debería plantear antes de cerrar el alcance. Incluye, al menos, una pregunta sobre seguridad, una sobre disponibilidad y una sobre las restricciones técnicas o económicas.
3. Indica dos decisiones que todavía no se pueden tomar con la información disponible y explica por qué.

### Actividad 2. Requisitos

Redacta cuatro requisitos candidatos para el proyecto:

- dos funcionales;
- dos no funcionales.

Para cada uno, indica un identificador, su tipo y una forma de comprobarlo. Si faltan datos para definir un umbral medible, anótalo como pregunta o decisión pendiente en lugar de inventarlo.

### Actividad 3. Historias de usuario y aceptación

Redacta dos historias con el formato:

> Como `<tipo de usuario>`, quiero `<capacidad>` para `<beneficio>`.

Para una de ellas, escribe al menos tres criterios de aceptación que se puedan verificar mediante pruebas o revisión de evidencias. Añade un ejemplo de comunicación que debería permitirse y otro que debería bloquearse, basándote solo en lo que dice el caso.

### Actividad 4. Preparación y finalización

1. Elige una de tus historias y comprueba si está preparada para planificarse usando una lista breve de condiciones de Definition of Ready (DoR).
2. Propón una Definition of Done (DoD) común al equipo con cuatro condiciones aplicables al proyecto.
3. Si no puedes verificar una historia por falta de información, señala qué dato falta y quién debería acordarlo.

### Actividad 5. Estimación y priorización

Considera estas tres historias candidatas:

- **A.** Documentar la topología actual del aula y los equipos identificados.
- **B.** Definir y probar la separación entre la red del alumnado y la red administrativa.
- **C.** Configurar la supervisión para que mantenimiento pueda detectar una interrupción de la conexión.

1. Asigna una talla relativa (XS, S, M, L o XL) a cada historia y justifica brevemente las diferencias. Las tallas no representan horas.
2. Indica qué información o dependencias habría que aclarar antes de estimar con más precisión.
3. Ordénalas por prioridad y explica el criterio utilizado. No hay un único orden correcto: justifica cómo has considerado valor, seguridad, esfuerzo, dependencias e incertidumbre.
4. Elige una historia y escribe una pregunta que ayudaría a dividirla si resultara demasiado grande o incierta.

## 4. Autoevaluación

Al terminar, comprueba si tus respuestas:

- separan lo que el caso afirma de lo que todavía hay que preguntar;
- incluyen requisitos comprobables sin inventar objetivos numéricos;
- describen historias desde la perspectiva de quien obtiene el beneficio;
- proponen criterios de aceptación observables;
- distinguen DoR, DoD y criterios de aceptación;
- justifican estimaciones y prioridades en lugar de tratar las tallas o los votos como medidas exactas.

Esta tarea es un recurso de práctica no evaluable: no requiere entrega y no se utiliza para calificar el módulo.
