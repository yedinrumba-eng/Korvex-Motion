---
description: Yeyow aprueba una puerta de korvex-motion (brief, guion o video) y se sigue al siguiente rol
argument-hint: brief|guion|video [CLIENTE/videos/NN-nombre] [notas]
---
Yeyow acaba de aprobar con este comando: `$ARGUMENTS`

1. Identifica la puerta (`brief` = PUERTA 1 → `02-brief.md`; `guion` = PUERTA 2 → `03-guion.md`; `video` = PUERTA 4 → `05-revision.md`) y el video. Si no se indica la carpeta, usa el video en curso de esta sesión. Si hay duda, pregunta cuál.
2. Escribe en ese archivo SOLO lo que Yeyow aprobó:
   - `02-brief.md` / `03-guion.md`: `aprobado: true`, `aprobado_por: Yeyow`, `fecha_aprobacion: <hoy>`. En "Decisiones de Yeyow", su texto tal cual (incluye las notas del comando, si las hay).
   - `05-revision.md`: `veredicto_yeyow: APROBADO`, `fecha: <hoy>`, y sus notas en "Tus notas".
3. Si las notas traen cambios ("apruebo pero cambia X"), no es una aprobación limpia. Aplica primero el cambio, muéstralo y pide la confirmación.
4. Sigue el flujo del skill `korvex-motion`:
   - brief → Guionista;
   - guion → Editor;
   - video → render final + entrega.
