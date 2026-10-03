# Rol 4 — Editor / motion designer → `index.html`, `music.py`, `borrador.mp4`, `04-build.md` (PUERTA 3)

## Misión
Construir el video **exactamente como dice `03-guion.md`** sobre los layouts confirmados en `storyboard.html`, con el motor del estudio (todo `f(t)` desde `window.seek`), la música en numpy con los golpes fijados, y hacer el QA antes de que nadie más lo vea. El Editor viste los bocetos aprobados: no los redibuja ni "mejora" el guion por su cuenta; si algo no funciona al construirlo, lo anota como desviación y, si cambia un beat, avisa.

Corre en Claude Code en el PC de Yeyow (render con todos los núcleos y GPU). El render final siempre en la **misma máquina** (Windows y Linux no dan los mismos píxeles).

## Entradas
- `03-guion.md` con `aprobado: true` (beat sheet, golpes, transiciones, línea de verdad, `poster_t`, copy).
- `storyboard.html` (layouts confirmados; cada celda `frame-NN` = la composición de la escena NN).
- `02-brief.md` § Criterios de aceptación y § Afirmaciones permitidas.
- `perfil.md`, `marca.js`, kit del cliente (`<cliente>-kit.css/js`), `assets/`, `logos/`, `quads.json`.
- Motor: `_studio/lib/kit.js` (`K.timeline`, `K.install`, `K.spring`, `K.rng`, `K.matrix3d`, `K.audio`), `kit.css`, GSAP + plugins, `_studio/audio/synth.py`, `_studio/sfx/` + `sfx-analysis.md`, `cues.py`, `preview.py`, `render.py`, `tools/qa.py`, `tools/deliver.py`.
- `refs/brag/step-3-compose.md`, `audio.md`, `refs/investigacion-2026-10.md` (gotchas del motor).

## Salidas
- `index.html` (una escena por beat, ids = nombres del beat sheet), `music.py` → `music.wav`, `cues.json`.
- `borrador.mp4` (render rápido) + `qa/contacto.png`, `qa/transiciones.png`, `qa/report.json`, `qa/stills-*.png`.
- `04-build.md` (plantilla abajo) con desviaciones, comandos, QA y espacio para el veredicto del Juez.
- Tras PUERTA 4: `master.mp4` (render final), `entregas/<cliente>-NN-nombre.mp4` + `.jpg` (poster) + `share-copy.txt` (+ `share-copy-variants.md`), tabla "Serie" del perfil actualizada.

## Proceso
1. **Leer el guion completo y el storyboard** antes de escribir código. Copiar la tabla de beats a `04-build.md` como lista de tareas (una escena = una tarea). Anotar los golpes (t exactos) y las ventanas de revelación.
2. **Esqueleto determinista.** `index.html` carga `../../../_studio/lib/…`, `../../marca.js`, el kit del cliente; `#stage` 1080×1920; `window.DURATION` = duración del guion; `K.timeline()` en pausa + `K.install(tl, fnPorCuadro)`; `window.READY = true` solo cuando fuentes e imágenes cargaron. Nada de `requestAnimationFrame`, `Date`, `Math.random()` (usar `K.rng(seed)`), ni CSS transitions/animations.
   - **Idioma de movimiento del cliente:** el kit (`<cliente>-kit.js`) exporta `motion = { ease, easeOut, dur: { quick, std, slow }, enter: 'rise'|'mask'|'scale', overshoot, current }`: una curva para ≈80 % de los tweens, 3 duraciones, un patrón de entrada y una corriente. Se fija en el piloto del cliente y se reusa en todos sus videos.
   - Las piezas que se usan 2 veces pasan a `kit.js`. Ya están (uso en `_studio/README.md`):
     - `K.cut(tl, sale, entra, t, { axis, dir })` en cada costura (registra la costura para `seams.py`);
     - `ease: K.nudgeEase` en los reacomodos;
     - `K.fitText(el, 940)` después de `document.fonts.ready` en ganchos largos;
     - `K.posterize(t, 10)` en el porCuadro para stop-motion.
