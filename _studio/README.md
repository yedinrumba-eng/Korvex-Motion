# _studio: el motor de Korvex Motion

Aquí está todo lo que hace los videos, **sin nada de ningún cliente**. Cada video es un `index.html` que expone `window.seek(t)`. El renderizador lo captura cuadro por cuadro con Chromium, le pone motion blur promediando sub-cuadros y lo codifica con ffmpeg. La música y los efectos también salen de código (numpy) y caen sincronizados con la imagen.

Cómo se trabaja una idea de punta a punta (intake → roles → puertas): ver el `README.md` de la raíz y el método en `metodo/`.

## Requisitos
- **Python 3.11+** con `playwright numpy opencv-python scipy` y el Chromium de Playwright: `python -m playwright install chromium`.
- **ffmpeg** en el PATH.
- **Node** (opcional): solo para Claude Code y para bajar librerías.
- **Windows:** `setup\instalar-windows.ps1` deja todo listo y lo verifica.

## Qué hay
```
render.py            renderizador determinista: motion blur, audio, workers en paralelo, --draft, --linear, adaptativo
preview.py           hoja de contacto de instantes sueltos (sin blur), para revisar rápido
cues.py              exporta window.CUES (efectos marcados en el timeline) → cues.json
audio/synth.py       sintetizador y mezcla; master_lufs() para redes
lib/                 GSAP 3.15 + plugins, Lottie, kit.js, kit.css, fuentes
sfx/                 SFX CC0 de Kenney (casino, impact, interface, keyboard, ui) + sfx-analysis.md
tools/deliver.py     poster (cuadro asentado) horneado como cuadro 0 + tope de MB (salta directo al CRF estimado)
tools/qa.py          QA automático: archivo, cuadros quietos, cortes, saltos de 1 cuadro, LUFS/dBTP, zona segura, hojas
tools/seams.py       costuras medidas: cada corte de window.SEAMS con Playwright (los dos se mueven, mismo eje y signo, sin doble exposición)
tools/golden.py      cuadros dorados: guarda un PNG por label y en cada vuelta compara (lo que no se tocó, no cambió)
tools/gate_check.py  candado de puertas (hook de Claude Code): sin aprobación no hay guion, video ni entrega
tools/nuevo_producto.py  crea <CLIENTE>/ desde _PLANTILLA-PRODUCTO
tools/nuevo_video.py     crea <CLIENTE>/videos/NN-nombre/ con las plantillas 01–05
tools/key.py         chroma key de fotos con pantalla verde → PNG recortado + esquinas (quads.json)
metodo/              el método: intake, categorías, recetas y un documento por rol (investigador → juez)
plantillas/          01-research · 02-brief · 03-guion · 04-build · 05-revision
refs/                /brag (MIT) e investigacion-2026-10.md (repos analizados, licencias)
setup/               instalación en Windows
test/                pruebas del estudio (determinismo, blur, audio) y kit-motion.html (demo del kit v2)
```

## Comandos (desde `<CLIENTE>/videos/NN-nombre/`)
```bash
python ../../../_studio/preview.py index.html prev.png 1,5,10,20 6       # revisar fotogramas
python ../../../_studio/cues.py index.html cues.json                     # efectos del timeline
python music.py                                                           # música → music.wav (+ audio-rms.js)
python ../../../_studio/render.py --html index.html --out borrador.mp4 --workers 4 --draft --audio music.wav   # borrador (~1 min)
python ../../../_studio/tools/qa.py --video borrador.mp4 --html index.html --out qa                           # QA (PUERTA 3)
python ../../../_studio/render.py --html index.html --out master.mp4 --w 1080 --h 1920 --fps 30 --sub 4 --workers 4 --audio music.wav
python ../../../_studio/tools/deliver.py --video master.mp4 --poster-t 2.2 --out ../../entregas/<cliente>-NN-nombre.mp4
python ../../../_studio/tools/qa.py --video ../../entregas/<cliente>-NN-nombre.mp4 --out qa-final
```
- **`render.py`:**
  - `--workers N` reparte los cuadros entre N Chromium.
  - `--draft` saca 540x960 sin blur.
  - `--linear` hace el blur en luz lineal.
  - `--start/--end` renderiza un tramo, para arreglar una escena y empalmarla.
  - `--frame N --png f.png` renderiza un solo cuadro.
