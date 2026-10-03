# Investigación de repos para el estudio de motion (02/10/2026)

Pedido de Yeyow: buscar skills, herramientas y componentes que le sumen variedad al estudio, y proponer un flujo spec-driven con roles para el contenido. Un agente revisó los repos en un scratch: no instaló nada ni tocó el estudio.

## Recomendaciones por prioridad
| # | Qué | Esfuerzo | Impacto |
|---|---|---|---|
| 1 | Flujo spec-driven con 5 documentos por video (`01-research` → `02-brief` → `03-guion` → `04-build` → `05-revision`), 3 puertas humanas y 1 automática | M | Alto |
| 2 | `_studio/tools/qa.py` ("oráculo") | M | Alto |
| 3 | Subir el nivel del kit de movimiento (ver abajo) | M | Alto |
| 4 | Recetario de briefs en español: plantilla `<inputs>/<direction>/<structure>/<build>/<gotchas>/<start>` | S | Alto |
| 5 | `render.py --draft` (540×960, sub 1), sub-cuadros adaptativos y promedio en luz lineal | S | Medio-Alto |
| 6 | Modo híbrido: research, brief y guion en Cowork; build y render en Claude Code del PC | S | Alto |
| 7 | Evaluar HyperFrames (Apache-2.0) en un sandbox, solo para tomarle la capa de documentos, el review loop y el pitch round | S | Medio |
| 8 | Audio: grilla de beats, SFX colocados por su pico medido y master a -14 LUFS / -1 dBTP | S | Medio |

**Detalle de la #2, `qa.py`:**
- Hoja de contactos con un cuadro por beat y otro a mitad de cada transición.
- Detecta saltos de un solo cuadro.
- Mide el % de cuadros quietos y que las duraciones de las tomas varíen (CV ≥ 0.25).
- Revisa LUFS/dBTP, la zona segura de IG, el tamaño (≤ 20 MB) y la duración.

**Detalle de la #3, kit de movimiento:**
- Springs que se suman por cada cambio de objetivo.
- Bordes elásticos con dos springs.
- Cursor con clic, arrastre y tecleo.
- Morph de contenedor.
- Zoom en espacio logarítmico, iris y flood.
- Scramble con semilla.
- Liquid glass (`feDisplacementMap`).

**Lo que no se adopta:**
- Remotion: obliga a reescribir en React y su licencia es de pago con más de 3 empleados.
- Código de onetake: la licencia es no comercial.
- Graphite como motor: está en alfa y su CLI solo exporta SVG/PNG/GIF.
- After Effects MCP: requiere AE, que es de pago.
- vox-director: depende de una API de pago.

## awesome-opus5-5-videos (yihui-dev) — MIT
La compilación es MIT, pero cada prompt y cada video es de su creador: se usan como inspiración, no se republican.
- **Qué trae:** 475 videos con su prompt (`prompts/*.md`, `data/videos.json`).
- **Categorías:** motion 288, interactive 70, explainer 62, 3d 55.
- **Tecnologías:** canvas 336, svg 193, threejs 141, shader 100, gsap 81.
- **Relación con nuestro estudio:** la mitad usa exactamente nuestro motor: `window.seek(t)` + Playwright con sub-cuadros + ffmpeg + grilla de beats.

**Formatos que sirven:**
- Launch con la UI real (es el formato de Korvin).
- "Una forma, nunca se corta": morph de UI a 120 BPM.
- Keynote de una sola toma con fotos reales + liquid glass.
- Tipografía cinética / bumper de marca.
- Explainer en 5 escenas: problema → qué hago → 3 pasos → prueba → nombre.
- **Receta paso a paso** (vaso vacío → coctel): le calza a un catering.
- Video al beat / lyric.
- Zoom infinito.

**Plantillas de prompt:**
- Bloques XML, donde `<start>` pide el storyboard en la grilla de beats ANTES del código. Es una puerta de aprobación.
- El brief largo de director.
- El estratega en 10 fases.
- Varios agentes con un juez que evalúa una sola vez.
- Variables `{{PRODUCT}}`/`{{COLOR_*}}`, que mapean a `perfil.md` + `marca.js`.

**Técnicas:**
- Todo es `f(t)`.
- Springs cerradas que se suman.
- Un cursor que causa cada cambio.
- Morph de contenedor.
- Transiciones que nacen de la escena anterior: match cut, zoom-through, iris, flood.
- Spring por glifo, scramble con semilla y misregistration en los cuadros de impacto.
- Footage como JPEG cambiado en cada seek (ya lo hacemos con `B.clip`).

**Gotchas:**
- No uses `will-change` en algo que la cámara escala.
- No pongas `opacity`/`filter` en `preserve-3d`.
- `backdrop-filter:url()` falla en Chromium: clona la escena.
- Un hijo con `visibility:visible` se ve a través de un padre oculto.
- En un loop, el último cuadro debe ser igual al primero.

**Prohibidos que se repiten:** partículas/confeti, anillos de onda, lens flares, temblor de cámara, neón, rebote exagerado, glassmorphism por todos lados, clichés de IA.

## HyperFrames (heygen-com/hyperframes) — Apache-2.0
- **Qué es:** el estudio más parecido al nuestro: HTML + GSAP en pausa, Puppeteer y FFmpeg.
- **Documentos:** `BRIEF.md`, `STORYBOARD.md` (status outline → built → animated) y `frame.md` (sistema de diseño para cámara).
- **Review loop:** plan → bocetos estáticos → construir → "¿render o cambios?".
- **Pitch round:** 5 conceptos, al menos 2 atípicos.
- **Recipe freeze:** un video aprobado se vuelve plantilla de la serie.
- **Ojo:** el cloud render, el publish y la generación usan servicios de HeyGen. No se usan.

