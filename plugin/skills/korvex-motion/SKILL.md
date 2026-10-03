---
name: korvex-motion
description: Crea contenido de motion graphics (reels, ads, launches, explainers, testimonios, promos) para cualquier cliente o producto de Yeyow con el flujo spec-driven de Korvex Motion. Primero hace preguntas (intake), después pasa por investigador → productor (brief, PUERTA 1) → guionista (guion + bocetos, PUERTA 2) → editor + QA + juez → aprobación de Yeyow (PUERTA 4) → entrega. Úsalo con /korvex-motion o cuando Yeyow diga "vamos a crear contenido para…", "hazme un reel/video/ad de…" o "un motion de…".
---

# Korvex Motion: de la idea al reel, con puertas

Úsalo cuando Yeyow quiera contenido de motion graphics de un cliente o producto: Korvin (el producto de Korvex Dev) o cualquier cliente nuevo. Funciona igual en Claude Code (en su PC) y en Cowork. Lo que cambia es dónde corren los comandos (ver "Dónde corre").

**Estudio:** la carpeta de este repo (en Cowork, la carpeta conectada). Las rutas de abajo son relativas a esa carpeta.
- `README.md`: cómo funciona todo.
- `PRODUCTOS.md`: índice de clientes.
- `CLAUDE.md`: reglas de la sesión.
- `_studio/metodo/`: el método completo de cada rol. **Léelo, no lo improvises.** Contiene `intake-preguntas.md`, `categorias.md`, `recetas.md`, `rol-investigador.md`, `rol-productor.md`, `rol-guionista.md`, `rol-editor.md`, `rol-juez.md`, `juez-casos.md` (casos de calibración del Juez), `00-RESUMEN.md` (fuentes) y `research-2/` (research de marketplaces del 03/10/2026 que dio el método v2).
- `_studio/plantillas/`: plantillas 01–05 de los documentos.
- El motor (render, kit, audio, QA) está en `_studio/README.md` y en el skill `motion-studio`.

## Reglas que no se negocian
1. **Una carpeta por cliente.** Todo sale de `<CLIENTE>/perfil.md` (fuente de verdad), `marca.js`, `logos/` y `assets/`. Nunca se mezcla nada con otro cliente.
2. **No inventar.**
   - Nada de funciones, cifras, clientes, testimonios ni precios que no estén en el perfil, en la web/código del cliente o en palabras de Yeyow.
   - Las fotos generadas llevan "Imágenes conceptuales" y los datos de ejemplo "EJEMPLO" / "DATOS DE DEMOSTRACIÓN".
3. **Marca desde el cuadro 0.** Desde que empieza se sabe de quién es. Logo visible en el primer cuadro + intro de marca de ~3–4 s que a la vez es el gancho (receta R1: preguntas de ocasión/dolor → logo + nombre). Pedido de Yeyow, 02/10/2026.
4. **Puertas.** Ningún rol se salta una puerta. Las aprobaciones son de Yeyow, con sus palabras: tú **nunca** escribes `aprobado: true` ni `veredicto_yeyow: APROBADO` por tu cuenta.
5. **Un video, una idea.** Si salen dos mensajes, son dos videos.

## El flujo
```
/korvex-motion <idea o referencia>
 0. Ubicar el cliente ─ perfil.md (si es nuevo: /korvex-motion:nuevo-cliente)
 1. INTAKE (tú, en la conversación) ─ preguntas con opciones → resumen "Lo que dijiste / Lo que inferí"
 2. Investigador ─► 01-research.md
 3. Productor ────► 02-brief.md ............ PUERTA 1 (Yeyow aprueba brief + concepto)
 4. Guionista ────► 03-guion.md + bocetos .. PUERTA 2 (Yeyow aprueba guion + storyboard)
 5. Editor ───────► index.html + music.py → borrador (--draft) → qa.py → Juez ... PUERTA 3 (automática)
 6. Yeyow ────────► 05-revision.md ......... PUERTA 4 (APROBADO / CAMBIOS / DESCARTADO)
 7. Final ────────► render completo → deliver.py → qa.py → entregas/ + share-copy + perfil + PRODUCTOS.md
```

### 0. Ubicar el cliente
- Busca la carpeta del cliente (por ejemplo `KORVIN/` o `PANADERIA-EJEMPLO/`) y lee **todo** su `perfil.md`: funciones, lo que NO se dice, marca, assets, copy aprobado y serie.
- Si Yeyow da una ruta o una referencia ("el proyecto está en C:\ruta\X", un enlace), esa es la fuente del investigador. Es de **solo lectura**: nunca se modifica el proyecto del cliente.
- Si el cliente no existe, sigue `/korvex-motion:nuevo-cliente` antes de seguir.