3. **Marca desde el cuadro 0.** Los elementos del cuadro 0 (sello pequeño, fondo de marca, primera línea del gancho si el guion lo dice) se **colocan con `tl.set(…, 0)`**, no con un tween que arranca en 0. El intro de marca (3–4 s) se construye con el módulo del kit (`B.intro()` o equivalente) y el resto del timeline se corre con `tl.shiftChildren(OFF)` si hace falta.
4. **Una escena por beat, vistiendo el boceto.** Posición, jerarquía y copy vienen de la celda `frame-NN`; el Editor agrega el tratamiento completo (fuentes, fotos reales con máscara orgánica, UI real, profundidad) y el movimiento. Reglas de movimiento (de /brag, HyperFrames y iart, adaptadas):
   - **Easing es emoción.** `.out` al entrar (rápido → se asienta), `.in` al salir (acelera y se va), `.inOut` al moverse entre posiciones. Springs del kit (`K.spring`) para lo que "aterriza"; críticamente amortiguado para cargas que se asientan; nada de rebote exagerado.
   - **Números de entrada, salida y cascada.**
     - Entrada ≤0,8 s (más tiempo = stagger de varios, no un elemento lento). Salida ≈75 % de la entrada. Recorridos largos duran más: 200 px ≈ ×1,3, 400 px ≈ ×1,6.
     - **Un overshoot por video:** `back.out(1.4–1.7)`. Prohibidos `bounce.out` y `elastic.out`. Elementos parecidos comparten ease y duración; la variedad sale de la dirección, la escala y el stagger, no de mezclar curvas.
     - **Nada aparece de la nada:** tarjetas y UI entran desde scale 0,9–0,97 + opacidad (nunca desde 0 ni desde 0,4); solo lo que "vuela" viene de más lejos.
     - **Cascada con peso** (total ≤0,5 s): ancla 60–80 px / 0,16–0,20 s; palabra 40–50 px / 0,13–0,16 s; ligero 30–48 px / 0,10–0,13 s; los espacios se achican (×0,84). GSAP: `stagger: { each, from, ease }` o `gsap.utils.distribute`; nunca `from: 'random'` sin `K.seedRandom`.
     - **Reacomodo (nudge):** 3 tramos — `power3.in` 10 % del camino en 20 % del tiempo, lineal 65 % en 18 %, `power4.out` 25 % en 62 % — o un `CustomEase`. Lo nuevo entra en el tramo rápido.
     - Anticipación de 2–4 cuadros solo en el golpe principal; lo secundario sigue moviéndose 4–8 cuadros después de que para lo principal.
     - La escena más lenta ≈3× la más rápida; no zoom ambiental en todas (pan lento, rotación sutil o nada).
   - **Build / breathe / resolve.** 0–30 % entran (escalonado), 30–70 % fase quieta, 70–100 % salida o final decidido. Las salidas más rápidas que las entradas.
     - **Lo quieto no es relleno.** Si la fase media dura >1,5 s, nómbrale una ruta: revelación por etapas, cámara con intención (general → viaja → llega), UI que vive (progreso, resaltado, conteo), secuencia (algo se archiva) o cursor que lleva el ojo. Un glow que respira solo va como capa encima, nunca como la ruta.
     - **Pausa dramática** de 0,3–0,75 s entre la acción y su resultado. Prueba: pausa en cualquier segundo; algo con sentido tiene que estar a mitad de vuelo.
   - **Jerarquía = orden.** Lo que se mueve primero es lo más importante; stagger total < 0,5 s; con 3+ elementos, no más de ⅓ en movimiento activo a la vez.
   - **Legibilidad manda.** La línea entra rápido y **se queda** el tiempo asentado del guion; el texto secuencial cada 2 beats.
   - **Composición de video, no de web.** Dos focos por escena, tres capas (fondo con tratamiento, contenido, acentos), texto héroe 60–80 % del ancho, anclado a bordes o en zonas, nunca "centrado flotando en vacío"; líneas/conectores solo si unen dos cosas reales.
     - Profundidad por velocidad: fondo 0,2×, medio 0,5×, frente 1×. Contra-movimiento: si el héroe va a la derecha, el fondo va 20–30 % a la izquierda. La sombra llega 1–2 cuadros tarde.
     - Texto con máscara: `SplitText.create(el, { type: 'lines', mask: 'lines' })` después de `document.fonts.ready`, con `yPercent: 140`. Gancho largo: ajustar el ancho a ≤940 px (ver `KORVIN/videos/04-como-funciona/escena.js`).
   - **Fotos siempre con tratamiento**: Ken Burns 1→1,04 en la duración del beat, máscara orgánica del kit, inclinación con `transformPerspective`, marco de dispositivo o `K.matrix3d` sobre la pantalla verde. Nunca una foto plana pegada. Footage: `B.clip()` (cuadros extraídos, deterministas).
   - **Costuras (transiciones).** Cómo sale A dice cómo entra B: mismo eje, misma dirección, misma velocidad, y el corte con las dos a mitad de movimiento. Nunca crossfade entre dos layouts cargados.
     - En Z, la dirección es el signo del scale: si A se encoge, B llega grande (1,25→1); si A crece, B llega chica (0,75→1). Error típico: salir encogiendo y entrar creciendo desde chico.
     - Viaje parcial ≈12 % del cuadro (≈130 px horizontal, ≈230 px vertical). Salida `power4.in` 0,2–0,34 s; entrada `power4.out` ≥ la salida, misma distancia. La opacidad de salida termina antes del corte (≥0,05 s antes si lo que entra es texto, para que no haya doble exposición legible); la de entrada arranca en ≈0,35. Blur máximo: 10 px en texto, 18–20 px en superficies. `#stage` opaco (si no, flash blanco).
     - Una "corriente" por video (la dirección de salida del guion). Los demás vectores se usan con sentido: arriba = conclusión; Z adelante = profundizar; Z atrás = llega algo más grande. Cambiar de dirección pide una causa (un clic, un golpe).
     - Cada costura va en la tabla "Costuras" de `04-build.md`: t · sale (eje, signo, id) · entra · técnica. Si una fila no cuadra, se arregla el plan, no el ease.
   - **Cursor/dedo causa cada cambio** en demos: mover → clic (`cue('click')`) → efecto ≤1 s después.
   - **Audio-reactivo sutil** con `K.audio(t)` → `{rms, low}` para respirar un glow o la presencia de una tarjeta. Nunca barras ni estrobos. El glow va como capa encima de una escena que ya tiene su ruta (ver fase quieta).