- **Tiempos medidos** de un reel de 20 s: 2 núcleos ≈ 10 min el final y ≈ 1.3 min el borrador. Con más núcleos baja casi en proporción.
- **El render final siempre en la misma máquina:** Chromium en Windows y en Linux no dan los mismos píxeles.

## El kit (`lib/kit.js` → `window.K`)
Todo es función de `t`: nada de `requestAnimationFrame`, `Date` ni estado entre cuadros.

| Grupo | API |
|---|---|
| Timeline | `K.timeline()`, `K.install(tl, porCuadro)` (pone `window.seek`, `window.TL` y `READY`), `K.shift(tl, OFF, CUES)` (corre todo el video OFF segundos, para meter un intro; mueve también labels y costuras) |
| Costuras y tiempo (v3) | `K.cut(tl, sale, entra, t, {axis, dir})` (transición con la ley del vector), `K.nudgeEase` (reacomodo en 3 tramos), `K.posterize(t, 10)` (stop-motion) — ver abajo |
| Matemática | `K.clamp/lerp/prog`, `K.ease.{out3,out5,in3,io3,outExpo,outBack}`, `K.spring(t,w,z)` (rebota, crítico o sobreamortiguado), `K.rng(seed)`, `K.seedRandom(seed)` (siembra `Math.random` para librerías que lo usan al construir) |
| Movimiento pro | `K.springs(t, [{t,v},…])` (spring que cambia de objetivo), `K.edges(t, [{t,l,r},…])` (bordes elásticos: tabs, knobs), `K.zoomLog(t,t0,t1,s0,s1)` (zoom a una sola velocidad), `K.morph(tl, el, t, props)` (contenedor que cambia tamaño/radio/color) |
| Texto | `K.typeOn(t, t0, text, cps)`, `K.scramble(t, t0, dur, text, seed)` (descifrado con semilla), `K.fitText(el, 940)` (achica la letra hasta que quepa) |
| Transiciones | `K.iris(tl, el, t, {x,y,open})`, `K.flood(tl, el, t, {x,y,x2,y2})`, `K.coverRadius(x,y)`, `K.measure(el)` (para match cuts) |
| Cursor | `K.cursor(stage, [{t,x,y,click,down,up},…])` → `.update(t)` en el porCuadro (arco natural, clic con onda, arrastre) |
| Filtros | `K.filters()` agrega `#k-glass` (vidrio líquido) y `#k-goo` → `style="filter:url(#k-glass)"` |
| Lottie | `K.lottie(contenedor, jsonEnLinea)` → `.draw(t)` (usa `lib/lottie_svg.min.js`) |
| Composición | `K.matrix3d(w,h,quad)` (homografía: UI sobre la pantalla verde de una foto), `K.lerpQuad`, `K.grain(stage)` |
| UI lista | `K.waPhone({name, avatar, status, clock, h})` (WhatsApp dark al píxel: `add`, `show`, `hide`, `typingHeader`, `tap`), `K.icon.*`, `K.mark()` (Korvin) |
| Audio | `K.audio(t)` → `{rms, low}` (con `audio-rms.js`) |
| Marca | `K.brand` = el `window.MARCA` del cliente; sus colores quedan en las variables CSS `--brand-*` |

**Plugins de GSAP** (todos gratis desde la 3.13; se registran solos si cargas el `<script>`):
- DrawSVG, MorphSVG, SplitText, CustomEase, MotionPath;
- Physics2D, PhysicsProps, Text, CustomWiggle, CustomBounce, EasePack, Flip.

**No uses ScrambleTextPlugin:** usa `Math.random` en cada cuadro. Para eso está `K.scramble`.

