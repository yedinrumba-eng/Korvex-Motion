# Recetas de formato — 12 estructuras reutilizables (120 BPM)

Una receta es una estructura por tiempos **probada** que el Productor cita en el brief (`receta: launch-ui-real`) y el Guionista instancia en el beat sheet. Las recetas no traen copy ni assets: traen el esqueleto, qué se carga de un beat al siguiente, dónde caen los golpes y qué suele fallar.

Convenciones: 120 BPM → beat 0,5 s, compás (c) 2 s; `c3.1` = compás 3, beat 1 = 4,0 s. Todas abren con el módulo **R1 (intro de marca con preguntas, 0–4 s)** salvo R11 (bumper) y R12 (promo, versión corta de 2 s). Los tiempos son para la duración indicada; se estira o recorta el cuerpo, nunca el gancho ni el CTA. Golpe = acento musical (kick/impact + cambio) fijado al beat.

| ID | Receta | Dur. | Categorías | Tono típico | Ya usada en |
|---|---|---|---|---|---|
| R1 | Intro de marca con preguntas (módulo) | 4 s | todas | el del video | Catering 02 v2, 03 v2 (`B.intro()`), Korvin 04a–d |
| R2 | Launch con UI real | 26–30 s | 1, 7 | polished · app-store · cinematic | Korvin 01 |
| R3 | Escenario con hora ("11:47 PM") | 20–22 s | 6, 2 | default · cinematic · deadpan | Korvin 02 |
| R4 | Explainer en 5 escenas | 22–26 s | 3, 7 | default · app-store | Catering 03, Korvin 04a–d |
| R5 | Una forma, sin cortes (morph de UI) | 16–20 s | 4, 7, 1 | polished · app-store | — |
| R6 | Receta paso a paso | 20–24 s | 3, 9, 6 | default · polished | Catering 03 (los 4 pasos) |
| R7 | Testimonio cinematográfico | 16–20 s | 5 | polished · deadpan · cinematic | — |
| R8 | Antes / después | 16–20 s | 2, 6 | default · deadpan | — |
| R9 | Lista de tips | 24–28 s | 9, 3 | default · deadpan · app-store | — |
| R10 | Demo con cursor | 16–20 s | 7, 1 | app-store · default | Korvin 01 (parcial) |
| R11 | Bumper de marca (loop) | 8 s | 4 | polished · cinematic | — |
| R12 | Promo con fecha | 14–16 s | 8 | chaotic · default · cinematic | — |

---

## R1 — Intro de marca con preguntas (módulo de 4 s)
**Cuándo:** siempre que el video sea de un cliente con marca que debe reconocerse desde el cuadro 0 (regla de Yeyow, 02/10/2026). Es el gancho **y** la marca a la vez.
**Estructura**
| t | c | Beat | Qué pasa | Se carga al siguiente | Audio |
|---|---|---|---|---|---|
| 0,0–0,8 | c1.1 | Pregunta 1 | Sello pequeño + nombre + ciudad visibles desde el cuadro 0 (set en 0); "¿TIENES UNA BODA?" entra con una foto en borde orgánico | el borde orgánico | cama suave entra; sin golpe |
| 0,8–1,6 | c1.3 | Pregunta 2 | "¿UN CUMPLEAÑOS?" (corte; otra foto en el mismo borde) | el borde | tecla/pop suave |
| 1,6–2,5 | c2.1 | Pregunta 3 (dolor) | "¿TE PREOCUPA / *LA COMIDA?*" (dos líneas, itálica dorada) | el sello | riser corto |
| 2,5–3,5 | c2.2 | Marca | **Golpe.** El sello crece al centro con aro; entra "<Marca> / <rubro>" + "<nombre del dueño>" | el sello (persistirá pequeño en el cuerpo) | golpe + entra el ritmo |
| 3,5–4,0 | c2.4 | Salida | Sale limpio (telón o el sello se reduce a su esquina) | el fondo de la escena 1 | — |
**Reglas:** 3 preguntas máx., 1–4 palabras cada una, ≥0,8 s asentadas; la tercera es el dolor; la marca llega en un golpe entre 2,5 y 3,0; nada aparece a medio entrar en el cuadro 0. Variante Korvin: observación en vez de preguntas ("Tu WhatsApp ya no duerme.") + la burbuja-K desde el cuadro 0.
**QA especial:** cuadro 0 publicable (es la portada por defecto si `poster_t` falla); `cues.json` con el golpe en 2,5 exacto.
**Errores:** 4+ preguntas; preguntas genéricas ("¿Quieres calidad?"); logo que rebota; intro de 6 s.