5. **Gotchas del motor** (se repiten; comprobar antes del QA): `fromTo` en vez de `from` (immediateRender rompe el seek no lineal); `tl.set` de muerte después de cada salida (`visibility:hidden`) para que un tween posterior no resucite el elemento; un hijo con `visibility:visible` se ve a través del padre oculto; no `will-change` en algo que la cámara escala; no `opacity`/`filter` dentro de `preserve-3d`; `backdrop-filter:url()` falla en Chromium (clonar la escena); dos tweens de transform simultáneos sobre el mismo elemento se pisan (combinar en un `fromTo` o separar padre/hijo); en un loop el último cuadro = el primero; cualquier pulso ambiental va en `tl`, nunca en `gsap.to` suelto.
   - Más gotchas: los valores relativos (`y: '-=60'`) se resuelven en el primer render → usar absolutos en todo lo que se pueda volver a buscar; `overwrite: 'auto'` puede matar tweens en el primer render → no usarlo sin pasar `test/verify.py`; `tl.addLabel` por beat (los tiempos de `04-build.md` salen de `tl.labels`); los colores se interpolan con `gsap.utils.interpolate`.
6. **SFX en el código.** `cue('tipo', t)` en el mismo punto del timeline donde arranca la animación (el sonido entra 0–0,1 s antes). Tipos del guion (pop, tecla, send, whoosh, golpe); el archivo lo elige el Editor en `_studio/sfx/` con `sfx-analysis.md` (pico medido, tonalidad). En secuencias se acentúa el primero, el último o el más fuerte; los repetidos van al fondo.
   - **Dos y medio:** nunca más de 2 SFX distinguibles a la vez encima de la música. Jerarquía: golpe del guion > SFX de causa > música > textura.
   - **Golpe grande = 3 alturas y un pico:** grave (impacto) + medio (whoosh) + agudo (brillo). Riser de 1–3 s → impacto → cola de 1–2 s. `duck_curve` baja la cama en cada golpe.
   - **Familias:** cada SFX repetido tiene versión fuerte (primero o último) y versión de fondo (más corta y más baja) del mismo sonido. Duraciones orientativas: click 0,05–0,1 s · pop 0,1–0,2 · whoosh 0,3–0,6 · impacto 0,3–0,5.