## onetake (feitangyuan) — PolyForm Noncommercial
No se usa el código en trabajo comercial; las ideas sí, reimplementadas.
- **Idea central:** "cada beat se carga al siguiente": una sola toma, no un slideshow.
- **Método:**
  1. Deconstruir una referencia en números (% quieto, cortes, curvas).
  2. Proponer 3 conceptos.
  3. Beat sheet con la columna "qué se carga al siguiente".
  4. Oráculo `verify_promo.py`: cadencia, quietud ≥ 25 %, carry ≥ 0.5, picos y encuadre.
- **Sonido:** master a -16 LUFS.

## mojs — MIT
- **Qué aporta:** bursts, shapes y swirls declarativos.
- **Determinismo:** con `Timeline.setProgress(p)` es determinista, pero `rand()` usa `Math.random` al construir. Hay que sembrar `Math.random` antes, o los workers dan bursts distintos.
- **Veredicto:** opcional, solo para un momento de celebración.

## Graphite — MIT/Apache-2.0
- Editor 2D procedural en Rust, todavía en alfa.
- `graphene-cli` exporta SVG/PNG/GIF y necesita GPU.
- **Veredicto:** sirve para diseñar assets SVG a mano, no como motor.

## Otros del topic motion-graphics
- **video-shotcraft** (Apache-2.0): 152 fichas de toma, útiles como vocabulario.
- **iart-ai/motion-skills** (MIT): 54 skills de referencia (ads, tipografía cinética).
- **motion-anything** (Apache-2.0): recetas con `avoid_when`.
- **dotlottie-web / lottie-web** (MIT): íconos Lottie posicionables con `setFrame`.
- **Motion Canvas, Revideo y Manim** (MIT): solo para explainers largos o de matemáticas.
- **Theatre.js:** el core es Apache-2.0 y el studio es AGPL.
- **Remotion:** licencia propia.
- **No van:** friction y commotion (GPL), cut-director (AGPL), after-effects-mcp (necesita AE).

## Flujo spec-driven propuesto
```
Investigador ─► 01-research.md
Productor ────► 02-brief.md            ══ PUERTA 1 (Yeyow): concepto + brief
Guionista ────► 03-guion.md + bocetos  ══ PUERTA 2 (Yeyow): guion + storyboard
Editor ───────► index.html, music.py, borrador.mp4, 04-build.md
                └─ qa.py + juez (subagente aparte, máx. 2 vueltas)  ══ PUERTA 3 (automática)
Yeyow ────────► 05-revision.md         ══ PUERTA 4 (Yeyow): aprueba → render final → entregas/
```

**Qué lleva cada documento:**
- **`01-research.md`:**
  - Hechos con fuente.
  - Lo que NO se dice.
  - Audiencia y dolor.
  - Flujo real del producto.
  - 2–3 referencias medidas.
  - El antipatrón de la categoría.
  - Assets con su licencia.
  - Música.
  - Riesgos.
- **`02-brief.md`:**
  - El frontmatter lleva `mensaje` (una frase), audiencia, duración, tono, CTA y `aprobado: false`.
  - Pitch de 3–5 conceptos.
  - Must-haves y prohibidos.
  - Afirmaciones permitidas, cada una con su fuente.
  - Criterios medibles:
    - gancho legible a 1.5 s;
    - producto antes de los 5 s;
    - CTA de al menos 2 s;
    - ≤ 20 MB;
    - -14 LUFS;
    - zona segura de IG;
    - tiempos de lectura.
- **`03-guion.md`:**
  - Guion con el tiempo de lectura de cada línea.
  - Beat sheet: t · compás · qué se ve · qué se lee · qué se mueve / qué queda quieto · qué se carga a la siguiente escena · SFX · cámara.
  - Golpes fijados a la música.
  - Poster.
  - Copy para redes.
  - Bocetos en `storyboard.html` → `qa/bocetos.png`.
- **`04-build.md`:** desviaciones del guion, comandos para reproducir, QA y veredicto del juez.
- **`05-revision.md`:** notas por timestamp y la decisión (APROBADO / CAMBIOS / DESCARTADO).

**En Claude Code:**
- Agentes en `.claude/agents/`: investigador, productor, guionista, editor y juez-qa.
- Comandos: `/video`, `/aprobar` y `/cambios`.
- Un hook `gate_check.py` que bloquea el build si falta `aprobado:`.

**En Cowork:** una skill `motion-pipeline` con roles y plantillas. Las aprobaciones se dan en el chat y se reflejan en el Project.

## Claude Code (PC) vs Cowork
- **Render:** en Cowork se midieron 605–738 s por reel de 20–22 s con 2 núcleos. En el PC se estiman 2–3 min usando todos los núcleos y la GPU para WebGL.
- **Archivos:** Cowork pasa los archivos al PC por un puente de 20 MB por archivo. A cambio da Projects, memoria, Artifacts con comentarios y aprobación desde el teléfono.
- **Recomendación:** híbrido.
  - Los roles 1–3 en Cowork.
  - El build y el render final en Claude Code.
  - El render final siempre en la misma máquina: Windows y Linux no dan los mismos píxeles.

## Bug encontrado y corregido
`K.spring` devolvía NaN con ζ ≥ 1. Desde el 02/10/2026 tiene ramas para el caso crítico y el sobreamortiguado.