## R2 — Launch con UI real (26–30 s)
**Cuándo:** lanzamiento o primer video del producto; hay UI real (chat, panel, formulario) y un flujo entrada → acción → resultado.
**Estructura (28 s)**
| t | c | Beat | Qué pasa | Se carga al siguiente | Audio |
|---|---|---|---|---|---|
| 0–4 | c1–c2 | R1 | Intro de marca con observación/preguntas | la marca a su esquina | golpe 2,5 |
| 4–7 | c3.1 | Promesa | El mensaje en una línea (≤8 palabras), texto héroe 60–80 % del ancho, quieto ≥1,5 s | la línea se vuelve el título del teléfono/pantalla | entra el bajo |
| 7–11 | c4.3 | Entrada | El producto aparece **en uso**: el cliente escribe ("¿Tienen disponible mañana?") en el teléfono (foto con pantalla verde + `K.matrix3d`) | el teléfono | teclas |
| 11–16 | c6.3 | Acción clave | El producto hace lo suyo paso a paso (responde, propone horario, confirma); una burbuja por 2 beats | la burbuja final → tarjeta de resultado | pop afinado por burbuja; **golpe 14,0** en la confirmación |
| 16–20 | c9.1 | Resultado | Lo que cambió para el dueño (la cita en el calendario del panel, el lead guardado) | la tarjeta → bloque de prueba | cama sube |
| 20–23 | c11.1 | Prueba | UN bloque: el claim permitido ("más de 9 empresas activas") o un testimonio verbatim | el bloque sale hacia la dirección del video | acento |
| 23–28 | c12.3 | Cierre | Nombre + tagline + CTA quieto ≥2,5 s + contacto (dentro de la zona segura) | — | **golpe 23,0**; nota final 26,0 |
**Gancho:** observación seria o pregunta de dolor; proof-first (abrir ya con el chat resolviendo) si el tono es app-store.
**Assets:** fotos con pantalla verde recortadas + `quads.json`, textos exactos del flujo, logos, claim con fuente.
**QA especial:** el producto se ve antes de 7 s; cero respuestas inventadas (todo del flujo real); un solo bloque de stats; CTA ≥2,5 s.
**Errores:** landing animada en vez del flujo; 3 bloques de features; demo de 2 s por burbuja ilegible.

## R3 — Escenario con hora ("11:47 PM") (20–22 s)
**Cuándo:** caso de uso / storytelling; el dolor tiene una hora o un lugar.
**Estructura (22 s)**
| t | c | Beat | Qué pasa | Se carga al siguiente | Audio |
|---|---|---|---|---|---|
| 0–4 | c1–c2 | R1 (variante) | Marca desde el cuadro 0 + "11:47 PM." como pregunta/observación en la tercera posición | el reloj/la hora | golpe 2,5 |
| 4–8 | c3.1 | Tensión | "Tu negocio cerró." Llegan 2–3 mensajes de clientes (verbatim plausibles, sin nombres reales); el teléfono en la mesa, luz baja | el último mensaje queda sin responder | cama tensa; cada mensaje un pop seco |
| 8–10 | c5.1 | Giro | El producto entra **en la escena** ("Korvin: en línea") | el estado "escribiendo…" | **golpe 8,0** |
| 10–16 | c6.1 | Resolución | Responde, agenda, confirma: 3 burbujas, una cada 2 beats, con el flujo real | la confirmación → resultado | pops afinados; güira entra |
| 16–18,5 | c9.1 | Resultado | "7:12 AM." La cita en el calendario del panel; el dueño no hizo nada | el calendario → cierre | cama se abre |
| 18,5–22 | c10.2 | Cierre | Marca + tagline + CTA que cierra la historia ("Que Korvin se encargue. Pide tu demo") ≥2,5 s | — | **golpe 18,5**; final 21,0 |
**Gancho:** hora exacta + observación; POV ("Son las 11:47 y te acaban de escribir").
**QA especial:** nada que "diga" el producto fuera de su función real; nombres de clientes ficticios con etiqueta "EJEMPLO" si aparecen; contraste de la escena oscura (texto ≥ 4,5:1).
**Errores:** "antes" más largo que la solución; el producto entra como lista de features; hora y lugar genéricos.

