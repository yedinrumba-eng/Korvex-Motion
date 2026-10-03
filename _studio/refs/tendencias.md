# Tendencias y técnicas — catálogo del radar (v1, 03/10/2026)

Qué es: el catálogo de técnicas que el Investigador mantiene para que los videos del estudio no se repitan. Cada técnica dice de dónde salió, para qué sirve, cómo se hace en nuestro motor (HTML + GSAP determinista, `window.seek(t)`, Playwright + ffmpeg, música en numpy) y en qué estado está.

Estados:
- **nueva**: no la hemos usado en ningún video del estudio.
- **probada**: ya salió en un video aprobado y funcionó (o está congelada en `recetas.md`).
- **gastada**: se ve copiada igual en todas partes (≥3 fuentes fijas el mismo mes) o Yeyow dice "ya se ve igual". No se propone salvo que el brief lo pida. Usarla mucho dentro del estudio no la gasta: eso lo controla la rotación del look por cliente (`rol-productor.md`, paso 3b).

Fuentes: `repo:` = `yihui-dev/awesome-opus5-5-videos` (MIT; 475 prompts, leídos el 03/10/2026; cada prompt es de su autor y se usa como idea, nunca se copia). `IG:` = reels públicos leídos con Apify `instagram-scraper` el 03/10/2026 (`resultsType: reels`, 20 por cuenta, ≤6 meses; cuentas: framer, notionhq, schoolofmotion). Las cifras de IG son reproducciones públicas relativas a la mediana de **su propia** cuenta; no son "engagement" ni benchmark para nosotros.

Videos del estudio al 03/10/2026: Korvin 01 (launch), 02 (11:47 PM), 03 (por qué), 04 (cómo funciona, 4 versiones) · Catering 01 (celebrar), 02 (cada plato), 03 (de tu idea).

## Tabla resumen

| ID | Técnica | Grupo | Costo | Riesgo | Estado | Usado en |
|---|---|---|---|---|---|---|
| T01 | Costura por objeto compartido | Transiciones | medio | bajo | probada | Korvin 04, Catering 01 |
| T02 | Inundación y contracción (flood) | Transiciones | bajo | bajo | probada | Catering 01 (telón), Korvin 03 |
| T03 | Iris de aspas | Transiciones | medio | bajo | nueva (iris circular: probada) | Catering 02 |
| T04 | Máscara con las letras de la palabra que sale | Transiciones | medio | legibilidad | nueva | — |
| T05 | Zoom a través de un elemento | Transiciones | medio | mareo si se abusa | nueva | — |
| T06 | Interruptor claro/oscuro en el golpe | Transiciones | bajo | estrobo | nueva | — |
| T07 | Gancho palabra por palabra en los beats | Tipografía | bajo | genérico si es todo el video | probada | Korvin 01, 04 |
| T08 | Máscara por líneas | Tipografía | bajo | bajo | probada | Korvin 04, Catering 01–03 |
| T09 | Tipografía que sostiene el layout | Tipografía | alto | legibilidad | nueva | — |
| T10 | Descifrado con semilla que encaja en el beat | Tipografía | bajo | cliché "hacker" | nueva | — |
| T11 | Desregistro de imprenta en el impacto | Tipografía | bajo | parece glitch | nueva | — |
| T12 | Palabra gigante como transición | Tipografía | medio | bajo | nueva | — |
| T13 | Fuentes con roles y ejes variables | Tipografía | bajo | bajo | nueva (roles: probada) | Korvin 02 (Inter 900/200) |
| T14 | Cámara "screen-studio" | Cámara | medio | zoom constante | nueva | — |
| T15 | Plano continuo a través de escalas | Cámara | alto | mareo | nueva | — |
| T16 | Entrada en perspectiva que se asienta | Cámara | bajo | bajo | probada | Korvin 01–03 |
| T17 | Parallax por capas de una foto | Cámara | alto | artefactos | nueva | — |
| T18 | Una forma, nunca se corta + bordes elásticos | UI | medio | bajo | probada en receta (R5), sin video | — |
| T19 | UI reconstruida por componentes | UI | medio | inventar UI | probada | Korvin 01–04, Catering 03 |
| T20 | Ancla persistente secundaria | UI | bajo | bajo | probada | Korvin 04, Catering (sello) |
| T21 | Vidrio líquido en UN elemento | UI | alto | glassmorphism | nueva | — |
| T22 | Goo: pastilla que se estira y se parte | UI | bajo | bajo | nueva | — |
| T23 | Lista que gira y aterriza | UI | bajo | legibilidad declarada | nueva | — |
| T24 | Pared de ítems con línea de escaneo | UI | medio | bajo | probada | Korvin 04 |
| T25 | Papel y notas a mano que se dibujan | Textura | medio | bajo | probada (papel) / nueva (mano) | Catering 01–03 |
| T26 | Halftone / riso en fotos y fondos | Textura | medio | legibilidad | nueva (grano: probada) | todos (grano) |
| T27 | Luz como material | Textura | bajo | parece flare | probada | Korvin 01 |
| T28 | Pixel art cuantizado a 8–12 fps | Textura | medio | fuera de marca | nueva | — |
| T29 | Tres momentos, no diez; valle antes del cierre | Estructura | bajo | bajo | probada | Korvin 02, 03 |
| T30 | Antes/después de UNA acción | Estructura | bajo | caricatura | probada (R8) | Korvin 03 |
| T31 | Bumper de 7–8 s "funciona con…" en loop | Estructura | bajo | bajo | probada en receta (R11), sin video | — |
| T32 | Manifiesto en 5 frases | Estructura | medio | bajo | nueva | — |
| T33 | Caption que entrega la receta | Estructura | bajo | bajo | nueva | — |
| T34 | Una base, varios cortes | Estructura | medio | bajo | nueva (variantes por rubro: probada) | Korvin 04a–d |
| T35 | Sin música: solo sonidos de UI | Sonido | bajo | queda frío | nueva | — |
| T36 | Drop en la revelación, breakdown antes del cierre | Sonido | bajo | bajo | probada | Korvin 02, 03 |
| T37 | Sonido causado por lo que se ve | Sonido | medio | bajo | nueva (SFX al beat: probada) | todos |
| T38 | Un cuadro por beat antes del render | Proceso | bajo | — | probada | todos |
| T39 | Dos revisores + uno que arregla, por rondas | Proceso | medio (tokens) | — | nueva | — |
| T40 | Captions medidos en la fuente real | Proceso | bajo | — | nueva | — |

---

## Transiciones y costuras

### T01 — Costura por objeto compartido
- **Cómo se ve:** algo de la escena A se convierte en algo de la escena B: la línea del gráfico es el borde del documento, el punto dorado es la esquina del recibo, la burbuja del chat es la tarjeta de la cita. "Claro, la siguiente escena salió de esa".
- **Fuente:** repo `prompts/daniel-haida-636937.md` (lista de transiciones buenas/malas), `prompts/brainextends-606193.md` ("match-position", conservar la posición del arte), `prompts/twoclipping-496100.md` ("cada escena está hecha de la anterior").
- **Sirve para:** categorías 1, 7, 3; recetas R2, R4, R5.
- **Cómo se hace en nuestro motor:** `K.measure(el)` para medir el origen y el destino en el stage, `K.morph(tl, el, t, {width,height,borderRadius,background})` o el plugin Flip (`Flip.getState` → `Flip.from`, determinista dentro del timeline). El contenido entra después de que el contenedor empezó a cambiar y sale antes del siguiente cambio (regla de la columna "se carga al siguiente").
- **Costo:** medio. · **Riesgo:** bajo; si hay dos layouts a la vez, `transiciones.png` lo delata.
- **Estado:** probada. · **Usado en:** Korvin 04 (la nota de voz se transforma en cada paso), Catering 01 (el verde se encoge hasta ser el arco del retrato).

