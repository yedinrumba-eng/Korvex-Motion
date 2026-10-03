# Investigación de roles para `korvex-motion` — resumen (02/10/2026)

Pedido: buscar en la web y en GitHub las mejores prácticas, skills y plantillas para cada rol del flujo spec-driven (Investigador → Productor → Guionista → Editor → Juez), y redactar versiones mejoradas alineadas con nuestro pipeline (HTML + GSAP determinista, Playwright + ffmpeg, música en numpy, reels 1080×1920 de 15–30 s, 120 BPM, leyes de /brag, `qa.py`).

Complementa `_studio/refs/investigacion-2026-10.md` (repos de motion). Esta carpeta se centra en **los roles, los documentos y el método**.

## Archivos de esta carpeta
| Archivo | Qué es |
|---|---|
| `00-RESUMEN.md` | Este archivo: hallazgos, fuentes, licencias, lo que no se verificó |
| `categorias.md` | Matriz de 10 categorías de video (objetivo, KPI, estructura, ganchos, tono, CTA, errores, assets) |
| `intake-preguntas.md` | Las preguntas que el Investigador hace SIEMPRE (formato de opciones múltiples, ≤4 por ronda) + extras por categoría |
| `rol-investigador.md` | Rol 1 → `01-research.md` |
| `rol-productor.md` | Rol 2 → `02-brief.md` (PUERTA 1) |
| `rol-guionista.md` | Rol 3 → `03-guion.md` + `storyboard.html` (PUERTA 2) |
| `rol-editor.md` | Rol 4 → `index.html`, `music.py`, `borrador.mp4`, `04-build.md` (PUERTA 3) |
| `rol-juez.md` | Rol 5 → veredicto en `04-build.md` + ficha para `05-revision.md` (PUERTA 4) |
| `recetas.md` | 12 recetas de formato con estructura por tiempos a 120 BPM |

## El flujo, con lo nuevo marcado
```
/korvex-motion <idea o referencia>
  │
  ├─ 1 Investigador   intake (≤4 preguntas/ronda, recomendada primero, recibos) → 01-research.md
  │                   hechos con fuente · flujo real · lenguaje verbatim · 2–3 referencias MEDIDAS · antipatrón · assets+licencia
  ├─ 2 Productor      frase Get/Who/To/By · UN mensaje · pitch 3–5 conceptos (≥2 atípicos) · afirmaciones permitidas
  │                   · criterios medibles → 02-brief.md ══ PUERTA 1 (Yeyow)
  ├─ 3 Guionista      gancho de 3 componentes · beat sheet a 120 BPM (qué se carga al siguiente, golpes, beat quieto)
  │                   · tiempos de lectura · storyboard.html → qa/bocetos.png → 03-guion.md ══ PUERTA 2 (Yeyow)
  ├─ 4 Editor         viste los bocetos, no los redibuja · index.html + music.py · borrador · qa.py → 04-build.md
  │                   └─ 5 Juez (contexto limpio, 9 criterios, P0/P1/P2, máx. 2 vueltas) ══ PUERTA 3 (automática)
  └─ Yeyow            05-revision.md: notas con timestamp, clasificadas (revisión / petición nueva / vaga) ══ PUERTA 4
                      → render final (misma máquina) → deliver.py (poster = cuadro 0) → entregas/ + share-copy
```

## Los 10 hallazgos que más cambian el flujo