## R4 — Explainer en 5 escenas (22–26 s)
**Cuándo:** educativo; una pregunta real (FAQ) y un proceso de 3–5 pasos. Esqueleto: problema → qué hago → pasos → prueba → nombre.
**Estructura (24 s)**
| t | c | Beat | Qué pasa | Se carga al siguiente | Audio |
|---|---|---|---|---|---|
| 0–4 | c1–c2 | R1 | Intro de marca; la tercera pregunta es la del FAQ ("¿CÓMO PIDO / UNA COTIZACIÓN?") | la pregunta sube | golpe 2,5 |
| 4–6 | c3.1 | Promesa | "Así de fácil." / "En 4 pasos." quieto | la palabra "pasos" → la primera tarjeta | entra el ritmo |
| 6–14 | c4.1 | Pasos | 4 tarjetas numeradas, una cada 2 beats (6,0 · 7,0 · 8,0 · 9,0) y luego **se sostienen** hasta 14; una línea las une | la tarjeta 4 → el objeto del paso siguiente (formulario) | pop afinado por paso (mi-sol-la-do) |
| 14–19 | c8.1 | Haciéndolo | El proceso **de verdad**: el formulario se llena (dedo + tecleo), toque en el botón | la tarjeta → el teléfono | teclas, click |
| 19–21 | c10.3 | Resultado/prueba | El artefacto real (el mensaje de WhatsApp armado, ✓✓) quieto ≥1,5 s | el teléfono se reduce | **golpe 19,0**; "send" |
| 21–24 | c11.3 | Nombre | Marca + "Cuéntanos tu idea ↗" + contacto ≥2,5 s | — | nota final 23,0 |
**Gancho:** la pregunta tal cual la escribe la gente; promesa numerada.
**QA especial:** pasos legibles (≥1 s asentados cada uno y el conjunto ≥3 s); el artefacto final es el real (formato exacto); etiqueta "EJEMPLO" en formularios/chats.
**Errores:** 5 pasos a 0,5 s; diagrama de lo que hace en vez de hacerlo; explicar la empresa antes del paso 1.

## R5 — Una forma, sin cortes (morph de UI) (16–20 s)
**Cuándo:** mostrar varias pantallas o estados de un producto sin que parezca slideshow; identidad + función; tono contenido.
**Estructura (18 s)**
| t | c | Beat | Qué pasa | Se carga al siguiente | Audio |
|---|---|---|---|---|---|
| 0–4 | c1–c2 | R1 | Intro; el sello se **convierte** en el contenedor (morph de contenedor) | el contenedor | golpe 2,5 |
| 4–7 | c3.1 | Forma 1 | El contenedor es una burbuja de chat con la pregunta del cliente | la burbuja se estira → tarjeta | pop |
| 7–10 | c4.3 | Forma 2 | La tarjeta es la cita en el calendario | la tarjeta se divide → lista | **golpe 7,0** |
| 10–13 | c6.1 | Forma 3 | La lista es el panel de leads | el panel se contrae → recordatorio | pop |
| 13–15,5 | c7.3 | Forma 4 | El recordatorio en el teléfono del cliente | el recordatorio → lockup | **golpe 13,0** |
| 15,5–18 | c8.4 | Cierre | El contenedor vuelve a ser el sello/lockup + tagline + CTA ≥2,5 s | (loop opcional: = cuadro 0) | nota final 16,0 |
**Reglas:** un solo objeto que cambia de forma (Flip/morph); cada forma 2,5–3 s con ≥1,2 s quieta; cada cambio en un beat; sin cortes, sin crossfade.
**QA especial:** `transiciones.png` no muestra dos layouts a la vez; `cuts_s` de `qa.py` casi vacío (es normal: el movimiento es continuo) — el Juez revisa quietud ≥6 % y legibilidad.
**Errores:** demasiadas formas (máx. 4); morph de texto letra a letra (ilegible); zoom ambiental encima del morph.