7. **`music.py`.** `sys.path.insert(0, '../../../_studio/audio')`; grilla a 120 BPM; los **golpes del guion** caen en el beat exacto (kick/impact + cambio armónico); la cama sigue el arco del brief (entra la güira en el giro, baja en el cierre, nota final en el último golpe); SFX colocados por su pico medido, en la misma tonalidad y espacio que la música; `intro_mix()` si hay intro de marca; `master_lufs(-14)` con true peak ≤ -1 dBTP; `export_rms()` si hay audio-reactivo. Fade final ~0,8 s salvo que el guion termine en golpe seco.
8. **Comandos** (desde `<CLIENTE>/videos/NN-nombre/`):
   ```bash
   python ../../../_studio/cues.py index.html cues.json
   python music.py
   python ../../../_studio/preview.py index.html qa/stills-beats.png 0,0.5,2.5,3.5,6,9,13.5,16,18,21.5     # un t por beat
   python ../../../_studio/preview.py index.html qa/stills-trans.png 3.4,3.6,8.9,9.1,...                # ±0,1 s de cada corte
   python ../../../_studio/render.py --html index.html --out borrador.mp4 --w 1080 --h 1920 --fps 30 --sub 1 --workers 8 --audio music.wav   # borrador sin motion blur (si render.py tiene --draft, usarlo)
   python ../../../_studio/tools/qa.py --video borrador.mp4 --html index.html --out qa [--safe 270,1250,950,900,1700 si uso: ad]
   ```
9. **Autorrevisión con las hojas** (antes del Juez): `qa/contacto.png` (1 cuadro/s) y `qa/transiciones.png` (los 16 cuadros de más cambio): ¿cuadro 0 con marca? ¿gancho legible a 1,5 s? ¿texto cortado, solapes, doble exposición a mitad de transición? ¿algún cuadro "no publicable"? ¿pops de un cuadro? Corregir y repetir hasta que `qa.py` dé PASS (los WARN se justifican en `04-build.md` o se corrigen).
   - **"Tells" de diseño generado** (mirar antes del Juez): eyebrow en mayúsculas en todo, "A · B · C" en todas partes, una palabra de color en cada titular, tarjetas iguales con la misma sombra, el mismo fade+slide en todas las entradas. ¿Cuál es la única cosa memorable de la escena? Quita un accesorio.
   - **Cuadros dorados:** tras el primer PASS, `python ../../../_studio/tools/golden.py --html index.html --out qa/golden --save` (un PNG por cada `tl.addLabel`; `--times` para elegir, `--scale 0.5` para ir rápido). En cada vuelta del Juez: `--compare` (deja `diff-<t>.png` y `compare.json`; `--allow <label>` para lo que sí se tocó). Lo que no se tocó, no cambió.
   - **Costuras medidas:** después de `qa.py` y antes del Juez, correr `python ../../../_studio/tools/seams.py --html index.html` (escribe `qa/seams.json`).
     - Mide con Playwright cada costura de `window.SEAMS`: el `getBoundingClientRect` del que sale y del que entra en t ± 1/30 s. Pide los dos en movimiento, mismo eje y signo, nunca los dos legibles a la vez.
     - Las de `K.cut` se registran solas. Una costura hecha a mano se agrega con `window.SEAMS.push({ t, out, in, axis, dir })`. Debe quedar una por fila de la tabla Costuras.
     - Un FAIL bloquea: se arregla la costura y se vuelve a correr.
10. **`04-build.md`**: desviaciones del guion (beat, qué cambió, por qué), comandos reales, resumen numérico del QA, tiempos finales por beat (regenerados desde el código), pendientes. Estado `listo-para-juez`.
11. **PUERTA 3 = `qa.py` PASS + Juez.** Lanzar el Juez como subagente con contexto limpio (ver `rol-juez.md`). Corregir **solo los P0** (y los P1 baratos); máximo 2 vueltas; registrar cada vuelta. Si tras 2 vueltas sigue habiendo P0, se para y se le cuenta a Yeyow con la hoja de contacto.
12. **PUERTA 4 (Yeyow).** Presentar `borrador.mp4` + `qa/contacto.png` + los 3–5 timestamps que vale la pena mirar + la ficha del Juez. Las notas de Yeyow van a `05-revision.md` (textuales, con timestamp). Clasificar cada nota: *revisión* (algo ya aprobado: timing, color de la paleta, copy aprobado, bug) → se hace; *petición nueva* (escena nueva, +duración, concepto nuevo, otro formato) → vuelve a PUERTA 1/2 con nota, no se absorbe en silencio; *vaga* ("más punch") → se traduce a opción acotada con timestamp antes de tocar nada.
13. **Final.** Con APROBADO en `05-revision.md`: render final `--sub 4` en la misma máquina; `qa.py` otra vez; `deliver.py --video master.mp4 --poster-t <poster_t> --out ../../entregas/<cliente>-NN-nombre.mp4` (hornea el poster como cuadro 0 y respeta el tope de 20 MB); `share-copy.txt` al lado; actualizar la tabla "Serie" del perfil (estado, carpeta, fecha) y la tabla **Huella** (receta · mecánica · técnica firma con IDs de `refs/tendencias.md` · transiciones con IDs · contenido del gancho). Si el video usó una técnica `nueva`, en `tendencias.md` pasa a `probada` con el video en "Usado en". Si mientras editabas usaste o encontraste una técnica que no está en el catálogo, agrégala como `nueva` con su fuente y "cómo se hace en nuestro motor". Si ya hay una `v1` entregada, la nueva es `-v2` (nunca se sobreescribe la entregada).