### T02 — Inundación y contracción (flood)
- **Cómo se ve:** una forma de color (el botón, el sello, un círculo) crece hasta tapar el cuadro, se queda un beat llena, y se contrae ya convertida en el objeto de la siguiente escena.
- **Fuente:** repo `prompts/twoclipping-496100.md` (gotcha: la inundación tiene que pasar las esquinas y durar ~0,3 s o media pantalla cambia en un cuadro), `prompts/raphaelaubryy-687877.md` ("un círculo se abre desde el botón hacia una escena oscura").
- **Sirve para:** todas; costura entre bloque y cierre; R1 → cuerpo.
- **Cómo se hace en nuestro motor:** `K.flood(tl, el, t, {x,y,x2,y2,dur})` ya existe (usa `K.coverRadius`). El beat lleno coincide con un golpe de `cues.json`.
- **Costo:** bajo. · **Riesgo:** bajo; no encadenar dos floods seguidos (parece slideshow de colores).
- **Estado:** probada. · **Usado en:** Catering 01 (telón verde con borde curvo), Korvin 03 (entradas "por el fondo").

### T03 — Iris de aspas
- **Cómo se ve:** seis aspas cierran como el diafragma de una cámara sobre el objeto y abren sobre la siguiente imagen. Más "foto" que el iris circular.
- **Fuente:** repo `prompts/twoclipping-496100.md` (6 aspas alrededor de una apertura hexagonal; cada aspa = 2 vértices + 2 prolongaciones + el arco corto).
- **Sirve para:** Catering (fotos de platos, R6, R7); categorías 4, 5.
- **Cómo se hace en nuestro motor:** `clip-path: polygon(...)` con los 6 vértices como función de `t` (hexágono que se cierra), o 6 `<path>` SVG negros sobre la escena; el iris circular ya existe (`K.iris`).
- **Costo:** medio. · **Riesgo:** bajo; tapar la marca a mitad del iris no (regla "marca desde el cuadro 0").
- **Estado:** nueva (iris circular: probada). · **Usado en:** Catering 02 (iris circular `clip-path: circle()`).

### T04 — Máscara con las letras de la palabra que sale
- **Cómo se ve:** la frase nueva aparece a través de las letras de la frase vieja; o el ojo de la "O" se vuelve la ventana por donde se ve la siguiente escena.
- **Fuente:** repo `prompts/techhalla-498547.md` ("mask wipe through the letterforms: la línea que sale es la máscara"), `prompts/gdgtify-929495.md` (el contador de la O en ROOM es una apertura).
- **Sirve para:** ganchos de 3 preguntas (R1), manifiestos (T32), categorías 4, 2.
- **Cómo se hace en nuestro motor:** SVG `<mask>` con `<text>` (la fuente real, sin convertir a path) encima de la escena B; se escala el `<text>` con GSAP hasta que una letra cubre el cuadro. Determinista. Para deformar letras hace falta el path del glifo (no lo tenemos en el kit: pedir SVG del wordmark o usar MorphSVG sobre paths exportados).
- **Costo:** medio. · **Riesgo:** legibilidad: la frase vieja tiene que haberse leído (≥0,3 s/palabra) antes de volverse máscara.
- **Estado:** nueva. · **Usado en:** —

### T05 — Zoom a través de un elemento
- **Cómo se ve:** la cámara empuja hacia un botón, una burbuja o un número hasta atravesarlo y aparecer en la siguiente pantalla; o lo contrario, se aleja hasta que el panel es un punto. Caso extremo: zoom infinito por portales.
- **Fuente:** repo `prompts/daniel-haida-636937.md` ("camera push through interface element"), `prompts/dale-vaz-879074.md` (zoom a varias escalas, el escritorio como punto en el espacio), `prompts/koldo2k-778767.md` (zoom exponencial a un punto fijo; la duración de cada tramo es proporcional al log del zoom), `prompts/jake11moran-414633.md` (las ventanas pasan por delante de la cámara).
- **Sirve para:** categoría 7 (una función por dentro), 1; costura R2 → panel.
- **Cómo se hace en nuestro motor:** `K.zoomLog(t, t0, t1, s0, s1)` sobre `#stage` o un grupo (velocidad constante en espacio logarítmico), con `transform-origin` en el elemento medido con `K.measure`. La escena B vive dentro del elemento a escala pequeña y se cambia por la grande cuando llena el cuadro. Sub-cuadros (`--sub 4`) para que no vibre.
- **Costo:** medio. · **Riesgo:** "zoom constante" es un error en la lista de haida; máximo 1–2 por video, nunca dentro de un morph (R5).
- **Estado:** nueva. · **Usado en:** —

### T06 — Interruptor claro/oscuro en el golpe
- **Cómo se ve:** toda la paleta se invierte en un cuadro justo en el golpe (papel → carbón; la tinta sigue siendo la misma). Divide el video en dos actos sin cortar.
- **Fuente:** repo `prompts/ik-builds-585923.md` ("hard light/dark switches"; la batería entra en el switch oscuro).
- **Sirve para:** R8 (antes/después), R3 (noche/mañana), categorías 2 y 6.
- **Cómo se hace en nuestro motor:** variables CSS `--bg/--ink/--accent` en `:root`; `tl.set(document.documentElement, {'--bg': ..., '--ink': ...}, tGolpe)`. El cambio es un `set`, no un tween (si se interpola parece crossfade). El `cue` del golpe va al mismo `t`.
- **Costo:** bajo. · **Riesgo:** hacerlo más de 2 veces = estrobo; comprobar contraste ≥4,5:1 en los dos modos.
- **Estado:** nueva. · **Usado en:** —

## Tipografía animada