### 1. Intake: SIEMPRE, antes de investigar
Sigue `_studio/metodo/intake-preguntas.md` al pie de la letra:
- **Rondas:**
  - Ronda 1: cliente, categoría/propósito, audiencia y uso (orgánico o ad).
  - Ronda 2: duración, CTA, fecha y referencias.
  - Ronda 3: solo lo que el perfil no responda.
  - Al final, las extras de la categoría.
- **Formato de las preguntas:** ≤4 por ronda, cada una con 2–4 opciones y **la recomendada primero con su razón**. Usa la herramienta de preguntas con opciones si existe (AskUserQuestion); si no, en texto con A/B/C.
- **No preguntes lo que el perfil o la idea ya responden.** Va como "inferido, con recibo".
- **Categorías** (detalle en `categorias.md`; ofrece las 3 más probables):
  1. Lanzamiento
  2. Marketing / ad de conversión
  3. Educativo / explainer
  4. Marca / awareness
  5. Testimonio
  6. Escenario / caso de uso
  7. Demo de función
  8. Evento / promo
  9. Contenido de valor / tips
  10. Reclutamiento / comunidad
- **Modo de revisión:**
  - Completo: 3 puertas con bocetos (por defecto para un concepto nuevo).
  - Rápido: sin bocetos.
  - Autónomo: solo apruebas el borrador; sirve para repetir una receta ya aprobada.
- **Cierre:** "Lo que dijiste / Lo que inferí / Chequeo de integración" + una sola pregunta ("¿Arranco?").
- **Al confirmar:**
  1. `python _studio/tools/nuevo_video.py <CLIENTE> "<nombre-corto>" --idea "<idea>"` crea `videos/NN-nombre/` con 01–05.
  2. Escribe el intake en la §1 de `01-research.md`.

### 2. Investigador → `01-research.md`
- **Claude Code:** delega al subagente `investigador` y pásale la ruta del video y del perfil.
- **Cowork:** hazlo tú siguiendo `rol-investigador.md`.
- **Contenido:** hechos con fuente, flujo real con los textos exactos de pantalla, frases verbatim del cliente, lo que NO se dice, 2–3 referencias **medidas** (qa.py sirve para medir una referencia), antipatrón, assets con licencia, audio, plataforma y riesgos.
- **Apify por defecto** (Yeyow, 03/10/2026): métricas públicas de ≤3 cuentas para las referencias.
- **Radar dentro del research:** si `_studio/refs/tendencias.md` tiene más de 30 días, el Investigador lo actualiza en ese momento (fuentes fijas + Apify). § 0 trae 2–3 técnicas candidatas distintas del look actual del cliente.

### 3. Productor → `02-brief.md` → PUERTA 1
- **Claude Code:** subagente `productor`.
- **Rotación del look** (paso 3b de `rol-productor.md`): repetir gancho, receta o método se vale. Lo que rota es la secuencia de edición de cada cliente (técnica firma, transiciones, forma del motion): hasta 3–4 videos seguidos con el mismo look y después cambia. La tabla **Huella** del perfil es el registro.
- **Contenido:**
  - Frase Get/Who/To/By y UN mensaje.
  - Si la idea no está formada, ronda de pitch: 3–5 conceptos, ≥2 atípicos.
  - Receta de `recetas.md`, afirmaciones permitidas con fuente y criterios medibles.
- **PUERTA 1:** preséntalo como propuesta en el chat (formato de `rol-productor.md`) y **para**. Espera la decisión de Yeyow.

### 4. Guionista → `03-guion.md` + `storyboard.html` → PUERTA 2
- **Claude Code:** subagente `guionista`.
- **Contenido:**
  - Gancho de 3 componentes (visual, texto, sonido).
  - Beat sheet a 120 BPM con "qué se carga al siguiente" y un beat quieto.
  - Golpes, tiempos de lectura, poster, copy y línea de verdad.
  - Bocetos estáticos con la marca real → `python _studio/preview.py storyboard.html qa/bocetos.png …`.
- **PUERTA 2:** presenta y **para**.

### 5. Editor + Juez → PUERTA 3 (automática)
- **Claude Code:** subagente `editor`.
- **Construcción:**
  - `index.html` (GSAP en pausa, `window.seek(t)`, kit `_studio/lib/kit.js` + kit del cliente) y `music.py` (`synth.master_lufs` → -14 LUFS / -1 dBTP).
  - Revisión con `preview.py`.
  - Borrador: `render.py --draft` (~1–2 min).
  - QA: `python _studio/tools/qa.py --video borrador.mp4 --html index.html --out qa`.
  - Costuras: `python _studio/tools/seams.py --html index.html`. Cuadros dorados entre vueltas: `golden.py --save` / `--compare`.