**Kit del cliente:** las piezas de una marca (sello, iconos, intro de marca) van en `<CLIENTE>/<x>-kit.css/js`, nunca aquí. Ejemplo: `PANADERIA-EJEMPLO/panaderia-kit.js` (ejemplo, no incluido), con `P.intro()`, `P.seal()` y `P.clip()`.

### Piezas v3: costuras, tiempo y control (03/10/2026)
Demo: `test/seams-demo.html`.
- **`K.cut(tl, A, B, t, { axis: 'x'|'y'|'z', dir: -1|1, dist, outDur: .28, inDur: .34, blur: 10, text: true })`**: una costura con la ley del vector.
  - A sale acelerando (`power4.in`) en `[t-0,28, t]`; B entra frenando (`power4.out`) en `[t, t+0,34]`. Mismo eje, misma dirección.
  - x/y: viaje de 130 px (x) o 230 px (y). `dir: -1` = izquierda / arriba.
  - z: `dir: -1` = A se encoge a 0,8 y B llega grande (1,25→1); `dir: 1` = A crece y B llega chica (0,75→1).
  - Opacidad: A llega a 0 en `t` (en `t-0,05` si `text`); B arranca en 0,35. Blur pico de 10 px (superficies: `blur: 18`).
  - A y B pueden ser selector, elemento o lista. Su reposo es x/y = 0 y scale 1 (si no, `rest`). B queda oculto desde el cuadro 0.
  - La costura queda en `window.SEAMS` para `seams.py`. Una costura hecha a mano se registra igual: `window.SEAMS.push({ t, out: '#a', in: '#b', axis: 'x', dir: -1 })`.
- **`K.nudgeEase`** (o `ease: 'nudge'`): reacomodo en 3 tramos (`power3.in` 10 % del camino en 20 % del tiempo, lineal 65 % en 18 %, `power4.out` 25 % en 62 %). Lo nuevo entra en el tramo rápido (≈ 20–38 % del tween).
- **`K.fitText(el, 940, { min: 24, max })`**: después de `document.fonts.ready`. Achica la letra del elemento y de sus hijos hasta que el texto mida ≤ 940 px. Mide sin transforms (sirve con spans escondidos con `yPercent`). Nunca pasa del tamaño original (o de `max`) y avisa si ni con `min` cabe. Devuelve `{ size, width, fits }`.
- **`K.posterize(t, 10)`**: congela el tiempo a 10 cuadros por segundo. En el porCuadro: `algo(K.posterize(t))` = stop-motion.
- **`tools/seams.py`**: `python ../../../_studio/tools/seams.py --html index.html` (escribe `qa/seams.json`). Mide cada costura en t ±1 y ±2 cuadros.
  - **FAIL** si uno de los dos no se mueve, si va en otro eje o signo, o si los dos se leen a la vez (opacidad > 0,6).
  - Se corre junto con `qa.py`, antes del Juez.
- **`tools/golden.py`**: lo que no se tocó, no cambió.
  - Tras el primer PASS: `python ../../../_studio/tools/golden.py --html index.html --out qa/golden --save` guarda un PNG por cada `tl.addLabel` (o `--times 0,1.5,…`; `--scale 0.5` va más rápido).
  - En cada vuelta del Juez: `… --compare` vuelve a renderizar esos instantes y da FAIL si un cuadro cambió más del 1 % de sus píxeles. Deja `diff-<t>.png` (guardado | nuevo | mapa).
  - Lo que sí se cambió a propósito va en `--allow 9.5,cierre` (t o label).

## Audio (`audio/synth.py`)
- **Electrónica:** `kick`, `clap`, `snare`, `hat`, `shaker`, `bass_pluck`, `sub_bass`, `pad`, `stab`, `pluck`, `bell`.
- **Acústica / latina:** `nylon` (Karplus-Strong), `strum`, `epiano`/`epiano_chord`, `upright`, `conga`, `guira`, `rim`, `taiko`, `strings`.
- **SFX:** `sfx_pop/send/tick/tap/whoosh/riser/boom/shimmer/sweep/chime/sizzle`, y `load_sample()` para los de Kenney.
- **Mezcla:** `make_ir`/`reverb`, `delay`, `duck_curve`.
- **Master:** `master_lufs(mix, -14, -1.5)` deja -14 LUFS y ≤ -1 dBTP (el AAC sube el pico, por eso -1.5). También están `lufs()`, `true_peak_db()` y `limiter()`.
- `export_rms()` para lo audio-reactivo.