### T07 — Gancho palabra por palabra en los beats
- **Cómo se ve:** la frase del gancho cae palabra por palabra, una por beat o por semicorchea (125 ms a 120 BPM), y se queda quieta. Solo la frase héroe se anima así.
- **Fuente:** repo `prompts/raphaelaubryy-687877.md` (compás 1: el gancho aterriza palabra por palabra en los beats), `prompts/techhalla-498547.md` (spring por glifo, stagger de 1/16 de nota), `prompts/jake11moran-414633.md` (entra palabra por palabra desde la derecha). Antídoto: `prompts/daniel-haida-636937.md` ("evitar que cada palabra se anime por su cuenta; la tipografía se mueve como objeto diseñado").
- **Sirve para:** R1 (tercera pregunta), promesa de R2/R4; todas las categorías.
- **Cómo se hace en nuestro motor:** `SplitText.create(el, {type:'words'})` + `stagger` = beat/4; `K.spring(t, 14, 0.8)` por palabra si se quiere peso; `S0` (`gsap.set`) de los `yPercent` en el cuadro 0. Variante de salida: Physics2DPlugin con velocidades de `K.rng(seed)` (las letras caen; demo Codrops/Osmo, 14/05/2025, https://tympanus.net/codrops/?p=93244).
- **Costo:** bajo. · **Riesgo:** si todo el texto del video entra así, es "video típico". Una frase héroe por video.
- **Estado:** probada. · **Usado en:** Korvin 01 ("ATIENDE. AGENDA. VENDE." una por beat), Korvin 04 (preguntas por spans con `yPercent: 140`).

### T08 — Máscara por líneas
- **Cómo se ve:** cada línea sube desde una ventana invisible, como si saliera de una ranura; nada se desvanece.
- **Fuente:** repo `prompts/brainextends-606193.md` ("short masked vertical movements"), `prompts/twoclipping-496100.md` ("text rises out of a mask line"), `prompts/raphaelaubryy-687877.md` ("masked type reveals"); web: Codrops/Osmo, SplitText con máscara, 14/05/2025, https://tympanus.net/codrops/?p=93244.
- **Sirve para:** todas; es la entrada por defecto del estudio.
- **Cómo se hace en nuestro motor:** `SplitText.create(el, {type:'lines', mask:'lines'})` tras `document.fonts.ready`, `yPercent: 140 → 0`, `expo.out`; o spans a mano con `overflow:hidden` (Korvin 04). `rol-editor.md` ya lo documenta.
- **Costo:** bajo. · **Riesgo:** bajo.
- **Estado:** probada. · **Usado en:** Korvin 04, Catering 01–03.

### T09 — Tipografía que sostiene el layout
- **Cómo se ve:** las palabras tienen un papel físico: una es dintel, otra columna, otra plataforma. La frase final se apoya en lo que las palabras anteriores construyeron. Hay un momento de quietud total (≥400 ms).
- **Fuente:** repo `prompts/gdgtify-929495.md` ("BUILD THE FLOOR": roles arquitectónicos de las palabras, baseline que se dobla con la carga, `render(0)=render(20)`).
- **Sirve para:** categoría 4 (manifiesto de marca), T32; Catering ("<LEMA / DE LA / MARCA>").
- **Cómo se hace en nuestro motor:** composición en SVG con `<text>` posicionado y transformado por GSAP (rotaciones de 90°, traslaciones en el beat); la "deformación" se limita a `skewY`/`scaleY` del grupo o a una línea SVG que se curva con `MorphSVG` (no deformar glifos sin su path). Quietud declarada en el guion para que el Juez no la marque.
- **Costo:** alto (diseño de la composición). · **Riesgo:** legibilidad si la palabra gira antes de leerse.
- **Estado:** nueva. · **Usado en:** —

### T10 — Descifrado con semilla que encaja en el beat
- **Cómo se ve:** las letras barajan caracteres y se asientan una a una justo en el beat.
- **Fuente:** repo `prompts/techhalla-498547.md` (Fisher–Yates con semilla por glifo, snap en el beat), `refs/investigacion-2026-10.md` (scramble con semilla).
- **Sirve para:** cifras permitidas (hora "11:47", "12 de 12"), categorías 6, 7.
- **Cómo se hace en nuestro motor:** `K.scramble(t, t0, dur, texto, seed)` en el `porCuadro`; nunca ScrambleTextPlugin (usa `Math.random`). `dur` = 1 beat.
- **Costo:** bajo. · **Riesgo:** cliché "hacker/IA" si se usa en títulos; solo para números o estados ("escribiendo…").
- **Estado:** nueva. · **Usado en:** —

### T11 — Desregistro de imprenta en el impacto
- **Cómo se ve:** en el cuadro del golpe el texto se duplica 2–4 px en dos tintas de la marca al 40 %, y en 0,1 s vuelve a registrarse. Se siente como un afiche mal impreso, no como glitch.
- **Fuente:** repo `prompts/techhalla-498547.md` (misregistration solo en cuadros de acento); web: BUCK, "Texture, Noise & Attitude" y "Human-Made Rebound", 12/01/2026, https://pencilsdown.buck.co/p/looking-ahead-bucks-2026-predictions.
- **Sirve para:** Catering (papel + oro), categorías 4 y 8 (promo); tono chaotic/default.
- **Cómo se hace en nuestro motor:** dos clones del texto con `mix-blend-mode: multiply`, `translate(±3px)`, `opacity` 0 → 0,4 → 0 en una ventana `[tGolpe, tGolpe+0,1]` escrita en el timeline (no en `porCuadro`).
- **Costo:** bajo. · **Riesgo:** con rojo/cian parece RGB split (prohibido en varios briefs del repo); usar solo colores de `marca.js`. Máx. 2 golpes por video.
- **Estado:** nueva. · **Usado en:** —

### T12 — Palabra gigante como transición
- **Cómo se ve:** una palabra crece hasta que una letra llena el cuadro y dentro de la letra ya está la siguiente escena; o la palabra del gancho se convierte en la UI del producto.
- **Fuente:** repo `prompts/daniel-haida-636937.md` ("typography may scale very large and become a transition device"), `prompts/raphaelaubryy-687877.md` (compás 2: una palabra del gancho se transforma en la UI).
- **Sirve para:** R2 promesa → entrada; categoría 1 y 2.
- **Cómo se hace en nuestro motor:** `K.zoomLog` sobre el `<text>` SVG usado como `<mask>` (T04) o `clip-path: text` no existe: usar la máscara SVG. La escena B se monta debajo con `tl.set(..., t)`.
- **Costo:** medio. · **Riesgo:** bajo si la palabra se leyó quieta ≥1 s antes de crecer.
- **Estado:** nueva. · **Usado en:** —

### T13 — Fuentes con roles y ejes variables
- **Cómo se ve:** tres voces tipográficas con trabajo fijo: display (1–4 palabras), grotesca para líneas secundarias, mono pequeña para "migas" (hora, etiqueta, contador). La display puede respirar en peso o ancho (`wdth` 125 → 100 al asentarse).
- **Fuente:** repo `prompts/techhalla-498547.md` (sistema de 3 fuentes, mono ≤18 caracteres), `prompts/daniel-haida-636937.md` (JetBrains Mono para cifras), `prompts/twoclipping-496100.md` (el wordmark se comprime estrechando el eje `wdth`); web: Codrops Motion Highlights #11, 24/07/2025, https://tympanus.net/codrops/?p=97643 (tipografía variable con pesos que cambian).
- **Sirve para:** todas; Korvin (Inter es variable), Catering (Manrope es variable).
- **Cómo se hace en nuestro motor:** `font-variation-settings: "wght" 700` como propiedad animable por GSAP (`tl.to(el, {fontVariationSettings: '"wght" 900'})`). La mono para etiquetas "EJEMPLO", horas y contadores.
- **Costo:** bajo. · **Riesgo:** bajo; una sola palabra variable por escena.
- **Estado:** nueva (roles: probada). · **Usado en:** Korvin 02 (Inter 900 titulares / 200 reloj; Michroma solo wordmark).

## Cámara y espacio

### T14 — Cámara "screen-studio"
- **Cómo se ve:** la cámara acerca a cada estado de la UI para que llene el cuadro, el cursor crece con la cámara, cada clic tiene un anillo suave y el cursor vuelve al inicio para que el video cierre en loop.
- **Fuente:** repo `prompts/demonugc-525162.md` y copias ("la cámara hace zoom para que cada estado llene el cuadro"), `prompts/twoclipping-496100.md` ("screen-studio style, el cursor escala con la cámara"); web: screen.studio, página de producto, consultada 03/10/2026, https://screen.studio/ (zoom automático donde hubo clics, cursor suavizado, anillo en el clic, cursor que regresa para el loop).
- **Sirve para:** R10 (demo con cursor), R2 acción clave; categorías 7 y 1.
- **Cómo se hace en nuestro motor:** `#stage` con `transform: scale()` y `transform-origin` hacia `K.measure(el).cx/cy` con `K.zoomLog` (1 → 1,6 máx.); `K.cursor(stage, path)` ya trae clic con onda y arrastre; el cursor va en un grupo que no escala con la cámara para que parezca que crece. Zona segura: lo ampliado no puede sacar texto de y 150–1550.
- **Costo:** medio. · **Riesgo:** "zoom constante" (haida); una ampliación por acción clave, no por beat.
- **Estado:** nueva. · **Usado en:** — (el cursor sí: Catering 03 dedo en el formulario).

### T15 — Plano continuo a través de escalas
- **Cómo se ve:** una sola toma que entra en el objeto: del teléfono al chat, del chat a la respuesta, de la respuesta al dato del negocio. Una regla al costado dice la escala.
- **Fuente:** repo `prompts/acoramaa-053577.md` (escritorio → átomo sin cortes, regla de escala), `prompts/irinatoxi-962937.md`, `prompts/rush3rx-342153.md` ("una cámara, sin cortes").
- **Sirve para:** categoría 3 y 7 ("cómo funciona por dentro"); Korvin 04 futuro (versión "rayos X").
- **Cómo se hace en nuestro motor:** capas anidadas en `#stage` con `K.zoomLog` largo (10–15 s) y sustitución de capas cuando llenan el cuadro (T05); sin 3D real. La "regla" es un `<div>` con `K.typeOn`/contador.
- **Costo:** alto. · **Riesgo:** mareo y `% quieto` bajo (declararlo en el guion; el Juez pide ≥6 %).
- **Estado:** nueva. · **Usado en:** —

### T16 — Entrada en perspectiva que se asienta frontal
- **Cómo se ve:** la pantalla entra con una leve inclinación 3D y se asienta de frente; tres tarjetas entran con inclinaciones opuestas y pequeñas.
- **Fuente:** repo `prompts/brainextends-606193.md` ("subtle perspective tilt during the entrance, settling toward a frontal view"; "small opposing tilts"), `prompts/daniel-haida-636937.md` (profundidad con moderación).
- **Sirve para:** R2 entrada del teléfono, R9 tarjetas; categorías 1, 7.
- **Cómo se hace en nuestro motor:** `perspective: 1400px` en el padre, `rotateY: 12 → 0` con `expo.out`; `K.matrix3d` cuando la UI va sobre una foto con pantalla verde. Gotcha: nada de `opacity`/`filter` en `preserve-3d` (fade al wrapper).
- **Costo:** bajo. · **Riesgo:** bajo; nunca "tarjetas 3D que giran sin motivo" (haida).
- **Estado:** probada. · **Usado en:** Korvin 01 (teléfono 3D), 02, 03 (`perspective`).

### T17 — Parallax por capas de profundidad de una foto
- **Cómo se ve:** una foto de un plato o una mesa respira en 3 planos (fondo, sujeto, primer plano) mientras la cámara se acerca despacio.
- **Fuente:** repo `prompts/koldo2k-778767.md` (cada paisaje en 3 capas desde su mapa de profundidad; escala de capa = cámara^Z con Z entre 0,45 y 1,22).
- **Sirve para:** Catering R6/R7 (fotos quietas que no parecen slideshow); categoría 5.
- **Cómo se hace en nuestro motor:** 3 PNG recortados (`tools/key.py` o recorte manual) escalados con `scale = Math.pow(cam, Z)` en `porCuadro`. El mapa de profundidad y el relleno de huecos son externos (Higgsfield/otro) → etiqueta "Imágenes conceptuales".
- **Costo:** alto (preparar capas). · **Riesgo:** bordes recortados visibles; usar movimientos ≤4 %.
- **Estado:** nueva. · **Usado en:** — (Ken Burns plano 1 → 1,04: probada en Catering).

## UI / producto en pantalla

### T18 — Una forma, nunca se corta + bordes elásticos
- **Cómo se ve:** un solo contenedor cambia de tamaño, radio y color y es, por turnos, botón, cargador, burbuja, tarjeta, lista, toast. Los indicadores de tabs y los knobs tienen dos bordes con springs distintos: el borde que va adelante se estira. Un slider arrastrado más allá del máximo se estira y vuelve.
- **Fuente:** repo `prompts/demonugc-525162.md` (plantilla repetida 7 veces: dzhohola, hicallmechai, morse, nezbuilds, sanjeevn72, twoclipping-402193), `prompts/annacher-433425.md` (versión con producto real), `prompts/verbove-268381.md`, `prompts/thegrootdev-966114.md`.
- **Sirve para:** R5; categorías 4, 7, 1 (Korvin: burbuja → cita → panel → recordatorio).
- **Cómo se hace en nuestro motor:** `K.morph`, `K.springs(t, keys)` (spring que cambia de objetivo, suma una respuesta por cambio), `K.edges(t, keys)` para los dos bordes; arrastre = valor que sigue al cursor mientras `down`, spring al soltar. Todo en `porCuadro`. Loop: último cuadro = primero, cursor incluido.
- **Costo:** medio. · **Riesgo:** bajo; máx. 4 formas en 18 s (R5).
- **Estado:** probada en receta (R5), ningún video aún. Es la técnica más repetida del repo: en 2027 será "gastada" afuera; úsala pronto o con giro propio. · **Usado en:** —

### T19 — UI reconstruida por componentes, no screenshot
- **Cómo se ve:** la pantalla del producto está hecha de piezas (cabecera, burbujas, botones) que se animan por separado, con los tokens reales del cliente. Nada parece una captura pegada.
- **Fuente:** repo `prompts/daniel-haida-636937.md` ("reconstruir/recortar/apilar para que cada región anime"), `prompts/ho-ba-761062.md` ("romper los screenshots en componentes"), `prompts/proanaliteg-458642.md` (UI rehecha desde los tokens, cero capturas), `prompts/l3d1c-632524.md` (importa los tokens CSS del sitio).
- **Sirve para:** todas las de Korvin; Catering 03 (formulario real).
- **Cómo se hace en nuestro motor:** `K.waPhone` (WhatsApp dark al píxel: `add/show/hide/typingHeader/tap`), `K.applyBrand` (`--brand-*` desde `marca.js`), kits por cliente (`<cliente>-kit.js`). Textos exactos del flujo real (research § 4).
- **Costo:** medio. · **Riesgo:** inventar UI que el producto no tiene (regla 2 de CLAUDE.md).
- **Estado:** probada. · **Usado en:** Korvin 01–04, Catering 03.

### T20 — Ancla persistente secundaria
- **Cómo se ve:** un elemento pequeño se queda durante todo el cuerpo (una barra de reproductor, la cabecera del chat, el sello) y conecta las tomas aunque todo lo demás cambie. Siempre secundario al contenido.
- **Fuente:** repo `prompts/brainextends-606193.md` (`<persistent_player>`: "este reproductor recurrente conecta las tomas y debe ser visualmente secundario").
- **Sirve para:** R2, R4, R5; cualquier video con 3+ escenas.
- **Cómo se hace en nuestro motor:** elemento fuera de los grupos de escena, `tl.set` en el cuadro 0, posición fija dentro de la zona segura; se mueve solo en los golpes.
- **Costo:** bajo. · **Riesgo:** bajo; no debe tapar texto al ampliar con la cámara (T14).
- **Estado:** probada. · **Usado en:** Korvin 04 (burbuja-K junto a la fila de pasos), Catering 01–03 (sello pequeño).

### T21 — Vidrio líquido en UN elemento
- **Cómo se ve:** una pastilla o barra de herramientas de vidrio que refracta la foto que tiene detrás, con borde cromático fino y luz en el filo; se estira como gota al arrastrar. Es el lenguaje de iOS 26.
- **Fuente:** web: Design Milk, Liquid Glass (WWDC, junio 2025), 16/06/2025, https://design-milk.com/apple-returns-to-a-layered-software-design-with-liquid-glass-interface/; Pixelmatters, tendencias UI 2026, 06/01/2026, https://pixelmatters.com/insights/7-UI-design-trends-to-watch-in-2026; repo `prompts/twoclipping-496100.md` (cada elemento de vidrio clona la escena de atrás y la filtra con `feImage` + tres `feDisplacementMap` a escalas distintas para bordes cromáticos; gotcha: `backdrop-filter: url()` falla en Chromium).
- **Sirve para:** Catering (toolbar sobre fotos de platos), categoría 1 polished; Korvin solo si el panel lo tiene de verdad.
- **Cómo se hace en nuestro motor:** `K.filters()` trae `#k-glass` (turbulencia, no lente); para el look real hace falta un clon de la escena dentro del elemento + mapa de desplazamiento tipo campo de distancia (canvas) → trabajo de kit nuevo. `backdrop-filter` a pantalla completa cuesta ~9 s/cuadro (README del motor).
- **Costo:** alto. · **Riesgo:** "glassmorphism en todo" es prohibido: UN elemento, solo sobre fotos, nunca sobre texto.
- **Estado:** nueva. · **Usado en:** —

### T22 — Goo: pastilla que se estira y se parte
- **Cómo se ve:** dos formas se funden como líquido al acercarse y se separan con un cuello que se adelgaza; la isla dinámica se estira, se parte y la gota se vuelve otra cosa. Burbujas de chat que se fusionan en una tarjeta.
- **Fuente:** repo `prompts/twoclipping-496100.md` (goo = blur + umbral de alfa, y la fuente encima para que el vidrio quede nítido; "la Dynamic Island se estira como líquido, se parte y crece en una ventana"); IG: reel de framer sobre hover líquido con rastro "gooey" (08/07/2026, 2,8× la mediana de su cuenta).
- **Sirve para:** Korvin (R5, R3: mensajes que se juntan en una cita), categoría 7.
- **Cómo se hace en nuestro motor:** `K.filters()` → `filter: url(#k-goo)` en el grupo de las dos formas; posiciones con `K.springs`; el texto va en una capa encima sin filtro. Determinista.
- **Costo:** bajo. · **Riesgo:** bajo; no es "onda" ni partícula.
- **Estado:** nueva. · **Usado en:** —

### T23 — Lista que gira y aterriza en lo importante
- **Cómo se ve:** una lista larga pasa a toda velocidad (no se lee, a propósito) y frena despacio sobre el ítem que importa; 0,2 s después aparece el signo "?" o la etiqueta.
- **Fuente:** repo `prompts/jake11moran-414633.md` (30 "cosas difíciles" con íconos; rápido, aterriza en "managing your desktop").
- **Sirve para:** R1 variante (lo que te preguntan todo el día → "¿tienen disponible mañana?"), R9 (de 20 tips a 3); categorías 2, 6, 9.
- **Cómo se hace en nuestro motor:** `translateY` de una lista con `expo.out` largo (2 beats), snap en el beat; o `K.springs` sobreamortiguado. Legibilidad: el guion declara que la lista "no se lee" y el ítem final cumple ≥1,2 s quieto (criterio 4).
- **Costo:** bajo. · **Riesgo:** el Juez marcará texto ilegible si no está declarado.
- **Estado:** nueva. · **Usado en:** —

### T24 — Pared de ítems con línea de escaneo
- **Cómo se ve:** una pared de tarjetas/fotos reales; una línea la recorre y marca 2–3 ganadores que se iluminan.
- **Fuente:** repo `prompts/raphaelaubryy-687877.md` ("wall of real clips with a scan line and 3 winners"), `prompts/annacher-433425.md` (muro de anuncios reales que aterriza en el mejor).
- **Sirve para:** Korvin (catálogo, "busca en tu info"), Catering (menú de 12 platos → los 3 del evento); categorías 7, 3.
- **Cómo se hace en nuestro motor:** grid CSS + `translateY` de la línea en `porCuadro`; las filas que coinciden cambian `--brand-accent` cuando la línea pasa por su `K.measure(el).cy`.
- **Costo:** medio. · **Riesgo:** bajo.
- **Estado:** probada. · **Usado en:** Korvin 04 (escáner sobre el "Cerebro", `#scan`).

## Textura, color y acabado

### T25 — Papel y notas a mano que se dibujan
- **Cómo se ve:** fondo papel, notas de marcador que se escriben solas al lado de la UI, subrayados a mano que aparecen y se borran, etiquetas tipo cinta de máquina de escribir.
- **Fuente:** repo `prompts/ik-builds-585923.md` (papel claro, notas de marcador que se dibujan, Caveat con `stroke-dashoffset`, Anton para tipo cinético), `prompts/stokebuilder-356793.md` (papel, etiquetas de cinta, marcas a mano), `prompts/helloshiva0801-438284.md` y `prompts/anabology-491441.md` ("paper style"/"papery feel"); web: BUCK, "Human-Made Rebound" (proceso visible, imperfección como señal), 12/01/2026, https://pencilsdown.buck.co/p/looking-ahead-bucks-2026-predictions; Codrops/Osmo, garabatos con DrawSVG, 14/05/2025, https://tympanus.net/codrops/?p=93244.
- **Sirve para:** Catering (ya es papel), Korvin R9 tips ("nota del dueño"), categoría 9 y 3.
- **Cómo se hace en nuestro motor:** `DrawSVGPlugin` sobre paths (subrayados, círculos, flechas) o `stroke-dasharray` sobre `<text>` SVG con una fuente manuscrita (Caveat, licencia OFL); `K.grain` para el papel. La "escritura" del texto manuscrito pide el path de la letra: si no, se usa `K.typeOn` con la fuente a mano.
- **Costo:** medio. · **Riesgo:** bajo; no mezclar con UI oscura de Korvin sin motivo.
- **Estado:** probada (papel) / nueva (notas a mano). · **Usado en:** Catering 01–03 (papel, sello que se dibuja con DrawSVG).

### T26 — Halftone / riso en fotos y fondos
- **Cómo se ve:** fotos con trama de puntos, dos tintas, bordes de impresión; textura de tinta en el fondo. Se siente impreso, no renderizado.
- **Fuente:** repo `prompts/stokebuilder-356793.md` ("halftone, manga and pixel print, kinetic data type"), `prompts/rneayan-441493.md` (estilo risograph), `prompts/techhalla-498547.md` (afiche de calle que se mueve); web: BUCK, "Texture, Noise & Attitude", 12/01/2026 (misma URL que T25).
- **Sirve para:** Catering (R12 promo, R9), categoría 8 y 4; tono chaotic.
- **Cómo se hace en nuestro motor:** trama con `radial-gradient` repetido en un pseudo-elemento + `mix-blend-mode: multiply` sobre la foto, o `feImage` con patrón; `K.grain(stage)` ya existe (semilla fija, 8 baldosas). Determinista.
- **Costo:** medio. · **Riesgo:** ensucia la legibilidad de la UI; solo fotos y fondos, nunca sobre texto ni chat.
- **Estado:** nueva (grano: probada). · **Usado en:** todos los videos (`K.grain`).

### T27 — Luz como material
- **Cómo se ve:** un brillo especular cruza despacio el lockup o la tarjeta una vez; un rim light dorado en el borde; caída oscura hacia los bordes; viñeta contenida. "Filmamos un objeto premium aunque sea software".
- **Fuente:** repo `prompts/daniel-haida-636937.md` (sección LIGHTING/MATERIAL: specular que pasa, rim light, bloom tenue, viñeta; "no desenfocar el producto para que parezca cine").
- **Sirve para:** R2 cierre, R11 bumper, R7; categorías 1, 4, 5; tono polished/cinematic.
- **Cómo se hace en nuestro motor:** un `linear-gradient(100deg, transparent, rgba(255,255,255,.35), transparent)` en una capa con `mask-image` del logo y `translateX` de −100 % a 200 % en 0,8 s (una vez); rim = `box-shadow inset` fijo; viñeta = `radial-gradient` estático.
- **Costo:** bajo. · **Riesgo:** si brilla en cada beat es lens flare (prohibido). Una pasada por video, sin glow.
- **Estado:** probada. · **Usado en:** Korvin 01 (barrido de luz sobre el logo).

### T28 — Pixel art cuantizado a 8–12 fps
- **Cómo se ve:** figuras de píxeles grandes que se mueven "a dos" (15 fps) o a 8–12 fps aunque el video sea de 30; paleta fija de ~24 colores.
- **Fuente:** repo `prompts/majidmanzarpour-927543.md` y `prompts/zacxbt-944604.md` (animar parámetros suaves y cuantizar al grid de píxeles cada cuadro; paleta fija; nada de antialias), `prompts/koldo2k-778767.md` (recortes a 15 fps "on twos"); web: BUCK 2026 (frame rates bajos como señal deliberada), 12/01/2026.
- **Sirve para:** categoría 8 (promo de temporada con tono chaotic), bumpers de Korvex Motion; no para Korvin ni Catering en su tono base.
- **Cómo se hace en nuestro motor:** `K.posterize(t, 10)` (pendiente en `rol-editor.md`): `tq = Math.floor(t*10)/10` para esas capas; `image-rendering: pixelated`; canvas lógico pequeño escalado por entero.
- **Costo:** medio. · **Riesgo:** fuera de marca; lee "gamer/retro".
- **Estado:** nueva. · **Usado en:** —

## Estructuras y formatos de guion

### T29 — Tres momentos, no diez; valle antes del cierre
- **Cómo se ve:** el video tiene 3–4 ideas visuales, cada toma una idea, y el ritmo baja justo antes del cierre (la escena previa al logo es la más calma). "Mejor 3 momentos extraordinarios que 10 animaciones de features mediocres".
- **Fuente:** repo `prompts/daniel-haida-636937.md` ("ONE SHOT = ONE IDEA", "approximately four visual ideas", "the rhythm briefly slows"), `prompts/raphaelaubryy-687877.md` ("one idea per shot, lots of empty space"), `prompts/twoclipping-496100.md` ("el muro se sienta en el breakdown").
- **Sirve para:** todas; es la regla contra el "kitchen sink".
- **Cómo se hace en nuestro motor:** en `02-brief.md` § 4 estructura: ≤4 bloques de contenido; en `03-guion.md` la columna "curva de ritmo" marca el valle (quietud ≥2 s) antes del cierre; `qa.py` mide `% quieto` y CV de tomas.
- **Costo:** bajo. · **Riesgo:** bajo.
- **Estado:** probada. · **Usado en:** Korvin 02 (tensión → alivio → demo → remate), Korvin 03.

### T30 — Antes/después de UNA acción
- **Cómo se ve:** el mismo encuadre, el estado roto; una sola acción (un prompt, un toque, el sello que cae) y el mismo encuadre resuelto. Sin caricatura del "antes".
- **Fuente:** IG: framer, reel "make this page responsive" (sitio solo desktop → un prompt → responsive), 02/07/2026, 4,5× la mediana de reproducciones de la cuenta en los últimos 4 meses (el más alto de los 19 leídos); repo `prompts/raphaelaubryy-687877.md` ("the key output as big type"); recetas R8.
- **Sirve para:** R8; categorías 2 y 6; ads de conversión.
- **Cómo se hace en nuestro motor:** R8 tal cual (mismo layout, 3 cosas que cambian de estado ✕ → ✓ una por 2 beats); el "puente" es un solo gesto (`K.cursor` clic o el sello que cae con `K.spring` crítico).
- **Costo:** bajo. · **Riesgo:** "antes" gris y "después" neón (error de R8); caricaturizar al dueño.
- **Estado:** probada (R8). · **Usado en:** Korvin 03 (comparación sin/con Korvin, filas que se voltean).

### T31 — Bumper de 7–8 s "funciona con…" en loop
- **Cómo se ve:** un lockup quieto y una fila de logos/categorías que pasa debajo; 7–8 s; el último cuadro es el primero. Sin CTA grande (va en el caption).
- **Fuente:** IG: notionhq, "works with all your favorite agents", 7 s, 18/09/2026, 2,0× la mediana de su cuenta (el más alto de los 11 leídos; sus videos largos de casos quedan en ~1×); framer, "3D Transforms", 8 s, 01/09/2026, 1,0×; recetas R11.
- **Sirve para:** R11; categoría 4; Korvin "Hecho para: salones · rent-a-car · restaurantes · transporte" (categorías reales del perfil).
- **Cómo se hace en nuestro motor:** R11 con `render(0) == render(8)` (MD5 del primer y último cuadro, QA de R11); la fila de logos con `translateX` lineal que cierra el ciclo exacto en 8 s.
- **Costo:** bajo. · **Riesgo:** bajo; solo logos/categorías permitidas por el perfil (nada de clientes no autorizados).
- **Estado:** probada en receta (R11), ningún video aún. · **Usado en:** —

### T32 — Manifiesto en 5 frases (spoken word tipográfico)
- **Cómo se ve:** cinco frases cortas del dueño, en orden, cada una cambia la arquitectura del cuadro; sin beat de baile: la cue sheet sigue frases, pausas y énfasis; hay un silencio visual de ≥400 ms; se entiende sin audio.
- **Fuente:** repo `prompts/gdgtify-929495.md` (discurso de 5 líneas; "no forzar el discurso a un beat"; quietud 400 ms; `render(0)=render(20)`), `prompts/advait-jayant-712107.md` (manifiesto de 20 s).
- **Sirve para:** categoría 4 (marca), 5 (voz del dueño con sus palabras reales del perfil "Tono de voz"); Catering ("<lema de la marca>"); tono polished/deadpan.
- **Cómo se hace en nuestro motor:** receta nueva candidata (R13): 5 frases × ~3,5 s, cada frase ≥0,3 s/palabra, la grilla de 120 BPM se usa solo para los 2 golpes; T09 y T04 como mecánicas; `cues.json` con pausas.
- **Costo:** medio (copy del dueño, verbatim). · **Riesgo:** bajo; peligro de "frases de marketing": solo palabras del dueño o del perfil.
- **Estado:** nueva. · **Usado en:** —

### T33 — Caption que entrega la receta
- **Cómo se ve:** el video muestra el resultado; el caption da los pasos/el "prompt"/la lista para que el espectador lo guarde o comente para pedirlo.
- **Fuente:** IG: framer, hover líquido con el prompt completo en el caption, 08/07/2026, 2,8× su mediana; framer, esfera 3D "comenta Sphere y te mandamos el prompt", 16/07/2026, 1,2× en reproducciones pero 277 comentarios (la mediana de comentarios de la cuenta es ≈11); melodyskim x notionhq, pasos numerados para pequeños negocios en el caption, 25/09/2026.
- **Sirve para:** categoría 3 y 9 (guardados), Korvin "cómo configurar tu información en 4 pasos", Catering "qué preguntar antes de contratar catering".
- **Cómo se hace en nuestro motor:** no es código: `share-copy.txt` lleva la lista completa (1–3 frases + pasos); el video termina con "los pasos están en el caption" (CTA suave orgánico). Se mide en guardados y comentarios a 7 días (`02-brief.md` § 16).
- **Costo:** bajo. · **Riesgo:** "comenta X" como gancho forzado; solo si la receta vale.
- **Estado:** nueva. · **Usado en:** —

### T34 — Una base, varios cortes
- **Cómo se ve:** del mismo `index.html` salen el de 30 s, el de 15 s y el bumper de 6 s, y la versión 16:9 para la web, como listas de escenas distintas. La vertical se recompone, no se recorta.
- **Fuente:** repo `prompts/l3d1c-632524.md` ("los cortes de 30, 15 y 6 s en 16:9 y 9:16 son cada uno una lista de escenas distinta"), `prompts/verbove-268381.md` (exportar todos los formatos en paralelo), `prompts/daniel-haida-636937.md` ("no recortar la composición de escritorio"), `prompts/palashbagchi11-389221.md`.
- **Sirve para:** ads (3–5 ganchos, resto igual; `02-brief.md` § 4b), R11 derivado de R2, web del cliente.
- **Cómo se hace en nuestro motor:** `window.CUT = 'full'|'15'|'bumper'` leído por `escena.js` para decidir qué escenas monta y `window.DURATION`; `render.py` corre una vez por corte; `K.shift` para re-ubicar bloques. Zona segura por formato.
- **Costo:** medio (diseñar las 2–3 listas). · **Riesgo:** bajo.
- **Estado:** nueva (variantes por rubro: probada). · **Usado en:** Korvin 04a–d (misma estructura, cambian textos y ejemplo).

## Sonido

### T35 — Sin música: solo sonidos de UI
- **Cómo se ve:** silencio y un sonido suave por cada cosa que aparece: tecla, pop, clic, tono resuelto en el logo. Versión pensada para que el cliente le ponga encima el audio de moda de Instagram.
- **Fuente:** repo `prompts/annacher-433425.md` ("No music. Synthesize UI sounds with numpy"), `prompts/aschapmann-724497.md` ("un efecto suave por elemento y silencio el resto"), `prompts/bilimfili1-459762.md` ("sin SFX de stock; yo le pongo la música"), `prompts/daniel-haida-636937.md` (lenguaje de sonido: impacto bajo suave, clic táctil, tic metálico, tono resuelto; evitar risers EDM y whooshes).
- **Sirve para:** R10 (demo), orgánico sin música horneada (`research § 10`), categorías 7 y 3.
- **Cómo se hace en nuestro motor:** `music.py` sin cama: solo `sfx_pop/tap/tick/send/chime` de `synth.py` colocados por `cues.json`, master a −14 LUFS igual (`master_lufs`); entregar también `music-con-cama.wav` por si se publica con sonido propio.
- **Costo:** bajo. · **Riesgo:** queda frío si el video dura >20 s; usar en ≤18 s.
- **Estado:** nueva. · **Usado en:** —

### T36 — Drop en la revelación, breakdown antes del cierre
- **Cómo se ve (se oye):** la música entra en secciones: tensión → la batería cae exactamente en la revelación (el producto entra, el interruptor claro/oscuro, el iris que abre) → un breakdown casi vacío bajo la escena calma → el tema vuelve con el logo.
- **Fuente:** repo `prompts/ik-builds-585923.md` ("drums drop on the dark switch… slam back on the type and the logo"), `prompts/twoclipping-496100.md` ("el zoom aterriza en el drop, el muro se sienta en el breakdown, el wordmark vuelve con el beat"), `prompts/raphaelaubryy-687877.md` ("The drop: a circle opens out of the button").
- **Sirve para:** R2, R3, R8; categorías 1, 2, 6.
- **Cómo se hace en nuestro motor:** `music.py` por secciones con `env` por compás; los golpes de `recetas.md` ya están (R3: 8,0 y 18,5). Lo nuevo es el **breakdown**: quitar kick y bajo 1 compás antes del cierre y dejar `pad`. Si la música es ajena (licenciada), medir la grilla con numpy (onset/energía por compás, calibrar al kick real) antes de guionar, como piden esos prompts.
- **Costo:** bajo. · **Riesgo:** bajo; nada de "riser EDM" largo (lista de haida).
- **Estado:** probada. · **Usado en:** Korvin 02 (Re menor → golpe 4,0 → Fa mayor), Korvin 03 (golpe + Fa en "KORVIN SÍ").

### T37 — Sonido causado por lo que se ve
- **Cómo se ve (se oye):** cada sonido tiene una causa visible y su intensidad sale del cuadro: el crepitar depende del brillo del fuego, cada nota viene de una colisión, los clics del teclado son el ritmo, los cilindros encienden en el orden real.
- **Fuente:** repo `prompts/nathanwilbanks-981110.md` ("el sonido sale de cuán fuerte arde el fuego en cada cuadro"), `prompts/kamstudiolabs-440893.md` ("cada nota viene de una colisión visible"), `prompts/iniyanai-856596.md` (grabaciones reales de switches como beats), `prompts/dys-hay-749645.md` (orden de encendido real del V8).
- **Sirve para:** R6 (receta paso a paso: cada ingrediente suena distinto), R10 (cada clic), Catering (chisporroteo real).
- **Cómo se hace en nuestro motor:** ya tenemos la mitad: `cues.json` nace del timeline (`cues.py`) y los SFX arrancan con la animación. Lo nuevo: exportar desde `porCuadro` un parámetro visual (p. ej. área de la burbuja, velocidad del cursor) a `cues.json` como `v` y que `music.py` lo use para `vel`/`bright` del `sfx_pop`/`pluck`. Determinista porque sale del mismo `seek`.
- **Costo:** medio. · **Riesgo:** bajo; sin barras de ecualizador ni estrobos (regla de contención del brief).
- **Estado:** nueva (SFX al beat: probada). · **Usado en:** todos (pops afinados por paso en Korvin 04 y Catering 03).

## Procesos de edición y producción

### T38 — Un cuadro por beat antes del render
- **Cómo se ve:** antes de renderizar, una hoja de contactos con un cuadro por beat (y uno a mitad de cada transición); se arregla lo apretado, lo ilegible y lo fuera de grilla; después se decodifican cuadros del MP4 final, no solo capturas del navegador.
- **Fuente:** repo `prompts/demonugc-525162.md` (build 7), `prompts/l3d1c-632524.md` ("20 stills en una hoja de contactos antes de renderizar nada"), `prompts/daniel-haida-636937.md` (lista de 10 timestamps + "inspeccionar cuadros decodificados del MP4"), `prompts/twoclipping-496100.md` (buscar pops de un cuadro: diferencia entre cuadros 3× la de sus vecinos), `prompts/raphaelaubryy-687877.md` (sub-cuadros a t−1/240, t, t+1/240 mezclados con `tmix`).
- **Sirve para:** todos.
- **Cómo se hace en nuestro motor:** `preview.py index.html prev.png 1,5,10 6`, `qa.py --out qa` (contacto.png, transiciones.png, saltos de 1 cuadro, % quieto, CV), `render.py --sub 4`. Ya es el método.
- **Costo:** bajo. · **Riesgo:** —
- **Estado:** probada. · **Usado en:** todos.

### T39 — Dos revisores que rankean + uno que arregla, por rondas temáticas
- **Cómo se ve:** cada ronda tiene 3 agentes: dos revisores con lentes distintos sacan 9–10 problemas cada uno y los rankean P0/P1/P2; el tercero arregla todos los P0 y los demás solo si valen. Las rondas cambian de tema (materiales y tipografía → cámara e interacción → "¿sale o no?" + QA). Copia de seguridad antes de cada ronda y rollback de lo que no se pudo arreglar. Variante: un juez evalúa una sola vez y solo lo "egregio" vuelve; nada de rehacer todo.
- **Fuente:** repo `prompts/voxyz-ai-345550.md` (3 rondas × 3 agentes, P0/P1/P2, backup y rollback), `prompts/stokebuilder-356793.md` (juez una vez; solo lo egregio vuelve; sin bucles de rehacer), `prompts/nathanwilbanks-981110.md` (crítica de un modelo de visión como supervisor de VFX, ~40 veces).
- **Sirve para:** PUERTA 3 (Editor + Juez); series de 4 versiones (Korvin 04a–d).
- **Cómo se hace en nuestro motor:** `rol-juez.md` ya limita a 2 vueltas. Propuesta: la vuelta 1 del Juez se parte en dos lentes (Verdad+legibilidad / Movimiento+sonido), cada una devuelve ≤10 hallazgos con P0–P2 en `04-build.md`; el Editor arregla P0 obligatorio, P1 si cabe, P2 se anota. `git stash`/copia de `index.html` antes de cada vuelta.
- **Costo:** medio (tokens). · **Riesgo:** —
- **Estado:** nueva. · **Usado en:** —

### T40 — Captions medidos en la fuente real, ajustados al safe zone
- **Cómo se ve:** cada línea en pantalla se mide con la fuente real antes de renderizar y se encoge hasta caber en la zona segura 9:16; nada queda bajo los botones de Instagram.
- **Fuente:** repo `prompts/l3d1c-632524.md` ("captions medidos en la fuente real y encogidos al safe zone 9:16"); web: Opus Pro, captions en Reels 2026, 11/11/2025, https://www.opus.pro/blog/instagram-reels-caption-subtitle-best-practices (tercio central, 2–4 s por bloque, sans bold, evitar sobre-animar; fuente C, sin datos primarios de Meta).
- **Sirve para:** todos; Juez criterio 9 (zona segura) y 4 (tiempos de lectura).
- **Cómo se hace en nuestro motor:** `K.fitText(el, maxW)` (pendiente en `rol-editor.md`): mide `getBoundingClientRect` tras `document.fonts.ready` y baja `font-size` en pasos de 2 px hasta `maxW ≤ 940`; `qa.py --html --safe` ya revisa la zona.
- **Costo:** bajo. · **Riesgo:** —
- **Estado:** nueva. · **Usado en:** —

---

## Lo que dijo el radar de Instagram (03/10/2026)
- framer (19 reels, mediana 22,6 k reproducciones): ≥3× solo dos: el antes/después de una acción (4,5×) y el video de lanzamiento de 75 s (4,5×). El hover líquido con el prompt en el caption, 2,8×. Los tutoriales largos de 37–50 s quedaron en 0,1–0,8×.
- notionhq (11 reels, mediana 26,5 k): ningún ≥3×. El más alto es el bumper de 7 s "works with all your favorite agents" (2,0×); los casos de cliente de 70–100 s quedan en ~1×.
- schoolofmotion (18 reels, mediana 8,1 k): ningún ≥3×. Arriba están los "tips rápidos" de una sola técnica (2,5× y 1,8×).
- Lectura: en cuentas de software, el formato corto y de una sola idea (antes/después, bumper) sube más que el tutorial largo. No es una regla; es lo que se vio en 48 reels propios de 3 cuentas (los 10 restantes eran colaboraciones de otras cuentas y no se contaron). Se vuelve a medir en el próximo radar.

## Gastadas o prohibidas para nosotros
Las de siempre (perfil del estudio, `CLAUDE.md` y `02-brief.md` § 6) y las que el repo repite como prohibidas o como errores:
- **Partículas, confeti, bursts, sparkles**: prohibidas en el estudio; también las prohíben los prompts más cuidados del repo (`demonugc`, `brainextends`, `raphaelaubryy`, `techhalla`, `daniel-haida`). Un "momento de celebración" se hace con T02 o T22.
- **Anillos de onda / shockwave**: prohibidos (`brainextends`, `raphaelaubryy`). 
- **Lens flare, glow, neón, "AI purple", gradientes arcoíris**: prohibidos (`daniel-haida`: "NOT cyberpunk, crypto, neon, generic AI purple"). T27 (luz como material) es lo permitido: una pasada, sin glow.
- **Temblor de cámara**: prohibido. El drift de "unos píxeles" de `alexwtlf` tampoco: nuestra cámara está quieta o se mueve con intención (T14, T05).
- **Rebote exagerado / bouncy UI / logo que rebota**: prohibido en el estudio y en casi todos los prompts del repo ("a tiny overshoot at most", "overshoot below ~2 %").
- **Glassmorphism en todo**: prohibido; T21 es UN elemento sobre una foto.
- **Clichés de IA** (robots, cerebros, redes neuronales, HUD futurista, "stock tech interface sounds"): prohibidos (`techhalla`, `daniel-haida`).
- **Glitch / RGB split / CRT / scanlines**: no son nuestros. `raphaelaubryy` los prohíbe; `pound75423` los usa en cada beat (brainrot). El VHS/CRT es moda de plugins (Analog FX Lab, Cavalry; School of Motion IG 15/09/2026) → gastada afuera, fuera de marca adentro. T11 (desregistro de imprenta) es la única pariente permitida, en 2 colores de marca y 2 golpes.
- **Crossfade, wipe aleatorio, spin, whip-pan cada 2 s, "slide-left SaaS", zoom-blur spam**: lista de transiciones malas de `daniel-haida`. Nuestras costuras son T01–T06.
- **Cinco screenshots deslizándose / "tour de features" / tres bloques de stats**: gastado en el repo (lo que `moritzkremb` pide, lo que `daniel-haida` rechaza). Un bloque de prueba por video (criterio 12).
- **Marcos, HUD, timecode, fps, "scrubber", watermark, texto en las esquinas**: delatan "hecho con IA" (`1littlecoder-914649`, `ik-builds`, `brainextends`). Nada de cromo decorativo; las etiquetas obligatorias (EJEMPLO, Imágenes conceptuales) van pequeñas y dentro de la zona segura.
- **Jerga de animador en pantalla** ("squash", "stagger") y frases de marketing extra fuera del mensaje: prohibidas (`ik-builds`, `techhalla`).
- **Cada palabra animada por su cuenta en todo el video**: genérico (`daniel-haida`); T07 es para UNA frase héroe.
- **Caption karaoke por palabra con cambios de color**: lo marcan como sobre-animado (Opus Pro, 11/11/2025, fuente C). Nuestros subtítulos: por línea, quietos, en la zona segura.
- **Barras de ecualizador / estrobos al beat**: regla de contención de `02-brief.md` § 10; lo audio-reactivo es sutil (Korvin 02).
- **Zoom constante / tarjetas 3D girando sin motivo / blur excesivo**: errores de `daniel-haida`.
- **"Una forma, nunca se corta" tal cual la plantilla** (botón → loader → check → isla → reproductor → slider → toggle → tabs → gráfico → ⌘K → toast): ya la copiaron 9 cuentas del repo con el mismo orden. Usar R5 con nuestros estados reales, no esos.
- **Rectángulos redondeados como idea visual central**: School of Motion (fin de 2025) los llama fórmula; nuestra UI los usa porque el producto los tiene, pero no son el concepto del video.
- **Intro de logo de 5 s**: prohibido (`daniel-haida`); nuestra marca entra con R1 en 2,5–3,0 s y es también el gancho.

## Fuentes web del radar v1 (fecha de publicación)
- School of Motion, "End of Year 2025" (podcast y notas), fin de 2025, https://schoolofmotion.com/blog/eoy2025 — el "gusto" como ventaja; rectángulos redondeados como fórmula; motion dentro de producto.
- School of Motion, Motion Mondays 26/01/2026, https://schoolofmotion.com/blog/motion-mondays-january-26-2026 — AE 26 con 3D nativo; "Motion DNA Test" de Vucko; flujos híbridos.
- BUCK, "Looking Ahead: BUCK's 2026 Predictions", 12/01/2026, https://pencilsdown.buck.co/p/looking-ahead-bucks-2026-predictions (y LBB, 21/01/2026) — motion por defecto, rebote de lo hecho a mano, textura y ruido, mascotas.
- Vucko, Communication Arts, 13/01/2026, https://www.commarts.com/columns/vucko — reconocer una marca por su movimiento: consistencia, timing, distinción.
- Motionographer, "25 (+1) for 2025", 02/01/2025, https://motionographer.com/2025/01/02/25-for-2025-the-motionographers-crystal-ball-motion-design-predictions-part-2/ — tipografía cinética táctil, glitch "preciso", física a medida, retrofuturismo.
- Rive, entrevista a Joey Korenman, 09/01/2025, https://rive.app/blog/what-s-next-in-motion-design-from-school-of-motion-s-founder — tiempo real, motion hacia producto.
- Rive, Spotify Wrapped 2025, 09/01/2026, https://rive.app/blog/spotify-used-rive-for-spotify-wrapped-2025 — sistema modular "mixtape", motion que se adapta al largo del texto y al dato.
- Adobe, "2026 Creative Trends Forecast", 12/08/2025, https://business.adobe.com/uk/blog/adobe-2026-creative-trends-forecast — multisensorial, conexión humana, "surreal silliness", sabor local (sirve para Catering: lo local, lo táctil).
- Codrops / Osmo, "5 demos con plugins gratis de GSAP", 14/05/2025, https://tympanus.net/codrops/?p=93244 — SplitText con máscara, Physics2D, DrawSVG garabatos, MorphSVG.
- Codrops, Motion Highlights #11, 24/07/2025, https://tympanus.net/codrops/?p=97643; #15–#17 (26/12/2025 – 29/03/2026), https://tympanus.net/codrops/category/articles/ui-interactions-animations-roundups — fluidos, microinteracciones, grids que se deforman, tipografía variable.
- Design Milk, Liquid Glass (WWDC 2025), 16/06/2025, https://design-milk.com/apple-returns-to-a-layered-software-design-with-liquid-glass-interface/.
- Pixelmatters, "UI design trends 2026", 06/01/2026, https://pixelmatters.com/insights/7-UI-design-trends-to-watch-in-2026.
- screen.studio (página de producto), consultada 03/10/2026, https://screen.studio/.
- Opus Pro, captions en Reels 2026, 11/11/2025 (fuente C: sin datos primarios de Meta), https://www.opus.pro/blog/instagram-reels-caption-subtitle-best-practices.
- Descartadas por SEO sin sustancia: Videobolt "Top motion graphics trends 2026" (11/12/2025; solo promociona plantillas), listas de agencias "best studios 2026", LottieFiles "animation trends" (2022, viejo).
