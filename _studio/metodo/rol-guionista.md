# Rol 3 — Guionista → `03-guion.md` + `storyboard.html` (PUERTA 2)

## Misión
Convertir el brief aprobado en **lo que se ve, se lee y se oye, beat por beat, en la grilla de 120 BPM**, con los tiempos de lectura calculados y un storyboard estático que Yeyow pueda juzgar antes de que exista una línea de código. El guion es el contrato con el Editor: lo que no está escrito aquí no aparece en el video, y lo que está aquí se construye tal cual.

`03-guion.md` sustituye al viejo `plan.md` (lleva lo mismo y más).

## Entradas
- `02-brief.md` con `aprobado: true` (mensaje, concepto elegido, receta, arco, tono + "pero no", afirmaciones permitidas, criterios, assets, audio).
- `01-research.md` (flujo real con textos exactos, lenguaje verbatim del cliente, referencias medidas).
- `perfil.md` § Copy aprobado y § Marca, `marca.js`, el kit del cliente (`<cliente>-kit.css/js` o equivalente), `_studio/lib/kit.css`.
- `recetas.md` (la receta elegida con su estructura por tiempos), `refs/brag/tones.md`.

## Salidas
- `03-guion.md` (plantilla abajo) con `aprobado: false` → PUERTA 2 → `aprobado: true`.
- `storyboard.html` (hoja de bocetos estática, sin scripts) → `qa/bocetos.png`.
- Borrador final de `share-copy.txt` y `share-copy-variants.md`.

## Proceso
1. **Grilla.** 120 BPM: beat = 0,5 s; compás = 2 s. Un video de 22 s = 11 compases. Escribir primero la línea de tiempo vacía por compases y asignar bloques de la receta (intro de marca 0–3,5 s · promesa · cuerpo · prueba · cierre).
2. **El gancho primero** (0–3,5 s, incluye el intro de marca). Son **tres componentes que no se repiten**: acción visual (qué pasa en el cuadro 1), texto en pantalla (la línea que se lee), sonido (qué suena/entra). Si los tres dicen lo mismo, dos sobran. El sello/logo está visible desde el cuadro 0 (pequeño) y la marca llega al centro en el golpe de ~2,5–3 s. Gramática de ganchos: pregunta de dolor ("¿Te preocupa la comida?"), observación seria ("11:47 PM. Tu negocio cerró."), promesa directa ("En 4 pasos."), negación ("Deja de contestar a mano."), interrupción de patrón (visual inesperado), proof-first (el resultado ya en pantalla), POV hiperespecífico, hora/lugar. Nunca vocabulario interno (nombres de funciones) en el gancho; nunca fade desde negro.
   - Antes de la línea, elige UN **trabajo** del gancho: reconocerse · pregunta abierta · lo que está en juego · romper una creencia · validar sin culpar · puente a la demo.
   - Para PUERTA 2, **3 ganchos con trabajos distintos** (no 3 redacciones de lo mismo). Yeyow elige uno; los otros van a `share-copy-variants.md` como gancho B y C.
   - Prueba del relleno: borra la segunda línea; si el gancho sigue funcionando, era relleno.
   - Una pregunta solo vale con dato: "¿Te mandan notas de voz pidiendo precio?" sí; "¿Quieres vender más?" no.
   - Nunca acusar al espectador ni abrir con metadatos de serie ("Parte 2"): eso va en una etiqueta pequeña.
3. **Arco** (del brief; se puede proponer otro con nota). Orden de beats por arco, para ~20 s:
   | Arco | Orden de beats | Úsalo cuando |
   |---|---|---|
   | PAS | gancho → dolor → agitación → producto entra → prueba/demo → CTA | el dolor es conocido y urgente |
   | BAB | antes → promesa del después → puente (producto) → paso 1 → paso 2 → wow → CTA | hay un "antes" visualizable |
   | Demo loop | pregunta → producto → ciclo 1 (acción→efecto) → ciclo 2 → confianza → CTA | la UI se explica sola |
   | Future pacing | "imagina…" → nombre → el dolor desaparece → mecanismo → resultado → CTA | se vende una forma nueva de hacer algo |
   | Cascada función→beneficio | gancho de categoría → función → beneficio → función → beneficio → clímax → CTA | hay varias capacidades; cada función se traduce a valor |
   Pirámide invertida siempre: el mensaje aterriza en el beat 2; lo demás es evidencia.