## Reglas del motor (aprendidas a golpes)
- **Estado inicial del cuadro 0** con `gsap.set` inmediato. Un `tl.set(x, …, 0)` no se aplica en el primer `seek(0)`.
- **`fromTo` aplica el `from` desde que se crea.** Si el elemento debe estar oculto antes, usa `immediateRender: false`. Si se anima varias veces, usa `tl.set(el, from, t).to(el, to, t)`.
- **`fetch()` falla en `file://`:** los datos van en línea o con `<script src>` (marca.js, audio-rms.js, Lottie).
- **Imágenes:** `img.decode()` en paralelo puede fallar en Chromium. Carga y decodifica en serie (`B.clip` lo hace). Los videos se usan como cuadros JPEG pintados en un canvas según t.
- **Gotchas de CSS:**
  - Nada de `will-change` en algo que la cámara escala.
  - Nada de `opacity`/`filter` en `preserve-3d`.
  - `backdrop-filter` en pantalla completa es carísimo (~9 s por cuadro).
- **Zona segura de IG:**
  - orgánico: y 150–1550, sin texto en x>950 entre y 900–1700;
  - ad: CTA por encima de y≈1250.
- **Fuentes:** `render.py`, `seams.py` y `golden.py` cargan todas las `@font-face` antes de capturar. Antes, una fuente que se usaba recién a mitad del video salía invisible o a medias en algunos renders (pasaba en `kit-motion.html`).
- **Escalas con GSAP:** a mitad del tween GSAP usa `translate3d` (`force3D: 'auto'`), y el borde de algo que escala puede variar 1 nivel entre renders. Si `verify.py --html` da DISTINTOS en un cuadro con escala, pon `force3D: false` en ese tween (`K.cut` ya lo hace).
- **Nunca uses `pkill -f`** con un patrón que aparezca en tu propio comando: matas tu shell. Usa el PID.
- **Límites:** ≤20 MB por archivo para la carpeta, ≤30 MB para mandarlo por el chat.

## Pruebas
- `test/verify.py`: el mismo MD5 del cuadro 90 en dos renders (determinismo), el blur y el beep a 1.000 s.
  - Para otra página: `python verify.py --html seams-demo.html --frames 0,54,102,150`. Renderiza cada cuadro dos veces y compara el MD5.
- `test/kit-motion.html`: demo del kit v2 (tabs elásticos, scramble, springs, vidrio, Lottie, Physics2D, cursor, iris).
  - Determinista salvo el borde del iris (cuadro 110, ≤4 niveles). Eso ya pasaba antes de v3.
- `test/seams-demo.html`: demo del kit v3 (3 costuras x/y/z, fitText, nudge, posterize). Da PASS en `seams.py` y es determinista.
- `test/seams-bad.html`: 1 costura bien hecha y 4 mal hechas (dirección opuesta, error típico en Z, crossfade, corte seco). `seams.py` debe dar FAIL en esas 4.
- `test/seams-demo-mod.html`: copia con la costura 2 movida 0,1 s. Sirve para ver que `golden.py --compare` la detecta.
- `test/kit_v3_test.py`: pruebas de `K.cut`, `K.nudgeEase`, `K.fitText` y `K.posterize`. Incluye el mismo estado buscando en orden o al azar.
- `test/regresion/`: cuadros 2.0, 11.8 y 17.8 s de Korvin #04, antes y después del kit v3 (idénticos).

## Licencias
- GSAP: licencia estándar gratuita, incluso comercial.
- Lottie-web: MIT (`lib/LICENSE-lottie.txt`).
- SFX de Kenney: CC0.
- Fuentes: OFL.
- /brag: MIT. Su música NO se usa (licencia sin verificar).
- Detalle de los repos analizados: `refs/investigacion-2026-10.md` y `metodo/00-RESUMEN.md`.
