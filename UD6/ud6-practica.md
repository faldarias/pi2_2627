---
title: "Prácticas sencillas de IA para proyectos ASIR"
subtitle: "Módulo PI2 · ASIR2. Unidad 6 · Actividades para compartir en el foro"
author: "Paco Aldarias"
date: "7 de noviembre de 2026"
lang: es
---

# Prácticas sencillas de IA para proyectos ASIR

Estas actividades sirven para explorar usos prácticos de la inteligencia artificial en un proyecto de infraestructura ASIR. Elige **una actividad** relacionada con tu proyecto, o la que indique el profesorado, y comparte el resultado en el **foro de la UD6** para que el resto de la clase pueda comentarlo y aprender de las experiencias de los demás.

## Antes de empezar

- Utiliza un laboratorio, una máquina virtual o datos inventados; no hagas pruebas en sistemas de producción.
- No introduzcas contraseñas, tokens, claves, datos personales ni información interna del centro o de una empresa en una IA.
- Revisa las respuestas y los comandos antes de usarlos. Comprueba los datos técnicos con documentación fiable.
- Indica qué herramienta de IA utilizaste y qué parte del trabajo revisaste o corregiste.
- Sigue las instrucciones del módulo y las normas de convivencia del foro.

## Actividad 1. Comparar IA en la nube y local

**Objetivo:** elegir una herramienta apropiada para ayudar a documentar el proyecto.

1. Elige una tarea sencilla y no confidencial, por ejemplo, preparar un inventario ficticio de máquinas virtuales.
2. Compara una herramienta en la nube, como ChatGPT o Gemini, con un modelo local ejecutado mediante Ollama o LM Studio. 
3. Compara conexión a Internet, requisitos del equipo, privacidad, facilidad de uso y limitaciones.
4. Explica cuál elegirías para esa tarea y por qué.

PD: No necesitas instalar los modelos locales, sólo 
debes usar la IA para comparar las IAs.

**Para compartir:** una tabla comparativa y una conclusión breve.

## Actividad 2. Resumir documentación técnica

**Objetivo:** usar IA para estudiar sin sustituir la fuente original.

1. Escoge una página pública de documentación sobre DNS, DHCP, Linux, Windows Server, copias de seguridad u otro tema de ASIR.
2. Pide a una IA que resuma un apartado o que formule cinco preguntas de repaso.
3. Comprueba cada respuesta consultando la documentación original.
4. Corrige cualquier error y anota el enlace y el apartado consultado.

**Para compartir:** el resumen o las preguntas revisadas, la fuente original y un ejemplo de corrección o comprobación.

## Actividad 3. Revisar una propuesta de red

**Objetivo:** emplear IA para obtener una propuesta inicial y practicar su validación.

1. Describe una red ficticia para una pequeña organización: usuarios, servidores, DNS y DHCP.
2. Pide a una IA una propuesta de subredes y de distribución de servicios.
3. Revisa que las direcciones y máscaras sean coherentes y que las subredes no se solapen.
4. Dibuja la propuesta final e indica qué cambiaste tras revisarla.

**Para compartir:** el diagrama o esquema final y dos decisiones técnicas justificadas. Usa direcciones reservadas para documentación, como `192.0.2.0/24`, `198.51.100.0/24` o `203.0.113.0/24`; no publiques el direccionamiento real de una organización.

## Actividad 4. Crear un pequeño script de comprobación

**Objetivo:** aprender a revisar código generado por IA antes de ejecutarlo.

1. Pide a una IA un script de Bash o PowerShell que compruebe la resolución DNS de un nombre de ejemplo.
2. Solicita una explicación de cada parte y que el script no cambie la configuración ni elimine archivos.
3. Revisa el código; ejecútalo solo en tu equipo de pruebas o máquina virtual.
4. Comprueba qué ocurre cuando la resolución funciona y cuando el nombre no existe.

**Para compartir:** el script revisado, su explicación y los resultados de las pruebas. No publiques registros que puedan revelar nombres internos, direcciones reales o información sensible.

## Actividad 5. Analizar una incidencia ficticia

**Objetivo:** usar IA para ordenar hipótesis, no para aceptar automáticamente un diagnóstico.

1. Inventa un mensaje de error sobre DNS o DHCP; no copies registros reales.
2. Pide a una IA tres causas posibles y una comprobación segura para cada una.
3. Contrasta las comprobaciones con la documentación del servicio.
4. Señala qué pruebas permitirían confirmar o descartar cada hipótesis.

**Para compartir:** una tabla con el error ficticio, las hipótesis, las comprobaciones y la conclusión. Deja claro qué sugerencias de la IA no se confirmaron.

## Actividad 6. Preparar una sección del README con IA

**Objetivo:** documentar una parte pequeña del proyecto y declarar el apoyo recibido.

1. Pide a una IA un borrador de instrucciones para iniciar o probar un servicio del laboratorio.
2. Comprueba versiones, comandos, requisitos y enlaces; corrige el borrador según tu proyecto.
3. Añade una declaración breve: herramienta utilizada, para qué y cómo verificaste el resultado.
4. Revisa el cambio con Git y comprueba que no hay secretos ni archivos privados antes de compartirlo.

**Para compartir:** el fragmento de README corregido y la declaración de uso de IA.

## Publicación en el foro de la UD6

Publica **una entrada por actividad** con este formato:

1. **Título:** nombre de la actividad y tema de tu proyecto.
2. **Objetivo:** qué querías resolver o aprender.
3. **Herramienta:** nombre de la IA utilizada y, si lo conoces, el modelo.
4. **Resultado:** tabla, resumen, diagrama, script o análisis; incluye una imagen solo si ayuda a entenderlo.
5. **Comprobaciones:** qué contrastaste, qué corregiste y qué resultado obtuviste.
6. **Conclusión:** qué fue útil, qué limitaciones encontraste y qué harías distinto.
7. **Fuentes:** enlaces a la documentación técnica consultada.

No es necesario publicar la conversación completa con la IA ni el prompt si contiene información privada. Responde al menos a una publicación de un compañero con una pregunta, sugerencia o comprobación constructiva, según indique el profesorado.

## Criterios de revisión

- El ejercicio se entiende y está relacionado con un proyecto ASIR.
- Se explica el uso de IA y se identifican sus límites.
- El resultado se revisó con pruebas o fuentes adecuadas.
- La publicación es clara, respetuosa y no revela información sensible.

[Descargar esta práctica en PDF](ud6-practica.pdf)