- **Juez:** el subagente `juez` lo revisa en contexto limpio con la rúbrica de `rol-juez.md`. Solo los P0 bloquean, máximo 2 vueltas.

### 6. PUERTA 4: Yeyow
- Le muestras el borrador, `qa/contacto.png`, los 3–5 timestamps clave y la ficha del Juez.
- Sus notas van textuales a `05-revision.md` y se clasifican:
  - **revisión:** se hace;
  - **petición nueva:** vuelve a la PUERTA 1 o 2;
  - **vaga:** se traduce a una opción concreta con timestamp.

### 7. Entrega final (solo con `veredicto_yeyow: APROBADO`)
- Render completo **en la misma máquina** (Windows y Linux no dan los mismos píxeles): `render.py … --sub 4 --workers N --audio music.wav`.
- `deliver.py --poster-t <cuadro asentado y con marca>`, y después `qa.py` del archivo final.
- `entregas/<cliente>-NN-share-copy.txt` (+ variantes).
- Actualiza la serie, la tabla **Huella** y el copy aprobado en `perfil.md`, `PRODUCTOS.md` y el doc del Project. Las técnicas `nueva` que usó el video pasan a `probada` en `tendencias.md`.
- Si el video estrenó una estructura que vale repetir, **congela la receta** en `recetas.md`.

## Cómo se aprueba
- **Claude Code:** Yeyow escribe `/korvex-motion:aprobar brief|guion|video [notas]`, o lo dice con sus palabras ("apruebo el brief").
- **Cowork:** Yeyow lo dice en el chat.
- **Qué se escribe:** solo entonces escribes `aprobado: true`, `aprobado_por: Yeyow`, la fecha y su texto en "Decisiones de Yeyow".
- **Una corrección no es aprobación:** se corrige, se vuelve a mostrar y se confirma.
- **En Claude Code** el hook `gate_check.py` bloquea escribir el guion, el video o la entrega si falta la aprobación.

## Leyes creativas (resumen; el detalle está en `rol-guionista.md` y `rol-editor.md`)
- **Duración y gancho:** 15–30 s (18–22 ideal). Gancho en 2 s, en lenguaje del resultado y no con nombres de funciones. El mensaje llega en el beat 2.
- **Mostrar, no contar:** enseña la cosa funcionando (UI real, flujo real). Máximo un bloque de cifras, y solo con fuente.
- **Legibilidad:**
  - etiqueta ≥0.8 s;
  - oraciones de hasta 7 palabras: ~0.3 s por palabra (mínimo 1.2 s); de 8 palabras o más: 0.35 s por palabra;
  - texto legible cada 2 beats, no cada beat.
- **Zona segura:**
  - orgánico: y 150–1550, sin texto en x>950 entre y 900–1700;
  - ad: CTA y teléfono por encima de y≈1250 (`qa.py --safe 270,1250,950,900,1700`).
- **Ritmo:** cada cuadro es publicable, sin crossfade entre layouts cargados, una dirección de salida y al menos un beat quieto.
- **Prohibidos:** partículas/confeti, ondas, lens flare, temblor de cámara, neón, rebote exagerado, glassmorphism por todos lados, clichés de IA y lenguaje SaaS genérico.
- **Sonido:** música y SFX son una sola pieza (misma tonalidad y reverb), golpes fijados al beat y -14 LUFS / -1 dBTP.
- **Estilo de Yeyow:** títulos en MAYÚSCULA, tarjetas con ícono + título + subtítulo, sin huecos grandes y español básico.

## Dónde corre
| | Claude Code (PC de Yeyow) | Cowork |
|---|---|---|
| Intake, research, brief, guion | ✓ (subagentes) | ✓ (en serie; aprueba desde el teléfono) |
| Render | ✓ todos los núcleos, rápido | Contenedor de 2 núcleos (10–12 min por reel de 20 s; el borrador ~1–2 min) |
| Puertas | Hook `gate_check.py` + `/korvex-motion:aprobar` | Por regla, con aprobación en el chat |
| Archivos | Directo en la carpeta | Se suben y bajan por el puente (≤20 MB por archivo) |

**Recomendado:** todo en una sola sesión de Claude Code. Cowork queda para revisar y aprobar desde el teléfono, o para trabajar sin el PC.

## Qué NO hacer
- Investigar sin intake, o preguntar lo que el perfil ya dice.
- Saltarse una puerta, escribir una aprobación o absorber en silencio una "petición nueva".
- Usar assets o datos de otro cliente.
- Copiar el guion, el footage o la música de una referencia: se toma la gramática.
- Renderizar el final en una máquina distinta a la del borrador aprobado sin avisar.