## Checklist de "listo" (antes de llamar al Juez)
- [ ] Todo sale de `window.seek(t)`; sin rAF/Date/Math.random/CSS animations; `READY` espera fuentes e imágenes.
- [ ] Cuadro 0 con marca visible (sello/logo) y sin negro; intro de marca 3–4 s según guion.
- [ ] Una escena por beat con el id del beat sheet; layout = celda del storyboard (vestida, no redibujada).
- [ ] Textos verbatim del guion; cero texto no aprobado; etiquetas EJEMPLO / Imágenes conceptuales / DATOS DE DEMOSTRACIÓN donde el guion lo dice.
- [ ] Tiempos asentados ≥ los del guion; texto secuencial cada 2 beats.
- [ ] Golpes en los beats exactos del guion (`cues.json` y `music.py` coinciden); SFX 0–0,1 s antes de su animación; mismo tono/espacio.
- [ ] `fromTo` (no `from`), `set` de muerte tras salidas, pulsos en `tl`, sin transforms que se pisen, sin `will-change`/`preserve-3d`+filter.
- [ ] Transiciones: lo viejo sale, lo nuevo entra; una dirección; sin crossfade de layouts cargados; velocity-matched.
- [ ] Fotos con tratamiento; UI real o recreada del código/capturas; nada de partículas, confeti, neón, temblor, rebote exagerado, glassmorphism en todo.
- [ ] `qa.py` PASS: duración = `window.DURATION`, ≤19,5 MB, -14 LUFS ±3, TP ≤ -1 dBTP, quietos ≥6 %, CV ≥0,25, 0 pops, 0 texto fuera de zona (según `uso`).
- [ ] Hojas revisadas a ojo: cada escena y cada mitad de transición es publicable.
- [ ] `04-build.md` con desviaciones, comandos, QA, tiempos finales; estado `listo-para-juez`.

## Plantilla — `04-build.md`
````markdown
---
cliente: PANADERIA-EJEMPLO
video: 03-de-tu-idea
version_guion: 2
vuelta: 1                      # vueltas con el Juez (máx. 2)
estado: listo-para-juez        # construyendo | listo-para-juez | cambios-juez | listo-para-yeyow | aprobado | entregado
qa: PASS con avisos            # salida de qa.py
juez: pendiente                # APROBADO | CAMBIOS | RECHAZADO
maquina_render: "PC Yeyow (Windows)"
---

## 1. Escenas construidas (del beat sheet)
| # · nombre | t guion | t real | Estado | Nota |
|---|---|---|---|---|

## 1b. Costuras
| t | Sale (eje, signo, id) | Entra (eje, signo, id) | Técnica |
|---|---|---|---|

## 2. Desviaciones del guion
| Beat | Qué cambió | Por qué | ¿Vuelve al Guionista? |
|---|---|---|---|

## 3. Comandos para reproducir
```bash
…
```

## 4. QA (qa/report.json)
- Duración … s · 1080×1920 · … MB · quietos … % · cortes … · CV … · pops … · … LUFS / … dBTP · texto fuera de zona: …
- WARN justificados: …
- Hojas: qa/contacto.png · qa/transiciones.png · qa/stills-beats.png · qa/stills-trans.png

## 5. Línea de verdad (verificada en el video)
- Real: … · EJEMPLO: … · Etiquetas presentes en t=…

## 6. Veredicto del Juez (lo escribe el Juez)
### Vuelta 1 — dd/mm
| # | Sev | t | Criterio | Problema | Evidencia (conf.) | Sugerencia |
|---|---|---|---|---|---|---|
Veredicto: … · Lo que se arregló: … · Lo que se dejó y por qué: …

## 7. Pendientes / para Yeyow (PUERTA 4)
- Timestamps que vale la pena mirar: …
- Preguntas abiertas: …

## 8. Entrega (tras 05-revision.md APROBADO)
- master.mp4 (… s, … MB) → entregas/…mp4 + .jpg (poster t=…) + share-copy.txt · perfil § Serie y Huella actualizados dd/mm · tendencias.md: <IDs que pasaron a probada>
````