## R6 — Receta paso a paso (20–24 s)
**Cuándo:** un proceso que "se construye" ante el ojo (vaso vacío → cóctel; mesa vacía → mesa servida; idea → propuesta → mesa). Satisfactorio, ASMR-friendly.
**Estructura (22 s)**
| t | c | Beat | Qué pasa | Se carga al siguiente | Audio |
|---|---|---|---|---|---|
| 0–4 | c1–c2 | R1 | Intro; tercera pregunta: "¿Y SI SOLO TUVIERAS QUE / *CONTAR TU IDEA?*" | el plato/mesa vacío | golpe 2,5 |
| 4–6 | c3.1 | Base | El objeto base vacío, quieto, grande (plato, mesa, hoja) | el objeto (persiste todo el video) | cama cálida |
| 6–16 | c4.1 | Ingredientes | 4–5 pasos, cada uno agrega algo **al mismo objeto** (una foto recortada que cae, un texto que se escribe): uno cada 2,5 s; etiqueta corta por paso ≥0,8 s | el objeto cada vez más completo | SFX por ingrediente (cada uno distinto, acentuado el último) |
| 16–19 | c9.1 | Listo | El objeto completo, Ken Burns lento 1→1,04, quieto ≥2 s; "Lo llevamos a la mesa." | el objeto se reduce | **golpe 16,0** |
| 19–22 | c10.3 | Cierre | Marca + CTA ≥2,5 s | — | nota final 20,0 |
**Gancho:** la pregunta "¿y si…?"; el objeto vacío como imagen inesperada; proof-first (el plato terminado 1 s y rebobinar).
**Assets:** fotos de ingredientes/platos recortadas (o `key.py`), orden real del proceso (del dueño).
**QA especial:** continuidad del objeto base (misma posición/escala entre pasos, salvo el Ken Burns final); etiqueta "Imágenes conceptuales" si las fotos lo son.
**Errores:** pasos que cambian de layout; textos largos por paso; el objeto se mueve en cada paso (mareo).

## R7 — Testimonio cinematográfico (16–20 s)
**Cuándo:** prueba social con citas reales y nombre; marca que ya tiene reconocimiento. La confianza se lee quieta.
**Estructura (18 s)**
| t | c | Beat | Qué pasa | Se carga al siguiente | Audio |
|---|---|---|---|---|---|
| 0–4 | c1–c2 | R1 | Intro; tercera línea: "LO QUE DICEN / *DE LA CHEF.*" | el fondo de foto grande | golpe 2,5 |
| 4–8,5 | c3.1 | Cita 1 | Foto grande (Ken Burns 1→1,04) + comillas; la cita entra **por líneas en orden de lectura** (una por beat, luego se sostiene ≥2 s); nombre debajo, pequeño | la comilla persiste | cama suave |
| 8,5–13 | c5.2 | Cita 2 | Otra foto; otra cita, misma gramática; **una** frase destacada (barrido dorado) después de que la línea asentó | la comilla | **golpe 8,5** suave |
| 13–15,5 | c7.3 | Lo que respalda | El servicio/producto en una imagen (la mesa, el chat) quieto | la imagen → lockup | cama sube |
| 15,5–18 | c8.4 | Cierre | Marca + "Hablemos de tu celebración ↗" ≥2,5 s | — | nota final 16,0 |
**Reglas:** citas **palabra por palabra** (incluidos errores de ortografía del original, si el perfil del cliente lo pide), nombre tal cual, máx. 1 frase destacada por cita, nada de estrellas inventadas; 2–3 citas máx.
**QA especial:** cada cita asentada ≥0,3 s/palabra; comparar texto con el perfil § 9 (Juez, criterio 1).
**Errores:** paráfrasis; animación por palabra; cita sin autor; más de 3 citas.

## R8 — Antes / después (16–20 s)
**Cuándo:** arco BAB; hay un "antes" visualizable (chat desordenado → chat atendido; mesa improvisada → mesa del catering). Ads de conversión.
**Estructura (18 s)**
| t | c | Beat | Qué pasa | Se carga al siguiente | Audio |
|---|---|---|---|---|---|
| 0–4 | c1–c2 | R1 | Intro; tercera pregunta: el dolor del "antes" | la etiqueta ANTES | golpe 2,5 |
| 4–8 | c3.1 | Antes | El estado actual, honesto (sin caricatura): 3 cosas que fallan, una por 2 beats, quietas al final | la pantalla/mesa | cama apagada, pops secos |
| 8–9 | c5.1 | Puente | El producto/servicio entra en UN gesto (un toque, el sello cae) | el gesto | **golpe 8,0** |
| 9–14 | c5.3 | Después | El mismo encuadre, ahora resuelto: las 3 cosas cambian de estado una por una (✓) | la última ✓ → resultado | pops afinados, güira |
| 14–15,5 | c8.1 | Resultado | Una línea de resultado permitido, quieta | la línea | acento |
| 15,5–18 | c8.4 | Cierre | Marca + CTA que repite la promesa del gancho ≥2,5 s | — | nota final 16,0 |
**Reglas:** mismo encuadre antes/después (la comparación la hace el ojo); el "antes" nunca inventa cifras ("perdías 30 clientes"); el "después" solo muestra funciones/servicios reales.
**QA especial:** message-match gancho ↔ CTA; nada de precios ni promesas de resultado no permitidas.
**Errores:** caricaturizar al cliente; "antes" en gris y "después" en neón; split-screen con dos layouts cargados.

