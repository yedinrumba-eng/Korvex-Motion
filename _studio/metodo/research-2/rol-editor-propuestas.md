# Propuestas para el rol Editor — research en marketplaces (03/10/2026)

Pedido: revisar marketplaces de skills/plugins para subir el nivel de `rol-editor.md` y `agents/editor.md`. Solo propuestas; no se tocó nada; no se repiten las fuentes del 02/10. Lo nuevo más fuerte: HyperFrames tiene una **segunda capa de skills** en `.claude/skills/` (doctrina de costuras) y 48 recetas con nuestro mismo contrato determinista.

## 1. Skills revisadas

| Skill | Repo / marketplace | Lic. | Qué hace | Veredicto |
|---|---|---|---|---|
| `motion-doctrine`, `cut-the-curve`, `seam-craft`, `oversized-cursor` | [hyperframes `.claude/skills/`](https://github.com/heygen-com/hyperframes/tree/main/.claude/skills) (commit 9123628) | Apache-2.0 | Ley del vector, signo Z, libro de costuras, puerta numérica, sin wobble, 5 rutas de movimiento sostenido | **Adoptar** (lo más útil) |
| `hyperframes-animation/rules/*` | [hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes-animation) | Apache-2.0 | 48 recetas seek-safe (`kinetic-beat-slam`, `chromatic-glitch`, `nudge-curve`); contrato sin relativos ni `Math.random` | **Adoptar como catálogo** del kit |
| `gsap-core/timeline/utils/plugins` | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) (oficial) | MIT | Stagger objeto, `distribute`, `CustomEase`, labels, `interpolate`, SplitText `mask` | **Adoptar 6 detalles** |
| `animate`, `review-animations` | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT | Nunca `scale(0)`, blur ≤2 px para fundir, revisión Antes/Después/Por qué | **Parcial** (lo de UI no aplica) |
| `motion-design` | [lottiefiles/motion-design-skill](https://github.com/lottiefiles/motion-design-skill) (oficial) | MIT | Personalidad de movimiento por marca, contra-movimiento, profundidad por velocidad | **Adoptar** (kit del cliente) |
| `frontend-design` | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design) | Apache-2.0 | "Tells" de diseño generado; audacia en un solo lugar | **Adoptar** en autorrevisión |
| `remotion-best-practices` | [remotion-dev/skills](https://github.com/remotion-dev/skills) | sin LICENSE | `fitText`, `posterize`, obturador 180°/8 muestras | **Solo 2 ideas** |
| `motion-designer` (+ `sound-effects`, `audio-design`) | [ncklrs/startup-os-skills](https://github.com/ncklrs/startup-os-skills) · copia en [editor-pro-max](https://github.com/hainrixz/editor-pro-max) | MIT | SFX en 3 alturas, riser→impacto→cola | **Parcial** (cifras sin fuente) |
| `sound-design-film` | [clawfu-skills](https://github.com/guia-matthieu/clawfu-skills) | MIT | Murch: jerarquía y "ley de dos y medio" | **Adoptar la regla** |
| `testing-visual-regression` | [claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) | MIT | Capturas contra baseline con umbral | **Adoptar la idea** |
| `video-motion-graphics` | [dylantarre/animation-principles](https://github.com/dylantarre/animation-principles) | MIT | Anticipación 2–4 cuadros, follow-through 4–8 | **Adoptar 2 reglas** |
| `emilkowalski-motion`, `gsap-*`, `chat-motion-overlay` | [nexu-io/open-design](https://github.com/nexu-io/open-design) | Apache-2.0 | Copias o plantillas Remotion | **Descartar**; ir al upstream |
| `interaction-design` · `ffmpeg-clip-team`, `game-audio` · `12-motion-design` · VoltAgent, ComposioHQ, travisvn, hesreallyhim | [wshobson/agents](https://github.com/wshobson/agents) · [claude-code-templates](https://github.com/davila7/claude-code-templates) · [claude-skills-fv](https://github.com/felvieira/claude-skills-fv) · clonados | MIT / Apache | UI web, prompts genéricos, `loudnorm`; los últimos cuatro sin nada de motion (grep) | **Descartar** / nada |

## 2. Mejoras concretas al rol de hoy

### 2.1 Ley del vector y libro de costuras
**Brecha:** § 4 "Transiciones con motivo" pide una dirección y velocity-matched, pero no fija eje, signo en Z, viaje parcial ni blur; `04-build.md` no registra las costuras.
**Texto (§ 4, sustituye "Transiciones con motivo"):**
```
- **Costuras.** Cómo sale A dice cómo entra B: mismo eje, misma dirección, misma velocidad, corte con las dos a mitad de movimiento. En Z la dirección es el signo del scale: si A se encoge, B llega grande (1,25→1); si A crece, B llega chica (0,75→1). Error típico: salir encogiendo y entrar creciendo desde chico.
- Viaje parcial ≈12 % del cuadro (≈130 px horizontal, ≈230 px vertical). Salida `power4.in` 0,2–0,34 s; entrada `power4.out` ≥ la salida, misma distancia. La opacidad de salida termina 0,02 s antes del corte; la de entrada arranca en ≈0,35. Blur pico: 10 px texto, 18–20 px superficie. `#stage` opaco (si no, flash blanco).
- Una "corriente" por video. Los demás vectores se gastan con sentido: arriba = conclusión; Z adelante = profundizar; Z atrás = llega algo más grande. Cambiar de dirección pide causa (clic, golpe).
- Tabla "Costuras" en 04-build.md: t · sale (eje, signo, id) · entra · técnica. Si una fila no cuadra, se arregla el plan, no el ease.
```
**Fuente:** hyperframes `motion-doctrine`, `cut-the-curve` §3–5, `seam-craft`.

### 2.2 Fase quieta con oficio
**Brecha:** § 4 permite "UN movimiento ambiental" y "respirar un glow"; HyperFrames lo prohíbe como relleno ("se ve que el video espera").
**Texto (§ 4, bajo "Build / breathe / resolve"):**
```
- **Lo quieto no es relleno.** Si la fase media dura >1,5 s, nómbrale una ruta: revelación por etapas, cámara con intención (general → viaja → llega), UI que vive (progreso, resaltado, conteo), secuencia (algo se archiva) o cursor que lleva el ojo. El glow solo como capa encima.
- Pausa dramática 0,3–0,75 s entre la acción y su resultado. Prueba: pausa en cualquier segundo; algo con sentido tiene que estar a mitad de vuelo.
```
**Fuente:** hyperframes `motion-doctrine` Parte 2; LottieFiles `choreography.md`.

### 2.3 Números de entrada, salida y cascada
**Brecha:** § 4 da 0,4/0,25 s pero no overshoot, escala mínima ni peso en la cascada. Korvin #4 usa cuatro `back.out` distintos y entradas desde `scale: .4`.
**Texto (§ 4, sustituye "Variar"):**
```
- **Entrada ≤0,8 s**; más tiempo = stagger de varios, no un elemento lento. Salida ≈75 % de la entrada. 200 px ≈ ×1,3 de duración, 400 px ≈ ×1,6.
- **Un overshoot por video:** `back.out(1.4–1.7)`. Prohibidos `bounce.out` y `elastic.out`. Elementos parecidos comparten ease+duración.
- **Nada aparece de la nada:** tarjetas y UI entran desde scale 0,9–0,97 + opacidad; solo lo que "vuela" viene de más lejos.
- **Cascada con peso** (total ≤0,5 s): ancla 60–80 px / 0,16–0,20 s; palabra 40–50 px / 0,13–0,16 s; ligero 30–48 px / 0,10–0,13 s; gaps que se achican (×0,84). GSAP: `stagger: { each, from, ease }` o `gsap.utils.distribute`; nunca `from: 'random'` sin `K.seedRandom`.
- **Reacomodo (nudge):** 3 tramos — `power3.in` 10 % del camino en 20 % del tiempo, lineal 65 % en 18 %, `power4.out` 25 % en 62 % — o un `CustomEase`. Lo nuevo entra en el tramo rápido.
- Anticipación 2–4 cuadros solo en el golpe principal; lo secundario sigue 4–8 cuadros después de que para lo principal.
```
**Fuente:** hyperframes `cut-the-curve` §6–7; Emil `animate`; LottieFiles; gsap-skills; dylantarre.

### 2.4 Profundidad y máscara de texto
**Brecha:** § 4 pide "tres capas" sin velocidades; la máscara de texto es manual (`.l > span`) y el ajuste de `#q1` quedó en el video.
**Texto (§ 4, en "Composición de video"):**
```
- Profundidad por velocidad: fondo 0,2×, medio 0,5×, frente 1×. Contra-movimiento: héroe a la derecha → fondo 20–30 % a la izquierda. La sombra llega 1–2 cuadros tarde.
- Texto con máscara: `SplitText.create(el, { type: 'lines', mask: 'lines' })` tras `document.fonts.ready`, mismo `yPercent: 140`. Gancho largo: `K.fitText(el, 940)`.
```
**Fuente:** LottieFiles `choreography.md`; gsap-skills `plugins`; remotion `measuring-text` (idea).

### 2.5 Sonido: capas, dos y medio, familias
**Brecha:** § 6–7 colocan por pico y tonalidad, pero no dicen cuántas capas ni cómo se arma un golpe grande; `duck_curve` existe y el rol no lo nombra.
**Texto (§ 6, al final):**
```
- **Dos y medio:** nunca más de 2 SFX distinguibles a la vez encima de la música. Jerarquía: golpe del guion > SFX de causa > música > textura.
- **Golpe grande = 3 alturas, un pico:** grave (impacto) + medio (whoosh) + agudo (shimmer). Riser 1–3 s → impacto → cola 1–2 s. `duck_curve` baja la cama en cada golpe.
- **Familias:** cada SFX repetido tiene versión fuerte (primero/último) y versión fondo (más corta, más baja) del mismo sonido. Orientativo: click 0,05–0,1 s · pop 0,1–0,2 · whoosh 0,3–0,6 · impacto 0,3–0,5.
```
**Fuente:** clawfu (Murch); startup-os `sound-effects.md`, `audio-design.md`.

### 2.6 Idioma de movimiento en el kit del cliente
**Brecha:** el kit del cliente es sello/intro/clip; no define su movimiento y cada video lo reinventa.
**Texto (§ 2, nueva viñeta):**
```
- `<x>-kit.js` exporta `KV.motion = { ease: 'expo.out', easeOut: 'power2.in', dur: { quick: .25, std: .45, slow: .8 }, enter: 'rise'|'mask'|'scale', overshoot: 1.6, current: 'left' }`: una curva para ≈80 % de los tweens, 3 duraciones, un patrón de entrada, una corriente. Se fija en el piloto.
- Pasan a `kit.js` cuando se usan 2 veces: `K.cut(tl, outEl, inEl, t, {axis, dir, dist, dur, blur})` (2.1), `K.nudge` (2.3), `K.fitText` (2.4), `K.posterize(t, 10)` (stop-motion).
```
**Fuente:** LottieFiles "Brand Motion Identity"; hyperframes; remotion `timing` (`posterize`).

### 2.7 Autorrevisión: cuadros dorados, puerta de costuras, tells y gotchas
**Brecha:** § 9 revisa a ojo; § 11 corrige P0 sin proteger lo que ya estaba bien; § 5 no cubre relativos ni `overwrite`.
**Texto (§ 9, al final; gotchas a § 5):**
```
- **Cuadros dorados:** tras el primer PASS, `render.py --frame N --png qa/golden/beat-NN.png` por beat. En cada vuelta del Juez se repiten y se comparan (opencv `absdiff` + umbral): lo que no debía cambiar, no cambió.
- **Puerta de costuras (`seams.py`, propuesto):** por cada fila de Costuras, medir con Playwright el `getBoundingClientRect` del que sale y del que entra en t±1/30: ambos en movimiento, mismo eje y signo, nunca ambos visibles. FAIL bloquea.
- **Tells antes del Juez:** eyebrow en mayúsculas en todo, "A · B · C", una palabra de color en cada titular, tarjetas iguales con la misma sombra, fade+slide igual en todas. ¿Cuál es la única cosa memorable de la escena? Quita un accesorio.
- **Gotchas:** valores relativos (`y: '-=60'`) se resuelven en el primer render → absolutos; `overwrite: 'auto'` mata tweens al primer render → no sin `test/verify.py`; `tl.addLabel` por beat y los tiempos de 04-build salen de `tl.labels`; colores con `gsap.utils.interpolate`.
```
**Fuente:** `testing-visual-regression`; hyperframes `seam-gate.md`; `frontend-design`; Emil `review-animations`; gsap-skills.

## 3. Lo que NO conviene adoptar
- **Remotion** en cualquier forma (`remotion-dev/skills`, startup-os, open-design): React y licencia propia. Solo ideas.
- **Scripts de HyperFrames** (`seam-gate.mjs`): Node + runtime propio + HeyGen; reimplementar en Python (2.7). Su cursor macOS tampoco: en WhatsApp es un dedo y `K.cursor` ya existe.
- **Reglas de UI** de Emil/wshobson/LottieFiles (≤300 ms, `prefers-reduced-motion`) y **`will-change: transform`** (gsap-performance, HyperFrames): interfaces, no reels; choca con el gotcha de la cámara que escala.
- **"Siempre capa ambiente" y "partículas"** (LottieFiles): chocan con los prohibidos y con 2.2.
- **SFX de `remotion.media`** (memes, sin licencia) y **soundcn** (incluye 110 sonidos de Blizzard no libres): seguimos con Kenney CC0.
- **`loudnorm`, agentes "audio-mixer" y trucos de tiempo real de GSAP** (`force3D`, ScrollTrigger): qa.py ya mide con ebur128, `master_lufs` ya mastera y el render es por cuadro.

## 4. No verificado
- Cifras de startup-os (SFX) y LottieFiles (×1,3/×1,6, 20–30 %, 0,2/0,5/1): sin fuente primaria. "Dos y medio": citada por clawfu; el ensayo de Murch no se leyó.
- Que `overwrite: 'auto'` rompa el determinismo entre workers: razonamiento, no probado.
- `remotion-dev/skills` sin LICENSE visible. Las skills `.claude/skills/` de HyperFrames llevan `metadata.internal: true` (no salen en el marketplace); commit 9123628.
- skillsmp.com no se abrió directo (la búsqueda devolvió agregadores); tampoco `heygen-com/skills/video-edit` ni los archivos profundos de LottieFiles.