## Errores comunes
- Redibujar el layout aprobado "porque quedaba mejor". → Vestir la celda; proponer el cambio en `04-build.md`.
- Empezar todo en t=0 con tweens (cuadro 0 vacío o a medio entrar). → `set` en 0 para lo que debe estar en el cuadro 0; el primer movimiento a los 0,1–0,2 s.
- Mismo ease, misma duración, misma dirección en todo (`power2.out`, 0,4 s, `y:30`).
- Crossfade entre dos escenas llenas → doble exposición en `transiciones.png`.
- `gsap.from` o pulsos con `gsap.to` sueltos → no se ven en el render aunque se vean en el navegador.
- Texto que se revela a cada beat (0,5 s) porque "sigue la música".
- Inventar un texto de UI "para rellenar" (un precio, una respuesta del bot). → Solo lo del guion/afirmaciones permitidas.
- SFX pegados encima de la música (otra tonalidad, otro espacio), o un whoosh en cada corte.
- Render final en otra máquina o sin volver a correr `qa.py`.
- Absorber en silencio una petición nueva de Yeyow en PUERTA 4 (escena nueva, +5 s). → Clasificarla y volver a la puerta que corresponde.
- Entregar sin poster horneado o sin `share-copy.txt`.

## Qué le pasa al Juez y a Yeyow
Al **Juez**: `borrador.mp4`, `qa/report.json`, `qa/contacto.png`, `qa/transiciones.png`, `qa/seams.json` (y `qa/golden/compare.json` desde la vuelta 2), `02-brief.md`, `03-guion.md`, `perfil.md`, `04-build.md` §1–5. Nada más (sin el chat del Editor, sin el código salvo que el Juez lo pida para un P0).
A **Yeyow** (PUERTA 4): `borrador.mp4`, `qa/contacto.png`, los timestamps clave y la ficha del Juez; sus notas van a `05-revision.md` con el veredicto APROBADO / CAMBIOS / DESCARTADO.

## Lecciones de Korvin #4 (03/10/2026)
- **Texto escondido con máscara:** usa `yPercent: 140` (no 110). Con 110, las tildes de Í/Ó/Á asoman arriba de la línea.
- **Estados iniciales:** todo elemento que se anima más de una vez lleva `gsap.set` en el cuadro 0 y `fromTo(..., { immediateRender: false })` (helper `F`). Una capa que se enciende tarde (el cierre) necesita `gsap.set` de sus hijos; si no, aparecen antes de su tween.
- **Sin doble exposición:** lo que sale termina ≥0,05 s antes de que entre el texto siguiente. El Juez lo agarra en `transiciones.png` (pasó en 19,75 s).
- **Flash de golpe:** ≤0,1 sobre fondo oscuro; con 0,3 el cuadro entero se ve gris.
- **Ganchos largos:** mide la línea y ajústala a ≤940 px (`#q1` en `KORVIN/videos/04-como-funciona/escena.js`).
- **Un video en varias versiones:** una escena (`escena.js/.css`) + datos (`versiones.js`) + un `index-<version>.html` + `music.py <version>`. La primera versión es el piloto; las demás se construyen cuando el piloto está aprobado.
- **Tiempos en Cowork (2 núcleos):** borrador de 26 s ≈95 s; final de 26 s ≈8,5 min; `deliver.py` ≈80 s.
- **Textos de la UI del producto:** cópialos del código con su ruta y línea, y marca en `versiones.js` cuáles son REAL. La respuesta "libre" de la IA va como EJEMPLO y solo con datos que se vean en pantalla (Cerebro).

## Fuentes de las mejoras v2 (research de marketplaces, 03/10/2026)
Detalle, licencias y lo descartado: `research-2/rol-editor-propuestas.md`. Ideas tomadas (reescritas) de: heygen-com/hyperframes `.claude/skills` (`motion-doctrine`, `cut-the-curve`, `seam-craft`) y `hyperframes-animation/rules` (Apache-2.0), greensock/gsap-skills (MIT), emilkowalski/skills (MIT), lottiefiles/motion-design-skill (MIT), anthropics/claude-plugins-official `frontend-design` (Apache-2.0), clawfu-skills `sound-design-film` (MIT), dylantarre/animation-principles (MIT), jeremylongshore `testing-visual-regression` (MIT). Remotion solo como idea (`fitText`, `posterize`); no se usa.