## R9 — Lista de tips (24–28 s)
**Cuándo:** contenido de valor; 3 (máx. 5) consejos del dueño en sus palabras; busca guardados.
**Estructura (26 s, 3 tips)**
| t | c | Beat | Qué pasa | Se carga al siguiente | Audio |
|---|---|---|---|---|---|
| 0–4 | c1–c2 | R1 | Intro; tercera línea: la promesa numerada ("3 COSAS ANTES DE / *CONTRATAR CATERING*") | el "3" | golpe 2,5 |
| 4–10 | c3.1 | Tip 1 | Número grande → el tip (≤8 palabras, asentado ≥2,4 s) → una línea de por qué (≤10 palabras) + 1 imagen | el número gira al 2 | **golpe 4,0** suave |
| 10–16 | c6.1 | Tip 2 | Misma gramática (misma entrada, misma salida) | el 2 → 3 | golpe 10,0 |
| 16–22 | c9.1 | Tip 3 | Misma gramática | las tres tarjetas se juntan | golpe 16,0 |
| 22–24 | c12.1 | Resumen | Los 3 tips juntos, quietos ≥2 s | el resumen → marca | cama sube |
| 24–26 | c13.1 | Cierre | Marca + "Guárdalo para tu próximo evento" ≥2 s | — | nota final 24,0 |
**Reglas:** gramática fija (misma entrada/salida); varían contenido e imagen, no el movimiento; tips **específicos del cliente** (de su experiencia real), no genéricos.
**QA especial:** cada tip ≥2,4 s asentado; CV de tomas puede ser bajo por diseño → el Juez lo acepta si el guion lo declara; comprobar que ningún tip contradice el perfil § 3.
**Errores:** 5 tips en 20 s; tips de cualquier marca; cambiar la gramática por tip.

## R10 — Demo con cursor (16–20 s)
**Cuándo:** feature drop; una función real con 2–4 acciones; el cursor/dedo **causa** cada cambio.
**Estructura (18 s)**
| t | c | Beat | Qué pasa | Se carga al siguiente | Audio |
|---|---|---|---|---|---|
| 0–4 | c1–c2 | R1 | Intro; tercera línea: la función en lenguaje de resultado ("AHORA AGENDA / *SIN CHOQUES*") | el panel/pantalla | golpe 2,5 |
| 4–5,5 | c3.1 | La pantalla | La UI real quieta, el cursor ya visible (entra desde fuera) | el cursor | cama |
| 5,5–13 | c3.4 | Acciones | 3 veces: mover (0,4 s, ease inOut, trayectoria con leve arco) → clic (`cue('click')`) → efecto ≤1 s → quieto ≥1 s. Una etiqueta corta por acción (≥0,8 s) | el estado final de la UI | click + pop por acción; **golpe 9,0** en la acción clave |
| 13–15,5 | c7.3 | Resultado | El resultado quieto ≥1,5 s (la cita en el calendario, el ✓) | el resultado se reduce | acento |
| 15,5–18 | c8.4 | Cierre | "Ya disponible" + marca + CTA ≥2,5 s | — | nota final 16,0 |
**Reglas:** cursor del kit con clic/arrastre/tecleo; nunca teletransporta; datos en pantalla con "DATOS DE DEMOSTRACIÓN"; UI del código o de capturas, no inventada.
**QA especial:** cada clic tiene su cue en `cues.json`; efecto después del clic (nunca antes); pops de 1 cuadro = 0.
**Errores:** 3 funciones en un video; UI con lorem ipsum; efectos sin causa.

