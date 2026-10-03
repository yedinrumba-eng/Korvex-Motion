# Propuestas para el rol Guionista — research en marketplaces (03/10/2026)

Solo propuestas; no se tocó el método. No se repiten las fuentes del 02/10 (HyperFrames, iart, marketingskills). Caso de prueba: `KORVIN/videos/04-como-funciona/03-guion.md` (el Juez marcó "MIRA CÓMO CONTESTA" ≈0,5 s, P0, y el resumen 1,6 s, P1).

## 1. Skills revisadas

| Skill | Repo / marketplace | Lic. | Qué hace | Veredicto |
|---|---|---|---|---|
| `hooksmith` (generate · audit · rehook · caption) | [arhamhi/hooksmith](https://github.com/arhamhi/hooksmith) · claudskills.com | MIT | "Sistema de gancho": texto + loop abierto + re-gancho a los 3–10 s + pago; anti-patrones; caption como segundo gancho | **Adoptar** (la más útil) |
| `hook-writing` · `hook-tactics` · `hook-voice-patterns` | [motion-creative/skills](https://github.com/motion-creative/skills) | MIT | 8 disparadores, 35 tácticas, swipe file; "varía el disparador, no la redacción" | **Adoptar** la regla de variantes; templates en inglés, no |
| `motion-picture` + `script-writer-skill` | [firatcand/founder-skills](https://github.com/firatcand/founder-skills) | MIT | Tipografía en motion: "leer dos veces", desfase entre niveles, escala ≥1,5×, un texto en movimiento a la vez | **Adoptar** § tipografía; cifras no |
| `vsl-storyboard-writer` | [ncklrs/startup-os-skills](https://github.com/ncklrs/startup-os-skills) | MIT (README; sin LICENSE) | Densidad palabras/duración, pausa tras afirmación, tiempos FIJO/FLEXIBLE, jerarquía PRIMARIO/SECUNDARIO | **Adoptar** parcial (es para VSL largos) |
| `humanizer` v3.1 | [blader/humanizer](https://github.com/blader/humanizer) | MIT | 26 muletillas de IA por fuerza; "aplica en cualquier idioma" | **Adoptar** la lista |
| `storyboard` · `frame-qa` | [kennykankush/skillpack](https://github.com/kennykankush/skillpack) | MIT | Bocetos por imagegen; etiquetas `keep / keep with note / regenerate / optional / replace narrative`; ritmo denso→quieto | **Adoptar** etiquetas y ritmo; IA no |
| `creative-review-gate` · `short-form-video-production` | [S3YED/appie-kit](https://github.com/S3YED/appie-kit) | MIT | "Review pack": cerrado / abierto / no sigo hasta tu OK; una palabra resaltada por frase | **Adoptar** el review pack |
| `social-content-engine` + `shared/voice-profile.md` | [knowledge-work-plugins/small-business](https://github.com/anthropics/knowledge-work-plugins) (instalado) | Apache-2.0 | Perfil de voz desde mensajes reales del dueño; caption = gancho + beneficio + CTA + 3–5 hashtags | **Adoptar** el perfil de voz |
| `create-shortform` · `scriptwriting` | [hungv47/meta-skills](https://github.com/hungv47/meta-skills) · [gtmagents/gtm-agents](https://github.com/gtmagents/gtm-agents) | MIT · Apache-2.0 | "Un recorte no es una versión"; "planea las variantes desde el inicio" | Ideas menores |
| `reel-script-writer` · `explainer-video-scripter` | [eddiebelaval/squire](https://github.com/eddiebelaval/squire) | MIT | Plantilla vacía ("Discovery → Planning → Execution") | **Descartar** |
| `content/video` · `draft-content` · `content-creation` | [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) · knowledge-work-plugins/marketing (instalado) | MIT · Apache-2.0 | Estructura genérica con cifras sin fuente; blog/SEO/landing | **Descartar** |
| `reels-scripting` · `content-quality-editor` · `create-hook-variant-pack` | charlie947 · VoltAgent · gooseworks-ai | no vista / MIT / no vista | Voz en inglés; limpiador en inglés; andamio vacío | Descartar |

## 2. Mejoras concretas al rol de hoy

### 2.1 Gancho: elegir el trabajo y hacer 3 variantes
**Brecha:** § 2 da la gramática pero no pide elegir qué hace el gancho ni variantes; en PUERTA 2 se presenta uno solo.
**Pegar al final de § 2:**
```
- Antes de la línea, elige UN trabajo del gancho: reconocerse · pregunta abierta · lo que está en juego ·
  romper una creencia · validar sin culpar · puente a la demo.
- Para PUERTA 2, 3 ganchos con trabajos distintos (no 3 redacciones de lo mismo). Yeyow elige uno; los otros
  van a share-copy-variants.md como gancho B.
- Prueba del relleno: borra la segunda línea; si el gancho sigue, era relleno.
- Una pregunta solo vale con dato: "¿Te mandan notas de voz pidiendo precio?" sí; "¿Quieres vender más?" no.
- Nunca acusar al espectador ni abrir con metadatos de serie ("Parte 2"): eso va en etiqueta pequeña.
```
**Fuente:** hooksmith `hook-frameworks.md`, `command-generate.md`, `anti-patterns.md`; motion-creative `hook-writing`.

### 2.2 Re-gancho entre 3 y 10 s
**Brecha:** § 3 pide el mensaje en el beat 2, pero nada exige renovar la atención en la rampa.
**Pegar en § 7:**
```
- Re-gancho: entre 3 y 10 s hay un cambio que renueva la atención Y conecta con la pregunta del gancho
  (contradicción, condición que faltaba, cambio de escena, del dicho al ejemplo: entra la UI real).
  Va en la fila como `regancho: <qué cambia>`. Sorpresa sin relación con el gancho no cuenta.
```
**Fuente:** hooksmith `command-rehook.md`; founder-skills `motion-picture` § 5.4 (orientativo).

### 2.3 Texto en pantalla sin voz: densidad y jerarquía
**Brecha:** § 5 calcula el mínimo por línea, pero no limita palabras por beat ni ordena dos textos que conviven ("1 ESCUCHA" + "Le llega una nota de voz.").
**Pegar después de la tabla de § 5:**
```
- Tope de palabras por beat (0,3 s/palabra menos 0,5 s de entrada/salida): 1,5 s → 3 · 2 s → 5 · 2,5 s → 6 ·
  3 s → 8 · 4 s → 10 (tope). Más: otro beat o menos texto.
- Jerarquía en "Se lee": PRINCIPAL / SECUNDARIO / DETALLE. El principal entra primero; el secundario 0,15–0,3 s
  después; escala ≥1,5×. Nunca dos textos del mismo nivel moviéndose a la vez.
- Una palabra resaltada por frase, máximo, cuando la línea ya asentó.
- Prueba de leer dos veces: si no la lees dos veces mientras está asentada, acórtala o alarga el beat.
```
**Fuente:** founder-skills `motion-picture/knowledge-base.md` § 3; vsl-storyboard-writer `script-pacing.md`; appie-kit `short-form-video-production`.

### 2.4 Tiempo de lectura que el Juez no marque
**Brecha:** la tabla de § 5 admite "≈"; en Korvin 04 las entradas y salidas del build se comieron 0,3–0,6 s por línea (P0 #3, P1 #4). § 14 lo detecta cuando ya cuesta arreglar.
**Pegar en § 5 y en el checklist:**
```
- Ningún "≈". Si una línea no llega al mínimo, se acorta o se alarga el beat ANTES de PUERTA 2.
- Reserva: asentado planificado = mínimo + 0,3 s (entradas y salidas siempre comen tiempo).
- Cada beat se marca FIJO (gancho, golpes, CTA, beat quieto) o FLEXIBLE ±0,5 s, con beat donante
  ("si ACTÚA no cabe, toma 0,5 s de RESUMEN"). El Editor ajusta sin volver al Guionista.
- Tras la línea del mensaje y la del resultado, 1 beat sin texto nuevo.
- Con versiones, el mínimo lo fija la línea más larga de todas (2.5).
```
**Fuente:** vsl-storyboard-writer `motion-designer-handoff.md` (FIXED/FLEXIBLE), `script-pacing.md`; `04-build.md`.

### 2.5 Versiones y series: sección propia
**Brecha:** la plantilla no tiene dónde escribir versiones; en Korvin 04 quedaron en una línea de § 12 y la tabla de tiempos solo cubre 04a.
**Pegar como "3b. Versiones" en la plantilla:**
```
## 3b. Versiones (si el brief las pide)
| Campo (clave de versiones.js) | 04a | 04b | 04c | Palabras máx. | Quién confirma |
- Por versión cambian DATOS (textos, chips, filas, final real), nunca estructura, tiempos ni golpes. Otro orden
  de beats = otro video.
- Cada versión tiene fila en la tabla de tiempos (gancho, transcripción, subtítulos, final) y su propia línea
  de verdad (rent-a-car: "la disponibilidad la confirma tu equipo").
- Un cambio por versión. Un recorte (otra duración o formato) no es versión: pide su gancho y su CTA.
```
**Fuente:** `versiones.js` y `02-brief.md` § 4 de Korvin 04; meta-skills `create-shortform`; gtm-agents `scriptwriting`.

### 2.6 Copy en español dominicano natural
**Brecha:** § 6 prohíbe muletillas pero no dice de dónde sale la voz del cliente ni cómo se valida un dominicanismo.
**Pegar en § 6:**
```
- Voz del cliente: lee `perfil.md § Voz`. Si no existe, el Investigador la arma con 10–20 mensajes reales del
  dueño a sus clientes: saludo, cierre, cómo llama a su servicio, palabras que nunca usa.
- La palabra del espectador, no la del experto: "te mandan notas de voz", no "mensajes de audio entrantes".
- Dominicanismos: solo los que ya usa el cliente o están en el Diccionario del español dominicano
  (ADL/Igalex, 2.ª ed., en línea). Nada inventado ni de otro país.
- Más prohibidas: filas de fragmentos ("Sin filas. Sin esperas. Sin excusas."), una palabra en MAYÚSCULAS
  como golpe, "X = Y", "la realidad es que…", "seamos honestos", tríadas forzadas, superlativos sin dato.
- Excepción: en pantalla, un fragmento corto con dato es legítimo ("5 pasos."). La regla completa es para el
  caption y el copy de redes.
```
**Fuente:** blader/humanizer § 1–4, 6, 12–16; `small-business/shared/voice-profile.md`; hooksmith `text-hook-templates.md`; DED 2.ª ed. (prensa: acento.com.do).

### 2.7 Storyboard para aprobar desde el teléfono
**Brecha:** § 13 captura a 1440 px en cuadrícula: en WhatsApp se ve chico. § 14 pide "di el número del beat" sin vocabulario ni decir qué está cerrado.
**Pegar en § 13 y en "Cómo se presenta la PUERTA 2":**
```
- Además de bocetos.png, exporta qa/bocetos-tel.png: una columna, celdas de 540 px, etiqueta debajo
  (`playwright screenshot --full-page --viewport-size "600,<alto>"`). Más de 12 celdas: 3 imágenes de 4.
- Ritmo: celda densa (UI, chat) seguida de una quieta (marca, reacción, confirmación). Tres seguidas iguales
  = un beat de más o de menos.
- Dos líneas más: "Cerrado (del brief): mensaje, receta, duración." · "Abierto para ti: beats <n>, CTA, gancho A/B/C."
- Respuesta por celda: `va` · `va con nota: <qué>` · `cambia: <qué>` · `sobra` · `el beat está mal` (vuelve a PUERTA 1).
```
**Fuente:** skillpack `frame-qa` y `storyboard`; appie-kit `creative-review-gate`.

### 2.8 Caption como segundo gancho
**Brecha:** § 12 pide "1–3 frases"; el share-copy de Korvin 04 repite el video.
**Pegar en § 12:**
```
- El caption no repite el gancho ni resume. Hace UN trabajo: segunda pregunta, el dato que el video no dio
  (qué incluye la demo), razón para guardar, o el mecanismo.
- Primera línea ≤8 palabras (lo que se ve antes de "más").
- CTA de comentario solo si hay algo que mandar y quien lo atienda: "Comenta DEMO y te escribimos".
  Prohibido "sígueme para más". 3–5 hashtags del perfil.
- En share-copy.txt van juntos: gancho elegido + caption + palabra de comentario.
```
**Fuente:** hooksmith `command-caption.md`; `social-content-engine` paso 8.

## 3. Lo que NO conviene adoptar
- **Rúbrica de 50 puntos (hooksmith):** el Juez ya tiene 9 criterios y P0/P1/P2.
- **Swipe files en inglés** (hook-voice-patterns): voz de creador a cámara. Sí la idea: un `ganchos-swipe.md` por cliente con reels medidos en RD.
- **Etapas de conciencia de Schwartz:** para ads segmentados; en orgánico la fija el Productor con el mensaje.
- **"Palabras ÷ 3 + 1" y mínimo 3 s por escena** (vsl): en 20 s deja 6 beats. Mantenemos 0,3 s/palabra + reserva.
- **Bocetos por IA** (skillpack): rompe fuentes/colores reales y la línea de verdad.
- **Zonas seguras y cifras de retención** (appie-kit, founder-skills, kostja94): sin fuente primaria; lo nuestro está en `00-RESUMEN.md` § 9–10.
- **Guion hablado** (script-writer-skill, ugc-scriptwriter) y **plantillas vacías** (squire, gtm-agents, draft-content): lo primero solo si entra voz en off; lo segundo mete ruido sin enseñar nada.

## 4. No verificado
- `ncklrs/startup-os-skills`: README dice MIT, el clon no trae LICENSE. Reescribir, no copiar.
- `charlie947`, `gooseworks-ai`, `postplusai`: solo la ficha del marketplace, sin licencia visible; `video-shotcraft` sigue sin clonarse. `gh api` dio 403; todo se leyó con `git clone --depth 1` en `scratchpad/repos2/`.
- Desfase 4–8 cuadros y escala 1,5× (founder-skills): práctica de diseño, no estudio; orientativos.
- Diccionario del español dominicano en línea: confirmado por prensa (acento.com.do), no se abrió la consulta. Guardar la URL antes de usarlo como regla.
