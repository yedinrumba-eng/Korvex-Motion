# Radar de tendencias — propuestas para pegar (03/10/2026)

Texto listo para `rol-investigador.md`, `rol-productor.md` y el plugin. Catálogo: `_studio/refs/tendencias.md`. Este archivo no edita nada por sí solo.

---

## A. Para `rol-investigador.md` → nueva sección "Modo Radar"

### Modo Radar (mantener `refs/tendencias.md`)
**Cuándo:** una vez al mes (primer lunes) y antes de cada serie nueva (cliente nuevo o cambio de categoría). Tope: 60 min o 12 búsquedas. No reemplaza el research de un video: lo alimenta.

**Qué hace, en orden:**
1. Lee `tendencias.md` y la tabla Serie de cada `perfil.md`: qué técnicas se usaron en los últimos 6 videos del estudio.
2. Recorre las fuentes fijas (lista D). Cada técnica nueva entra como `### Tnn — nombre` con los 8 campos del catálogo. Si no es determinista o pide algo que el kit no tiene, lo dice y la marca "pide kit".
3. Actualiza **Estado**:
   - **nueva → probada**: salió en un video con `veredicto_yeyow: APROBADO`; se anota el video en "Usado en".
   - **probada → gastada**: usada en ≥3 de los últimos 6 videos del estudio, **o** vista en ≥3 fuentes fijas el mismo mes como plantilla copiada igual, **o** Yeyow dice "ya se ve igual".
   - **gastada → probada**: 6 meses sin usarla y un giro propio declarado.
   - Las prohibidas del estudio no son técnicas: van en "Gastadas o prohibidas".
4. Instagram (solo si Yeyow lo autorizó, P13): Apify `instagram-scraper`, ≤3 cuentas, `resultsType: reels`, `resultsLimit: 20`, `onlyPostsNewerThan: "6 months"`. Mediana de reproducciones por cuenta; referencia = ≥3× **su** mediana. Se anota formato, duración y qué se ve en los primeros 2 s; nunca se descarga el video ni se guardan datos de personas. Cuesta centavos por corrida.
5. Reescribe el bloque "Lo que dijo el radar" (fecha, cuentas, medianas, hallazgos) al final del catálogo.
6. **Entrega al Productor**: en `01-research.md` § 0 una línea "Radar: 2–3 candidatas" (ID + una frase). Criterio: estado `nueva` o `probada`, no usadas en los últimos 2 videos del cliente, que calcen con categoría y receta probable, al menos una de costo bajo. El Productor decide; el Investigador no propone conceptos.

**Checklist:** fecha del radar en el encabezado · cada entrada con fuente y fecha · estados revisados contra la tabla Serie · bloque IG con mediana por cuenta · 2–3 candidatas en el § 0.

---

## B. Para `rol-productor.md` → regla "Anti-repetición" (antes del paso 4, ronda de pitch)

### Regla anti-repetición
Antes de escribir conceptos, el Productor lee la tabla Serie del cliente y la del estudio (`PRODUCTOS.md`) y aplica:
- **Receta:** no repetir la del último video del mismo cliente (R1 siempre va; cambia el cuerpo).
- **Mecánica del concepto** (respuesta implícita, testigo, contraste, reencuadre, el formato es la idea): distinta a la de los últimos 2 videos del cliente.
- **Técnica firma** (lo que el espectador recordaría: morph, escáner, interruptor, iris…): ninguna de los últimos 3 videos del cliente ni de los últimos 2 del estudio. Las `gastadas` no se usan salvo que Yeyow las pida.
- **Paleta de transiciones** (T01–T06): no el mismo conjunto que el video anterior; cambia al menos una.
- **Estructura del gancho:** si el último abrió con 3 preguntas, este abre con observación, hora, antes/después o la pregunta tal cual la escribe la gente. Dos ganchos iguales seguidos = volver a pitch.
- **Chequeo de silueta** también contra el video anterior del cliente: misma distribución de bloques = mismo video.

**Cómo se anota:** la tabla Serie del `perfil.md` gana columnas `receta · mecánica · técnica firma (IDs) · transiciones (IDs) · gancho`. El Editor las llena al entregar; el Productor las lee en el paso 1. Cada concepto del pitch termina con `[radar: T22, T30]` y el brief § 6 lista las técnicas vetadas en este video por repetición.

---

## C. Comando `/korvex-motion:radar`

**Qué hace:** corre el Modo Radar sin un video de por medio.
- `radar`: fuentes fijas + estados → actualiza `refs/tendencias.md` y devuelve 10 líneas: qué entró, qué pasó a gastada, 3 candidatas por cliente activo.
- `radar <cliente>`: lo anterior más la tabla Serie de ese cliente y 2–3 candidatas para su próximo video, con receta y riesgo.
- `radar ig <c1> <c2> <c3>`: solo el bloque de Instagram (pide confirmación por el costo).
- `radar estados`: no busca; recalcula nueva/probada/gastada contra las tablas Serie.

**Qué entrega:** `refs/tendencias.md` actualizado (tabla, entradas, bloque IG, fecha) y un resumen pegable para la próxima sesión de research. No toca perfiles ni briefs. Si no hay nada nuevo, lo dice y solo cambia estados.

**Guardas:** no copia prompts ni textos ajenos (resume y cita); nada de cifras de engagement sin fuente primaria; cada URL con fecha; una fuente que no respondió va como "0 — falló".

---

## D. Fuentes fijas del radar

| Fuente | URL |
|---|---|
| School of Motion (blog, Motion Mondays) | https://schoolofmotion.com/blog |
| BUCK, Pencils Down (predicciones anuales) | https://pencilsdown.buck.co |
| Motionographer | https://motionographer.com |
| Codrops: Motion Highlights + demos GSAP | https://tympanus.net/codrops/category/articles/ui-interactions-animations-roundups |
| GSAP showcase | https://gsap.com/showcase/ |
| Rive blog | https://rive.app/blog |
| LottieFiles blog | https://lottiefiles.com/blog |
| Adobe Creative Trends (agosto) | https://business.adobe.com/uk/blog/adobe-2026-creative-trends-forecast |
| Apple HIG / WWDC (junio) | https://developer.apple.com/design/ |
| Communication Arts (columnas) | https://www.commarts.com/columns |
| Repo awesome-opus5-5-videos | https://github.com/yihui-dev/awesome-opus5-5-videos |
| Instagram vía Apify (≤3 cuentas/mes) | framer · notionhq · schoolofmotion; rotar una cuenta del rubro del cliente cada mes |

Se descartan listas SEO de vendedores de plantillas, agregadores sin fecha y cifras sin fuente primaria.