1. **Una sola conversación de intención, con recibos.** HyperFrames separa "entender" (intent layer) de "ejecutar" (workflow): se pregunta una vez, cada campo lleva su opción recomendada primero + la razón ("recibo"), y el resumen final separa **lo que dijo el usuario** de **lo que se infirió**. Lo adoptamos tal cual en el Investigador: nunca preguntar lo que `perfil.md` o la idea ya responden; convertirlo en opción recomendada con su recibo.
2. **"Formado" vs "no formado".** Si la idea ya trae mensaje + material + ocasión, se va directo a las preguntas obligatorias. Si solo trae un tema ("haz un video de Korvin"), antes de preguntar el mensaje se hace una **ronda de pitch**: 5 conceptos, ≥2 fuera de lo típico, todos antes de recomendar uno, y "mezclar" es una respuesta válida. Va en el Productor.
3. **Pirámide invertida: valor antes que evidencia.** El gancho habla en el lenguaje del resultado para el espectador (nunca con nombres de funciones), el mensaje aterriza en el beat 2 y todo lo demás es evidencia. Autoprueba: borra los beats de evidencia y el video debe seguir diciendo el valor; borra los de valor y si "todavía funciona", era un tour de features.
4. **El storyboard es una propuesta, no un listado.** Se presenta como "Este video le dice a [audiencia] que [mensaje]" + tabla de beats con columna **Por qué** (cada beat se rastrea al mensaje; el que no se rastrea, se corta). Y los bocetos se revisan en una hoja HTML estática con fuentes y colores reales (`storyboard.html`): cambiar un beat ahí cuesta 30 s; después del build, minutos.
5. **El gancho son 3 componentes que no se repiten**: acción visual + texto en pantalla + sonido/voz. Si los tres dicen lo mismo, dos están desperdiciados (marketingskills). Además, "cada test de gancho es también un test de rampa (seg. 3–15)": al cambiar el gancho hay que reescribir lo que sigue, no pegarlo encima.
6. **Un mensaje, un "pero no", un decisor.** Del brief de agencia (iart `creative-brief`): si hay tres mensajes el brief no está listo (se fuerza el ranking; el #1 va al video, el resto son videos futuros); el tono lleva guardarraíl ("cálido, pero no cursi"); los adjetivos vagos se traducen a elecciones acotadas ("¿'limpio' = más aire, paleta de 2 colores, easing lento o layout mínimo?").
7. **Las notas de revisión se clasifican antes de tocar el archivo**: *revisión* (cambia algo ya aprobado en brief/guion: timing, color de la paleta, copy aprobado, un bug) vs *petición nueva* (escena nueva, +duración, concepto nuevo, otro formato, revertir algo aprobado). Las notas vagas ("que tenga más punch") se traducen a opción acotada + timestamp antes de ejecutar. Va en `05-revision.md` y en el Juez.
8. **El juez juzga una vez y solo lo "egregiamente malo" vuelve** (@stokebuilder); otro patrón: dos revisores eligen 9–10 issues cada uno y los rankean P0/P1/P2, un tercero arregla; solo los P0 bloquean; si los revisores no coinciden, se elige uno y se escribe por qué (@Voxyz_ai). Adoptamos: Juez independiente, rúbrica fija, P0/P1/P2, máximo 2 vueltas, solo P0 bloquea.
9. **Legibilidad con números externos que confirman los nuestros.** BBC: 160–180 palabras/min ≈ 0,33–0,375 s por palabra y mínimo ≈0,3 s/palabra. Nuestro 0,3 s/palabra (mínimo 1,2 s) está en el límite rápido de ese rango: bien para líneas de 1–6 palabras; para oraciones de 8+ palabras el Guionista debe usar 0,35 s/palabra. TikTok (oficial) recomienda "5–10 palabras por segundo" para texto en pantalla, que es *más rápido* que lo nuestro; lo ignoramos a favor de la legibilidad: nuestra regla es más conservadora y la mantenemos.
10. **Zona segura: la nuestra es el mínimo orgánico, no la de anuncios.** Nuestra zona (y 150–1550; evitar x>950 entre y 900–1700) coincide con el consenso orgánico (arriba ~150–250 px, abajo ~350–400 px, derecha ~120 px). Para **anuncios** Meta publica 14 % arriba (~270 px) y 35 % abajo (~672 px): si un reel va a correr como ad, el CTA y el teléfono deben quedar por encima de y≈1250. Lo convertimos en un parámetro del brief (`uso: organico | ad`) y en un flag de `qa.py --safe`.

## Qué se puede reutilizar y bajo qué licencia

| Fuente | Licencia | Qué tomamos | Cómo |
|---|---|---|---|
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | Apache-2.0 | `skills/hyperframes/references/intent-interview.md`, `brief-contract.md`, `brief-format.md`, `pitch-round.md`, `review-loop.md`, `production-loop.md`, `storyboard-format.md`; `skills/hyperframes-creative/references/story-spine.md`, `storyboard-recipe.md`, `beat-direction.md`, `motion-principles.md`; `skills/product-launch-video/references/story-design.md` (arcos PAS/BAB/Demo Loop/Future Pacing/Feature-Benefit + banco de "formas de guion" por rol de beat); `skills/motion-graphics/agents/director.md` | Ideas y estructura de documentos, reescritas en español y adaptadas a nuestro motor. Apache-2.0 permite copiar texto si se conserva el aviso de licencia; preferimos reescribir. No usamos su CLI ni servicios de HeyGen. |
| [iart-ai/motion-skills](https://github.com/iart-ai/motion-skills) (índice) → packs [tiktok-video-skills](https://github.com/iart-ai/tiktok-video-skills), [ad-video-skills](https://github.com/iart-ai/ad-video-skills), [freelance-motion-skills](https://github.com/iart-ai/freelance-motion-skills), [motion-design-skills](https://github.com/iart-ai/motion-design-skills), [explainer-video-skills](https://github.com/iart-ai/explainer-video-skills) | MIT (cada pack trae su LICENSE MIT) | `short-form-video` (arco de retención, gramática de ganchos, interrupciones de patrón, loop), `ad-creative-video` (anatomía del ad 15–30 s, taxonomía de ganchos, message-match gancho↔CTA, una variable por variante), `launch-video/references/launch-structure.md` (el sonido manda: drop → reveal), `testimonial-video` (confianza antes que movimiento; citar palabra por palabra), `creative-brief` (11 dimensiones, traductor de adjetivos vagos, "pero no", sign-off), `client-revisions` (revisión vs petición nueva, traductor de feedback vago), `video-delivery-specs/references/qc-checklist.md` y `safe-areas.md`, `animation-principles` (easing, duraciones, stagger, regla del 1/3) | Reutilizable con atribución MIT. Sus scripts son para Remotion (no los usamos). Ojo: trae cifras de retención ("87 % decide en 3 s", "70 %+ view-through") **sin fuente**: no las citamos como hechos. |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT | `skills/ad-creative/references/hook-system.md` (gancho de 3 componentes, matriz segmento×motivación×formato, embudo diagnóstico stop/stay/click/convert, regla de la rampa), `short-form-video-specs.md` (banda segura multiplataforma 720×1200: y 220–1420; captions estáticas; música orgánica vs horneada), `creative-review-page.md` (página HTML de aprobación para el cliente), `skills/video/references/edit-anatomy.md` (deconstruir una referencia en un beat sheet + 3–5 "movimientos firma"), `skills/copywriting/references/copy-frameworks.md` (fórmulas de titulares) y `ai-tells.md` (muletillas de IA prohibidas), `skills/social/references/short-form-video.md` (librería de ganchos por objetivo) | Reutilizable con atribución MIT. Lo más valioso para el Investigador (edit anatomy) y el Guionista (hook system, ai-tells). |
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | Apache-2.0 | 152 fichas de toma en 10 categorías (propósito, energía, duración sugerida, parámetros, pitfalls), librería SFX en 16 categorías, flujo capture → storyboard → implement → sound → beat sync → QA → export | **No se pudo clonar desde este sandbox** (el clone pidió credenciales; `raw.githubusercontent.com/.../master/README.md` dio 404). Se verificó por la página del repo (6,7k estrellas). Vale como vocabulario de tomas para `recetas.md`; revisar desde el PC. Sus componentes son Remotion. |
| [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | Apache-2.0 | Recetas con `avoid_when`; skills `web-clone` (extraer DNA de diseño de una web: útil al investigar la web de un cliente) y `gsap-*` | Ideas; su app no se usa. |
| [anthropics/skills](https://github.com/anthropics/skills) | Apache-2.0 por skill (`LICENSE.txt` en cada carpeta); el spec vive en [agentskills.io/specification](https://agentskills.io/specification) | Formato `SKILL.md` (frontmatter `name`/`description`), `skill-creator` para empaquetar `korvex-motion`, `discernment-nudge` (idea de cerrar con 2–3 preguntas de verificación) | No tiene contenido de video. Sirve para la forma del plugin. |
| [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | MIT (la compilación); cada prompt es de su autor | Patrón de juez único (`prompts/stokebuilder-356793.md`), patrón de 2 revisores + 1 fixer con P0/P1/P2 (`prompts/voxyz-ai-345550.md`), "quality gate: inspecciona 8 cuadros representativos" (`prompts/gdgtify-929495.md`), verificación numérica del audio (`prompts/astrothewizard-618782.md`) | Como inspiración de método; no se republican prompts. |

## Fuentes web (plataforma, guion, legibilidad)

**Oficiales o cuasi oficiales**
- TikTok for Business, *Creative best practices for performance ads*: "Prioritize your hook in the first 6 seconds", "Introduce your content proposition in the first 3 seconds", "We recommend displaying 5-10 words per second when using text", vertical 9:16 dentro de la zona segura, 3–5 creatividades por grupo de anuncios. https://ads.tiktok.com/help/article/creative-best-practices?lang=en
- Meta, zonas seguras de Reels/Stories ads (14 % arriba, 35 % abajo, 6 % lados; en marzo de 2026 unificó FB/IG Stories/Reels en una sola zona 9:16). La página oficial (`facebook.com/business/help/...`) **no se pudo leer** desde aquí (robots.txt). Cifras tomadas de terceros que la citan: https://www.hopperhq.com/blog/instagram-reel-size/ · https://www.firstpier.com/resources/instagram-ad-safe-zones · https://billo.app/?p=50654 (menciona el lienzo unificado 1440×2560).
- Netflix Timed Text Style Guide (marketing assets): no fija cps para marketing; remite a las guías por idioma; "no pongas subtítulos arriba". https://partnerhelp.netflixstudios.com/hc/en-us/articles/115000239632
- BBC Subtitle Guidelines (vía resumen de Clevercast): 160–180 wpm (0,33–0,375 s/palabra), mínimo ≈0,3 s/palabra, máximo 2 líneas. https://clevercast.com/bbc-subtitling-guidelines (original: https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles/)

**Terceros (útiles, no oficiales)**
- Zona segura TikTok (orgánico): arriba ~150 px, derecha ~120 px, abajo ~350–400 px. https://www.trymypost.com/blog/tiktok-ad-specs-2026-safe-zones (no cita doc oficial)
- Banda segura multiplataforma "peor caso" 720×1200 (y 220–1420): marketingskills `short-form-video-specs.md` (advierte que "los números se mueven con cada update").
- Loudness: Instagram y TikTok **no publican** su objetivo de normalización; -14 a -16 LUFS es rango seguro; YouTube -14 LUFS / -1 dBTP. https://openclip.app/learn/audio-normalization.md
- Señales de ranking de Reels 2025 (Mosseri, ene. 2025, parafraseado por terceros): tiempo de visualización, likes por alcance, envíos por alcance; "los primeros 3 segundos"; 3–5 hashtags; sin marcas de agua; 9:16. https://posteverywhere.ai/blog/how-the-instagram-algorithm-works · https://later.com/blog/instagram-reels-tips · https://onestream.live/blog/instagram-algorithm-creators-guide/
- Fórmulas de gancho: https://www.opus.pro/blog/tiktok-hook-formulas (sus porcentajes son de datos propios, sin fuente externa) · https://faceless.so/blog/15-hook-formulas-for-tiktok-reels-shorts
- Frameworks de copy (AIDA, PAS, BAB, 4Ps, FAB, PASTOR): https://growthmethod.com/writing-frameworks-for-marketers/
- Brief de una frase Get/Who/To/By: https://www.selfstorming.com/tools/frameworks/Get-Who-To-By
- Principios de motion aplicados a UI (UX in Motion Manifesto): https://uxmag.com/articles/creating-usability-with-motion-the-ux-in-motion-manifesto

## Lo que NO se verificó (y cómo lo tratamos)
- **Porcentajes de retención** ("87 % decide en 3 s", "65 % a los 3 s = 4–7× impresiones", "Reels ≥65 % view-through"): aparecen en skills y blogs sin fuente primaria. En los documentos los marcamos como *orientativos* y medimos lo nuestro en Insights/Analytics.
- **Pixeles exactos de Meta y TikTok**: no leímos las páginas oficiales. Regla práctica: antes de un gasto en ads, revisar la superposición de zona segura en Ads Manager / TikTok Ads Manager.
- **Normalización de audio de IG/TikTok**: no documentada. Mantenemos -14 LUFS / -1 dBTP (y `qa.py` avisa fuera de ±3 LU).
- **"21–34 s es el sweet spot de TikTok"**: lo repiten varios blogs atribuyéndolo a TikTok; no encontramos la página. Nuestro rango 15–30 s sigue.

## Decisiones que proponemos para el pipeline (afectan archivos fuera de esta carpeta; no se tocaron)
1. `03-guion.md` sustituye a `plan.md` (misma información y más). Dejar `plan.md` como puntero de 2 líneas en los videos viejos; actualizar `_studio/README.md`.
2. `02-brief.md` y `03-guion.md` llevan `aprobado: false|true` en el frontmatter; un hook `gate_check.py` bloquea el build si falta.
3. `02-brief.md` lleva `uso: organico | ad`; `qa.py` recibe `--safe` ajustado (ad: y 270–1250).
4. El Juez corre en contexto limpio (subagente) y escribe en `04-build.md` → sección "Veredicto del juez"; prepara la ficha de `05-revision.md`.
5. `recetas.md` es el catálogo que el Productor cita en el brief (`receta: launch-ui-real`), y el Guionista la instancia.

---

## Investigación 2: skills de marketplaces por rol (03/10/2026)
Pedido de Yeyow: revisar skills de marketplaces (plugins oficiales de Anthropic, knowledge-work-plugins, obra/superpowers, wshobson/agents, VoltAgent, davila7, jeremylongshore, alirezarezvani, ComposioHQ, hyperframes `.claude/skills`, greensock/gsap-skills, emilkowalski/skills, lottiefiles, hooksmith, motion-creative, smixs, hamelsmu/evals-skills y otros) para subir el nivel de cada rol.
- Propuestas completas, con tabla de skills, licencias, lo descartado y lo no verificado: `research-2/rol-<rol>-propuestas.md`.
- Integradas como **método v2** en cada `rol-*.md` (sección "Fuentes de las mejoras v2" al final de cada uno), en las plantillas 01–05 y en los agentes del plugin (`korvex-motion` 1.1.0).
- Nuevo: `juez-casos.md` (casos de calibración del Juez, sembrado con Korvin #4).
- Pendiente de construir en el motor (propuesto, no hecho): `K.cut`, `K.nudge`, `K.fitText`, `K.posterize`, `seams.py` (costuras medidas) y cuadros dorados automáticos.

## Investigación 3: radar de tendencias y motor v3 (03/10/2026)
Pedido de Yeyow: que el estudio se mantenga al día y que los videos de un mismo cliente no tengan siempre la misma secuencia de edición. Repetir gancho, receta o método se vale; un look puede durar 3–4 videos y después cambia (aclaración de Yeyow, 03/10/2026).
- **Catálogo:** `_studio/refs/tendencias.md`: 40 técnicas (T01–T40) en 8 grupos, con estado nueva / probada / gastada, cómo se hacen en el motor, la corrida de Instagram con Apify y la lista "Gastadas o prohibidas". Fuentes con fecha al final del catálogo.
- **Método:** Modo Radar dentro del research (`rol-investigador.md`: lo corre el Investigador si el catálogo tiene >30 días; fuentes fijas y Apify por defecto); paso 3b "Rotación del look" en `rol-productor.md`; tabla **Huella** en cada `perfil.md` (la llena el Editor al entregar, como registro).
- **Plugin 1.2.0:** comando `/korvex-motion:radar`.
- **Motor v3:** `K.cut`, `K.nudgeEase`, `K.fitText`, `K.posterize` en `lib/kit.js`; `tools/seams.py` (costuras medidas) y `tools/golden.py` (cuadros dorados). Detalle y pruebas en `_studio/README.md`.
- Propuestas originales: `research-2/radar-propuestas.md`.