## R11 — Bumper de marca (8 s, loop)
**Cuándo:** identidad; cabecera de otros videos; stories; loop que suma repeticiones. Sin R1 (el bumper **es** la marca).
**Estructura (8 s = 4 compases)**
| t | c | Beat | Qué pasa | Se carga al siguiente | Audio |
|---|---|---|---|---|---|
| 0–1 | c1.1 | Imagen | Una imagen o palabra fuerte de la marca; sello pequeño visible desde el cuadro 0 | la imagen → palabra | nota |
| 1–5 | c1.3 | Tres palabras | 3 palabras/imágenes que SON la marca, una por compás ("Celebrar." "Compartir." "Recordar."), cada una ≥0,8 s asentada | la última palabra → lockup | pop por palabra; **golpe 5,0** |
| 5–7,5 | c3.3 | Lockup | Sello/lockup + tagline, quietos ≥2 s | el lockup se reduce al tamaño del cuadro 0 | nota final |
| 7,5–8 | c4.4 | Loop | El último cuadro = el primero (misma posición, color y escala) | → cuadro 0 | cama vuelve al inicio |
**QA especial:** `render(0) == render(8)` (MD5 del primer y último cuadro); sin CTA de contacto grande (va en el caption).
**Errores:** confeti; logo que rebota; 12 s; loop con salto.

## R12 — Promo con fecha (14–16 s)
**Cuándo:** evento, temporada, promo con fecha real. Versión corta del intro (2 s).
**Estructura (16 s)**
| t | c | Beat | Qué pasa | Se carga al siguiente | Audio |
|---|---|---|---|---|---|
| 0–2 | c1.1 | Fecha-gancho | Marca pequeña desde el cuadro 0 + la fecha/temporada grande ("DICIEMBRE SE RESERVA / *EN OCTUBRE.*") | la fecha | **golpe 0,5** |
| 2–8 | c2.1 | Qué hay | 3 cosas (foto + etiqueta ≥0,8 s), una por compás, misma gramática | la tercera → condición | pop por ítem; güira |
| 8–11 | c5.1 | Condición | Fecha límite / lugar / cupos **reales** quietos ≥2 s | la condición → CTA | **golpe 8,0** |
| 11–16 | c6.3 | CTA | Marca + acción + canal + fecha, quietos ≥3 s | — | nota final 14,0 |
**Reglas:** urgencia solo verificable; sin precios si el perfil los prohíbe; dejar prevista una versión sin fecha (mismo `index.html`, variable `FECHA=null`).
**QA especial:** la fecha aparece ≥3 s en total; plan de bajada anotado en `04-build.md`.
**Errores:** "últimos cupos" sin dato; menú completo en 6 s; CTA de 1,5 s.

---

## Cómo se usa una receta
0. Repetir receta se vale, también entre clientes (el branding la hace distinta). Lo que rota es el look de cada cliente (`rol-productor.md`, paso 3b). Las técnicas que visten cada receta están en `_studio/refs/tendencias.md`.
1. El Productor la cita en `02-brief.md` (`receta: R4 explainer-5-escenas`) y ajusta la duración; si mezcla dos (R3 + R10), lo dice.
2. El Guionista copia la tabla a `03-guion.md`, pone los textos verbatim, los assets con ruta y los golpes exactos, y la convierte en beat sheet completo (todas las columnas de `rol-guionista.md`).
3. El Editor construye por beats; si una receta exige un módulo del kit (R1 → `B.intro()`, R10 → cursor, R5 → morph de contenedor), lo usa; si no existe para ese cliente, lo crea en su kit (`<cliente>-kit.js`), nunca en `_studio/lib`.
4. **Receta nueva**: cuando un video aprobado estrene una estructura que vale repetir, se congela aquí (ID nuevo, tabla, reglas, QA especial, "ya usada en") — la idea del *recipe freeze* de HyperFrames.

## Fuentes de las recetas
- Formatos de `refs/investigacion-2026-10.md` (awesome-opus5-5-videos: launch con UI real, una forma sin cortes, explainer en 5 escenas, receta paso a paso, bumper tipográfico).
- HyperFrames `storyboard-recipe.md` (beat 1,5–3,5 s, held frame, una dirección, callback/hero prop) y `product-launch-video/references/story-design.md` (arcos y formas por rol de beat).
- iart `launch-structure.md` (el sonido manda: drop → reveal, montaje en beats, end card ≥2 s), `short-form-video` (loop: último cuadro = primero), `testimonial-video` (orden de lectura, 1 énfasis, autor obligatorio), `ad-creative-video` (message-match, una variable).
- onetake (ideas, reimplementadas): "qué se carga al siguiente", quietud ≥25 % del tiempo (nuestro `qa.py` pide ≥6 % de cuadros quietos como piso; las recetas apuntan más alto).
