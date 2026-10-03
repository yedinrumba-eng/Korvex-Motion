---
cliente: {{CLIENTE}}
video: {{VIDEO}}
version: 1
aprobado: false
aprobado_por:                 # solo "Yeyow", y solo con sus palabras (/korvex-motion:aprobar)
fecha_aprobacion:
mensaje:    # ej.: "Pedir una cotización es contar tu ocasión; tú decides si envías."
audiencia:    # ej.: "…"
receta:    # ej.: explainer-5-escenas
arco:    # ej.: demo-loop
tono:             # pero no: juguetón, pero no infantil
duracion:    # ej.: 26
bpm: 120
poster_t:    # ej.: 5.2
direccion_salida:    # ej.: izquierda
beat_quieto:    # ej.: 6
---

## 1. Gancho (0–3,5 s) — tres componentes
- Acción visual: …
- Texto en pantalla: "…"
- Sonido: …
- Marca: sello visible desde el cuadro 0 (<posición>); marca al centro en t=2,5 (golpe).

## 2. Líneas y tiempos de lectura
| Línea (verbatim) | Nivel (PRINCIPAL/SECUNDARIO/DETALLE) | Palabras | Mínimo (s) | Asentada (s) = mínimo + 0,3 | ✓ (sin "≈") |
|---|---|---|---|---|---|

## 3. Beat sheet (120 BPM · beat 0,5 s · compás 2 s)
| # · nombre | t · compás | tipo · persuasión · emoción | Se ve | Se lee | Se mueve / quieto | Se carga al siguiente | Audio | Cámara · salida | Restricción | Por qué |
|---|---|---|---|---|---|---|---|---|---|---|
Suma de duraciones: … s (objetivo … s). Cada fila: FIJO o FLEXIBLE (con beat donante); entre 3 y 10 s, `regancho:`.

## 3b. Versiones (si el brief las pide)
| Campo (clave de versiones.js) | 04a | 04b | Palabras máx. | Quién confirma |
|---|---|---|---|---|

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