4. **Un beat, una idea, un foco.** Cada beat tiene tipo (`gancho | dolor | promesa | intro-producto | funcion | beneficio | prueba | marca | cta`), un movimiento persuasivo concreto (validar el dolor, contraste, mostrar-no-contar, traducir función a beneficio, prueba social, reducir fricción, regla de tres…) y una emoción (ansiedad → alivio, curiosidad → claridad, confianza, urgencia). "Otro beneficio" no es un beat.
5. **Líneas con tiempo de lectura.** Tabla: línea → palabras → mínimo (0,3 s × palabras, nunca < 1,2 s; oraciones de 8+ palabras: 0,35 s × palabras; etiqueta de 1–3 palabras: 0,8 s) → tiempo asentado que se le da → ✓. El tiempo cuenta **desde que la línea completa está en pantalla hasta que empieza a salir**. Texto secuencial legible: cada 2 beats (1 s), no cada beat; o entra rápido y se sostiene el conjunto. El texto que es solo textura no cuenta.
   - **Tope de palabras por beat** (0,3 s/palabra menos 0,5 s de entrada y salida): 1,5 s → solo una etiqueta (≤3 palabras) · 2 s → 4 · 2,5 s → 5 · 3 s → 7 · 4 s → 9 (tope; ya incluye la reserva de 0,3 s). Más: otro beat o menos texto.
   - **Jerarquía en "Se lee":** PRINCIPAL / SECUNDARIO / DETALLE. El principal entra primero; el secundario 0,15–0,3 s después y a una escala al menos 1,5× menor. Nunca dos textos del mismo nivel moviéndose a la vez. Máximo una palabra resaltada por frase, cuando la línea ya asentó.
   - **Ningún "≈" en la tabla.** Si una línea no llega al mínimo, se acorta o se alarga el beat ANTES de PUERTA 2.
   - **Reserva:** asentado planificado = mínimo + 0,3 s (las entradas y salidas siempre comen tiempo; en Korvin #4 se comieron 0,3–0,6 s por línea).
   - Cada beat se marca **FIJO** (gancho, golpes, CTA, beat quieto) o **FLEXIBLE ±0,5 s** con su **beat donante** ("si ACTÚA no cabe, toma 0,5 s de RESUMEN"). El Editor ajusta sin volver al Guionista.
   - Tras la línea del mensaje y la del resultado, 1 beat sin texto nuevo.
   - Prueba de leer dos veces: si no la lees dos veces mientras está asentada, acórtala o alarga el beat.
   - Con versiones, el mínimo lo fija la línea más larga de todas las versiones.
6. **Copy**: solo de `perfil.md § Copy aprobado`, de la tabla de afirmaciones permitidas o verbatim del cliente. Voz de la marca (de tú, cálida; mayúsculas si el perfil lo pide). Prohibidas las muletillas de IA: "no es X, es Y", listas de negación ("sin X, sin Y, sin Z"), "di adiós a", "lleva tu negocio al siguiente nivel", "revoluciona", "desbloquea", "estoy feliz de compartir", preguntas autorrespondidas ("¿El resultado? …"), rayas largas en titulares. Nada de "los mejores de RD", "calidad premium".
   - **Voz del cliente:** lee `perfil.md` § Marca → Tono de voz y § Copy aprobado, y `01-research.md` § 5 (Voz). Si no hay, el Investigador la arma con 10–20 mensajes reales del dueño a sus clientes: saludo, cierre, cómo llama a su servicio, palabras que nunca usa.
   - La palabra del espectador, no la del experto: "te mandan notas de voz", no "mensajes de audio entrantes".
   - **Dominicanismos:** solo los que ya usa el cliente o los que están en el Diccionario del español dominicano (Academia Dominicana de la Lengua). Nada inventado ni de otro país.
   - Más prohibidas: filas de fragmentos ("Sin filas. Sin esperas. Sin excusas."), una palabra en MAYÚSCULAS como golpe dentro de una frase, "X = Y", "la realidad es que…", "seamos honestos", tríadas forzadas, superlativos sin dato. En pantalla, un fragmento corto con dato es legítimo ("5 pasos."); la regla completa es para el caption.
7. **Beat sheet** (la tabla central; columnas abajo). Reglas: cada beat dice **qué se mueve y qué queda quieto**; cada beat dice **qué se carga al siguiente** (el elemento que persiste o se transforma: la tarjeta que se vuelve campo, el sello que crece, la burbuja que se convierte en cita); una **dirección de salida para todo el video** (p. ej. todo sale hacia arriba o a la izquierda); **un beat quieto a propósito** (nada se mueve y la línea aterriza ≥1,5 s); primer movimiento visible dentro de los 0,2 s de empezar el beat; transiciones con motivo (match cut, zoom-through, iris, telón/flood, morph de contenedor, push) y **nunca crossfade entre dos layouts cargados**.
   - **Re-gancho entre 3 y 10 s:** un cambio que renueva la atención Y conecta con la pregunta del gancho (una contradicción, la condición que faltaba, un cambio de escena, del dicho al ejemplo: entra la UI real). Va en la fila como `regancho: <qué cambia>`. Una sorpresa sin relación con el gancho no cuenta.
8. **Golpes fijados a la música.** 1–3 golpes fuertes (t exacto en beat): la marca al centro, el giro, el cierre. Las revelaciones secuenciales en ventanas de la grilla (cada 2 beats si se leen). SFX por tipo de momento (pop, tecla, send, whoosh suave), arrancando 0–0,1 s antes de la animación. El Editor elige el archivo; el Guionista fija el momento y la intención.
9. **Cámara/encuadre** por beat: quieto, push lento, Ken Burns 1→1,04, zoom-through; zonas: texto dentro de la zona segura (y 150–1550; CTA por encima de y≈1250 si `uso: ad`), nada importante en x>950 entre y 900–1700.
10. **Línea de verdad**: qué es real, qué es "EJEMPLO", qué lleva "Imágenes conceptuales" o "DATOS DE DEMOSTRACIÓN", qué nunca aparece (respuestas inventadas del producto, clientes con nombre).
11. **Poster**: elegir el t del cuadro más fuerte con la marca visible y el texto asentado (ni en transición ni a medio entrar). Va a `deliver.py --poster-t`.
12. **Copy para redes**: `share-copy.txt` (1–3 frases, tono del video) + variantes y hashtags del perfil en `share-copy-variants.md`.
   - El caption no repite el gancho ni resume el video. Hace UN trabajo: una segunda pregunta, el dato que el video no dio (qué incluye la demo), una razón para guardarlo o el mecanismo.
   - Primera línea ≤8 palabras (lo que se ve antes de "más").
   - CTA de comentario solo si hay algo que mandar y alguien que lo atienda ("Comenta DEMO y te escribimos"). Prohibido "sígueme para más". 3–5 hashtags del perfil.
   - En `share-copy.txt` van juntos: el gancho elegido + el caption + la palabra de comentario, si la hay.
13. **Storyboard.html** (hoja de bocetos): una celda 9:16 por beat, en orden, con **las palabras reales en las fuentes y colores reales de `marca.js`**, bloques planos para fotos/paneles/UI que aún no existen, un acento en el foco. Cada celda: `id="frame-NN"`, el momento clave del beat, fila de etiqueta (`NN · NOMBRE` · `t inicio–fin`), nota en negrita de qué se mueve primero y hacia dónde sale, chip con la transición. Dos celdas de cierre: el mapa de transiciones (todas en una tira) y la de tokens (paleta, tipos, prohibidos). Sin scripts, sin assets externos, abre desde `file://`. Se captura con `playwright screenshot --full-page --viewport-size "1440,900" "file://$PWD/storyboard.html" qa/bocetos.png` (CLI de Playwright para Python; en Windows, la ruta absoluta con `file:///C:/...`). Si Yeyow eligió "rápido", se omite la hoja pero no la tabla.
   - Además de `bocetos.png`, exporta **`qa/bocetos-tel.png`**: una columna, celdas de 540 px, la etiqueta debajo (`--viewport-size "600,<alto>"`). Más de 12 celdas: 3 imágenes de 4. Es la que Yeyow ve en el teléfono.
   - Ritmo: una celda densa (UI, chat) seguida de una quieta (marca, reacción, confirmación). Tres seguidas iguales = un beat de más o de menos.
14. **PUERTA 2**: presentar (formato abajo). Las notas de Yeyow van textuales en "Cambios desde v1"; se revisan **solo los beats nombrados**; se sube la versión; se repite hasta "listo". Después del build, la tabla de tiempos se regenera desde `index.html` (los tiempos reales mandan) y se anota.

### Cómo se presenta la PUERTA 2
```
Guion v<N> — <cliente> · <video> · <duración> s · <n> beats · receta <nombre> · arco <nombre>
Este video le dice a <audiencia> que <mensaje>.

| # | Beat | t (compás) | Se ve | Se lee | Por qué |
|---|---|---|---|---|---|
(una fila por beat; "Por qué" rastrea al mensaje)

Golpes en la música: <t1 qué pasa> · <t2> · <t3>. Beat quieto: #<n>. Poster: t=<s>.
Bocetos: qa/bocetos.png (<n> celdas).
Línea de verdad: <qué es real / qué lleva etiqueta>.
Ganchos: A <trabajo> · B <trabajo> · C <trabajo> (recomiendo A porque …).
Cerrado (del brief): mensaje, receta, duración. · Abierto para ti: beats <n>, CTA, gancho A/B/C.
Responde por beat: `va` · `va con nota: <qué>` · `cambia: <qué>` · `sobra` · `el beat está mal` (vuelve a PUERTA 1).
```

## Columnas del beat sheet
| Columna | Qué va |
|---|---|
| `#` · nombre | `03 — Formulario` (el nombre será el id de la escena en el código) |
| t · compás·beat | `9,0–13,5 s · c5.1–c7.3`; duraciones 1,5–4 s; sumadas = duración objetivo (verificar la suma) |
| tipo · persuasión · emoción | `funcion · mostrar-no-contar · claridad` |
| Qué se ve | objetos concretos, cuántos, dónde (zona), asset con ruta |
| Qué se lee | texto **verbatim entre comillas**, con su tiempo de lectura |
| Qué se mueve / qué queda quieto | verbos concretos (ENTRA deslizando desde la derecha, TECLEA, SE ASIENTA, CRECE, SE QUEDA) + easing/duración orientativos (out al entrar, in al salir) |
| Qué se carga al siguiente | el elemento que persiste o se transforma y cómo |
| Audio | golpe en beat / SFX por tipo / qué hace la música (entra la güira, baja la cama) |
| Cámara · transición de salida | quieto / push / Ken Burns; tipo de transición + dirección |
| Restricción | al menos un "no …" por beat que podría volverse genérico |
| Por qué | el trabajo del beat en la historia, rastreado al mensaje; sin "por qué" se corta |

## Plantilla — `03-guion.md`
```markdown
---
cliente: PANADERIA-EJEMPLO
video: 03-de-tu-idea
version: 1
aprobado: false
aprobado_por:                # solo "Yeyow", y solo con sus palabras
fecha_aprobacion:
mensaje: "Pedir una cotización es contar tu ocasión; tú decides si envías."
audiencia: "…"
receta: explainer-5-escenas
arco: demo-loop
tono: default            # pero no: juguetón, pero no infantil
duracion: 26
bpm: 120
poster_t: 5.2
direccion_salida: izquierda
beat_quieto: 6
---

## 1. Gancho (0–3,5 s) — tres componentes
- Acción visual: …
- Texto en pantalla: "…"
- Sonido: …
- Marca: sello visible desde el cuadro 0 (<posición>); marca al centro en t=2,5 (golpe).

## 2. Líneas y tiempos de lectura
| Línea (verbatim) | Palabras | Mínimo (s) | Asentada (s) | ✓ |
|---|---|---|---|---|

## 3. Beat sheet (120 BPM · beat 0,5 s · compás 2 s)
| # · nombre | t · compás | tipo · persuasión · emoción | Se ve | Se lee | Se mueve / quieto | Se carga al siguiente | Audio | Cámara · salida | Restricción | Por qué |
|---|---|---|---|---|---|---|---|---|---|---|
Suma de duraciones: … s (objetivo … s). Cada fila marca FIJO o FLEXIBLE (con su beat donante) y, entre 3 y 10 s, `regancho:`.

## 3b. Versiones (si el brief las pide)
| Campo (clave de versiones.js) | 04a | 04b | 04c | Palabras máx. | Quién confirma |
|---|---|---|---|---|---|
- Por versión cambian DATOS (textos, chips, filas, final real), nunca estructura, tiempos ni golpes. Otro orden de beats = otro video.
- Cada versión tiene su fila en la tabla de tiempos (gancho, transcripción, subtítulos, final) y su propia línea de verdad (rent-a-car: "la disponibilidad la confirma tu equipo").
- Un recorte (otra duración u otro formato) no es una versión: pide su propio gancho y su CTA.

## 4. Golpes fijados a la música
| t | beat | Qué pasa en pantalla | Qué hace la música/SFX |
|---|---|---|---|
Ventanas de revelación secuencial: … (cada 2 beats).

## 5. Transiciones (una dirección: <dir>)
| De → a | Tipo (motivo) | Duración | Qué elemento la motiva |
|---|---|---|---|
Prohibido: crossfade entre dos layouts cargados.

## 6. Línea de verdad
- Real: … · EJEMPLO: … · Imágenes conceptuales: … · Nunca aparece: …

## 7. Zona segura y encuadre
- Texto en y 150–1550; CTA en y … (uso: …); nada en x>950 entre y 900–1700.

## 8. Poster
- t=…: <qué se ve>.

## 9. Copy para redes
- share-copy.txt: "…"
- Variantes + hashtags: ver share-copy-variants.md

## 10. Storyboard
- `storyboard.html` → `qa/bocetos.png` (<n> celdas + mapa de transiciones + tokens).

## 11. Decisiones de Yeyow (PUERTA 2)
- dd/mm: "<texto tal cual>" → beats cambiados: …
## 12. Cambios desde v1 · Pendientes
## 13. Tiempos finales (se regenera desde index.html tras el build)
```

## Checklist de "listo"
- [ ] Gancho con 3 componentes distintos; sello en el cuadro 0; marca al centro en un golpe ≤3,5 s.
- [ ] Mensaje aterriza en el beat 2; cada beat tiene "Por qué" rastreable al mensaje.
- [ ] Todas las líneas con tiempo de lectura ≥ mínimo + 0,3 s de reserva, sin ningún "≈"; texto secuencial cada 2 beats; tope de palabras por beat respetado.
- [ ] 3 ganchos con trabajos distintos; re-gancho entre 3 y 10 s; beats FIJO/FLEXIBLE con donante.
- [ ] Si hay versiones: § 3b con datos y tiempos por versión.
- [ ] `qa/bocetos-tel.png` exportado y caption que no repite el gancho.
- [ ] Copy solo del perfil/afirmaciones permitidas/verbatim; cero muletillas de IA; cero vocabulario interno en el gancho.
- [ ] Cada beat: qué se mueve/qué queda quieto, qué se carga al siguiente, una restricción.
- [ ] 1–3 golpes fijados a beats exactos; SFX por tipo de momento; un beat quieto.
- [ ] Una dirección de salida; transiciones con motivo; sin crossfade de layouts cargados.
- [ ] Suma de duraciones = duración objetivo (±0,5 s); 1,5–4 s por beat.
- [ ] Texto dentro de la zona segura según `uso`; CTA ≥2 s (ad ≥2,5 s).
- [ ] Línea de verdad y etiquetas definidas.
- [ ] Poster elegido en un cuadro asentado con marca.
- [ ] `storyboard.html` con fuentes/colores reales → `qa/bocetos.png`.
- [ ] PUERTA 2 presentada; notas textuales; solo los beats nombrados cambiaron; `aprobado: true`.

## Errores comunes
- Escribir el guion como slideshow: cada beat una tarjeta nueva, nada se carga al siguiente. → "Una forma, nunca se corta": algo persiste o se transforma.
- Screensaver: movimiento que no dice nada (fondos que flotan, zoom ambiental en todo). → Cada verbo tiene un motivo; quietud después del movimiento.
- Texto pegado al beat (0,5 s por línea) porque "va al ritmo". → Cada 2 beats o entra rápido y se sostiene.
- Gancho que nombra la función ("Agenda inteligente con IA") en vez del resultado ("Tu agenda se llena sola").
- Los tres componentes del gancho dicen lo mismo.
- Inventar lo que "dice" el producto (una respuesta de Korvin que no está en su función real; un mensaje de WhatsApp que `quote.js` no arma).
- Beat sheet sin tiempos exactos ("después entra el formulario"). El Editor necesita `t` y beat.
- Bocetos sin las fuentes y colores reales (no se puede juzgar jerarquía) o con motion (no es el momento).
- Cambiar el mensaje/receta/duración en PUERTA 2 sin volver a PUERTA 1.
- Olvidar el poster y el copy para redes (el Editor los necesita en `deliver.py`).

## Qué le pasa al Editor
`03-guion.md` con `aprobado: true`, `storyboard.html` (layouts confirmados: el Editor **viste** esas celdas, no las redibuja), la tabla de golpes y ventanas (para `music.py` y `cue()`), la línea de verdad, el `poster_t`, el copy para redes y los criterios de aceptación heredados del brief. Toda desviación que el Editor necesite hacer se anota en `04-build.md` y, si cambia un beat, vuelve al Guionista para actualizar la tabla de tiempos finales.

## Fuentes de las mejoras v2 (research de marketplaces, 03/10/2026)
Detalle, licencias y lo descartado: `research-2/rol-guionista-propuestas.md`. Ideas tomadas (reescritas) de: arhamhi/hooksmith (MIT: trabajo del gancho, re-gancho, anti-patrones, caption como segundo gancho), motion-creative/skills (MIT: variantes que cambian el disparador), firatcand/founder-skills `motion-picture` (MIT: jerarquía, leer dos veces), ncklrs/startup-os-skills `vsl-storyboard-writer` (FIJO/FLEXIBLE, densidad), blader/humanizer (MIT: muletillas de IA), kennykankush/skillpack y S3YED/appie-kit (MIT: etiquetas de revisión, review pack), anthropics/knowledge-work-plugins `social-content-engine` / `voice-profile` (Apache-2.0).
