# Propuestas para el rol Investigador — research en marketplaces (03/10/2026)

Pedido: revisar marketplaces de skills/plugins para mejorar el rol Investigador. Solo propuestas; no se tocó el método. Fuentes del 02/10 no se repiten.

## 1. Skills revisadas

| Skill | Repo (URL) | Lic. | Qué hace | Veredicto |
|---|---|---|---|---|
| `customer-research` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/tree/main/skills/customer-research) | MIT | Minería de lenguaje del cliente (reseñas, comentarios IG/TikTok/YouTube), confianza Alta/Media/Baja, sesgo por fuente, ≥5 datos por segmento, fuentes "proxy" | **Adoptar** (nuevo frente al 02/10) |
| `competitor-profiling` | [marketingskills](https://github.com/coreyhaines31/marketingskills/tree/main/skills/competitor-profiling) | MIT | Observado / inferido / implicación; "no observado ≠ no existe"; nunca afirmar motivos | **Adoptar la regla**, no el perfil B2B |
| `research-positioning`, `knowledge-review`, `create-shortform` | [hungv47/meta-skills](https://github.com/hungv47/meta-skills) | MIT | Observado/Inferido/Asumido; "momento costoso"; un hilo = una muestra; recheck con fecha; "el benchmark de otra cuenta no es tu base" | **Adoptar** |
| `research` + `deep-research` | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills/tree/main/research) | MIT | Citar solo lo devuelto en la sesión; conteo búsquedas/leídas/citadas; criterios de parada | **Adoptar** conteo y parada; descartar router |
| `review-reputation` + `absent-is-not-zero.md` | [knowledge-work-plugins/small-business](https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business) (instalado) | Apache-2.0 | Temas con conteo y verbatim; "Fuentes" con fallos nombrados; "ausente no es cero" | **Adoptar** |
| `brand-voice/source-ranking.md` | [knowledge-work-plugins/partner-built](https://github.com/anthropics/knowledge-work-plugins/tree/main/partner-built/brand-voice) | Apache-2.0 | Niveles de fuente con peso y corte de 12 meses | **Adoptar simplificado** (3 niveles) |
| `claim-verifier` · `yt-research` | [jeremylongshore/claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) | MIT | CONFIRMADA/REFUTADA/NO VERIFICABLE con la prueba; referencia = video ≥3× la media del canal | **Adoptar las dos ideas** |
| `verification-before-completion` | [obra/superpowers](https://github.com/obra/superpowers) | MIT | Sin evidencia fresca no hay afirmación; "parece/debería" = bandera roja | **Adoptar** como puerta de salida |
| `ai-research-skills` | [WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills) | MIT | Claim sin evidencia → `status: gap`; el paso siguiente lo rechaza | **Adoptar la idea** |
| `recursive-research` | [Anjos2/recursive-research](https://github.com/Anjos2/recursive-research) | MIT | Niveles 1/2/3/Rechazo (marketing sin datos, SEO spam, IA sin supervisión) | **Adoptar la lista de rechazo** |
| `market-researcher`, `competitive-analyst`, `fact-checker` | [VoltAgent](https://github.com/VoltAgent/awesome-claude-code-subagents) · [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | MIT | Listas de palabras y pseudocódigo que no corre | **Descartar**: plantilla, no método |
| `competitive-brief`, `performance-report`, `competitive-landscape`, `voice-of-customer` | [knowledge-work-plugins/marketing](https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing) · [wshobson/agents](https://github.com/wshobson/agents) · [gtm-agents](https://github.com/gtmagents/gtm-agents) | Apache-2.0 / MIT | Battlecards, Porter, VoC con ARR | **Descartar**: enterprise; benchmarks sin fuente |
| `competitive-ads-extractor` | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | sin LICENSE | Ad Library; ejemplo inventado | **Descartar**; la idea sí (hay MCP de Meta) |
| `claude-plugins-official` | [anthropics](https://github.com/anthropics/claude-plugins-official) | Apache-2.0 | Plugins de desarrollo | Nada de research |

## 2. Mejoras concretas

### 2.1 Nivel de confianza por dato y fecha de recheck
**Brecha:** § Checklist pide "cada hecho lleva fuente" pero no separa lo leído de lo inferido ni dice cuándo caduca (en Korvin #4 conviven código, una GUIA desactualizada y "Yeyow, chat" con el mismo peso).
**Texto (nueva sección antes de la Plantilla):**
```
## Cómo se marca cada dato
Cada hecho lleva fuente Y nivel:
- [LEÍDO] lo vi en esta sesión: código, captura, perfil, marca.js, chat de Yeyow con fecha.
- [INFERIDO] lo deduzco de algo leído; digo de qué.
- [NO VERIFICADO] no lo encontré. Nunca va al video.
Fuentes: A) código / capturas / perfil / Yeyow · B) web del cliente, docs oficiales de la plataforma · C) reseñas y comentarios públicos (verbatim, URL, fecha) · Rechazo) blogs sin fuente, cifras sin estudio, "lo que yo sé".
Lo que puede cambiar (precio, función en desarrollo, zona segura) lleva `recheck: <fecha o evento>`. Un pendiente no se vuelve hecho por viejo.
Las afirmaciones negativas ("no tiene X") y universales ("todos…") se verifican dos veces.
```
**Fuente:** meta-skills; `claim-verifier`; `recursive-research`; `customer-research`.

### 2.2 "No observado ≠ no existe" y "ausente no es cero"
**Brecha:** § Errores comunes prohíbe inventar, pero no dice cómo escribir lo que *no* se encontró.
**Texto (añadir a § Errores comunes):**
```
- Escribir "no tiene" cuando solo no lo viste. Se escribe: "no observado en <archivos revisados>, al <fecha>".
- Tratar una fuente vacía como buena noticia. Si Google Maps, IG o el FAQ no devolvieron nada, va en § 14 Fuentes como "0 — sin resultados" o "falló".
- Afirmar por qué el cliente o un competidor hizo algo. Se registra qué cambió, no el motivo.
```
**Plantilla:** añadir `## 14. Fuentes` — una línea por fuente: nombre · qué devolvió (conteo) · "falló" si falló.
**Fuente:** `competitor-profiling`; `absent-is-not-zero.md`; `review-reputation/sources.md`.

### 2.3 Lenguaje del cliente con muestra y sesgo
**Brecha:** § Proceso paso 4 pide "≥5 verbatim" pero no dice dónde buscarlas para un negocio pequeño en RD ni cuándo bastan (Korvin #4 cerró con "no verificado: frases reales de clientes").
**Texto (sustituye el paso 4):**
```
4. Audiencia y dolor en sus palabras. Dónde, en orden: a) reseñas del cliente en Google Maps (pedir al dueño captura o exportación); b) comentarios de los reels del cliente y de 2–3 cuentas del rubro (§ 6b); c) FAQ, chats de WhatsApp autorizados, preguntas de alta; d) sin reseñas propias → reseñas de competidores, marcadas "proxy".
   Cada frase es una fila: fuente+URL+fecha · verbatim · contexto · tema (dolor / disparador / resultado / alternativa / vocabulario) · sentimiento.
   Reglas: un hilo = UNA muestra · ≥5 datos independientes por segmento antes de llamarlo "tema" · ≤12 meses · se guarda el texto, nunca el @ ni la foto · las preguntas ("¿funciona para…?", "¿cuánto…?") valen más que los elogios.
   Anotar el momento costoso: el evento que vuelve urgente el problema (la cita perdida a las 11 PM).
```
**Fuente:** `customer-research` (`source-guides.md` § B2C); `research-positioning`; `review-reputation`.

### 2.4 Referencias y competidores medidos con IG_SCRAPPER y Meta Ad Library
**Brecha:** § Proceso paso 6 mide con `qa.py` solo si el video es local; como no se descargan videos ajenos, la referencia externa queda sin medir (Korvin #4, R3).
**Texto (nuevo paso 6b):**
```
6b. Métricas públicas (Apify `apify/instagram-scraper`, solo datos públicos).
- Entrada: resultsType reels · directUrls [cuenta] · resultsLimit 30 · onlyPostsNewerThan "6 months". ≈ US$0,003 por resultado (tarifa FREE, 10/2026).
- Mediana de videoPlayCount y likesCount de la cuenta. Referencia = reel ≥3× su mediana. La base es la cuenta, no nosotros.
- Por referencia: videoDuration, largo del caption, hashtags, musicInfo, commentsCount, 3 preguntas de los comentarios, isPinned / paidPartnership (sesgo).
- El beat sheet se hace viendo el reel en el navegador. Nunca se descarga videoUrl a assets/; se cita la URL.
- Ads: Meta Ads → ads_library_search por página del competidor. Activo ≥30 días = lo siguen pagando; se anota promesa, gancho y CTA.
- Ética: Instagram prohíbe la recolección automatizada sin permiso; Apify opera sobre datos públicos. ≤30 por cuenta, solo research, nada se republica ni se guarda de personas. Si Yeyow no quiere scraping: 10 reels a mano.
```
Fila nueva en § 7: `| Métricas públicas (fecha) | plays · likes · comentarios · mediana de la cuenta |`.
**Fuente:** esquema del actor (03/10/2026); `yt-research`; `create-shortform`; tool `ads_library_search`.

### 2.5 Cuándo parar
**Brecha:** no hay criterio de parada; § Errores comunes solo dice "10 páginas sobra".
**Texto (nueva sección antes de la Checklist):**
```
## Cuándo parar
Se para cuando se cumplen las 4: 1) los campos de bloqueo están [LEÍDO] (flujo con textos exactos, CTA, prohibidos); 2) hay ≥5 verbatim o el hueco está nombrado; 3) hay 2 referencias medidas; 4) cada búsqueda nueva repite lo que ya hay.
Tope: ~90 min o 15 búsquedas web. Si no alcanza, se entrega con huecos nombrados.
Al final, 3 números: búsquedas · fuentes leídas · fuentes citadas.
La pregunta pendiente que más cambiaría el brief va primera en § 13.
```
**Fuente:** alirezarezvani `research` y `deep-research`; meta-skills.

### 2.6 Entrega corta al Productor + puerta de salida
**Brecha:** § "Qué le pasa al Productor" es una línea y el Productor lee 13 secciones; la Checklist no exige evidencia fresca antes de `listo-para-productor`.
**Texto (bloque obligatorio tras el frontmatter):**
```
## 0. Para el Productor (10 líneas; cada una remite a su sección)
- Audiencia estrecha + momento costoso (§ 5)
- Flujo real en una línea con el texto final de pantalla (§ 4)
- Claim más fuerte permitido + fuente (§ 3)
- 3 verbatim top (§ 5)
- Antipatrón y lo contrario (§ 8)
- Receta probable · duración · uso (frontmatter)
- Lo que falta y quién lo resuelve (§ 13)
- Fuentes: leídas / citadas / fallidas (§ 14)
```
**Checklist:** `- [ ] Antes de poner listo-para-productor volví a abrir cada fuente de "texto exacto". Donde escribí "debería", "parece" o "probablemente", puse [NO VERIFICADO].`
**`rol-productor.md` § 1:** "Si una fila de § 3 o § 5 no tiene fuente ni nivel, el research se devuelve."
**Fuente:** `verification-before-completion`; `ai-research-skills`; Conquistador `quality.md`.

### 2.7 Prueba de distinción para el antipatrón
**Brecha:** § Proceso paso 7 pide "cómo se ven todos" pero no comprueba que lo hallado sea propio del cliente.
**Texto (añadir al paso 7):** `Prueba: cambia el nombre del cliente por el de un competidor en § 2 y § 8. Si todo sigue sirviendo, no encontraste el mecanismo propio; vuelve a § 3.`
**Fuente:** Conquistador `quality.md` ("competitor swap"); `research-positioning`.

## 3. Lo que NO conviene adoptar
- **Routers de research** (alirezarezvani, hyperflow): el intake ya decide.
- **Carpetas por fuente, ≥3 fuentes por tesis, pase adversarial** (`deep-research`, `recursive-research`): 1–3 h por reel de 20 s; el Juez ya hace el pase crítico.
- **Frameworks de empresa** (Porter, battlecards, VoC con ARR): no caben en un reel ni en el perfil de un salón.
- **Benchmarks numéricos de las skills de marketing**: sin fuente primaria; chocan con "nada de cifras de blogs".
- **Agentes-plantilla** (VoltAgent, davila7): no cambian ningún comportamiento.
- **Scoring compuesto de fuentes** (`source-ranking`, pesos 0,30/0,25…): precisión falsa; 3 niveles alcanzan.
- **Descargar reels ajenos para `qa.py`**: exige guardarlos; va contra la regla de no copiar y contra los términos de Instagram.

## 4. No verificado
- Los Términos de Instagram (`help.instagram.com/581066165581870`) no cargaron desde aquí; la frase sobre recolección automatizada se confirmó en copias de terceros (expediente judicial de 2019). Revisar la versión vigente antes de usar Apify a escala.
- Qué mide `videoPlayCount` vs `videoViewCount` en el actor (no documentado); el precio por resultado puede cambiar.
- `gh api` no tuvo acceso a repos ajenos: estrellas y uso no se anotaron; fechas salen del clon. `competitive-ads-extractor` no trae LICENSE.
- Exportar reseñas desde Google Business Profile: `review-reputation` lo afirma; no lo comprobé.
- `video-shotcraft` sigue sin poder clonarse desde este sandbox.
