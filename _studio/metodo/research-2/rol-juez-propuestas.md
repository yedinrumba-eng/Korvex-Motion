# Rol Juez — propuestas desde marketplaces de skills (03/10/2026)

Investigación 2 (la del 02/10 ya cubrió juez único, 2 revisores + fixer e iart `client-revisions`/`qc-checklist`). Aquí: revisores de los marketplaces de Claude Code y literatura de LLM-as-judge, contra el Juez de HOY (`rol-juez.md`). Solo propuestas.

## 1. Skills revisadas

| Skill | Repo · licencia | Qué hace | Veredicto |
|---|---|---|---|
| `code-review`, `pr-review-toolkit` | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-review) · Apache-2.0 | 5 revisores paralelos; un agente puntúa cada hallazgo 0–100 y descarta <80; lista de falsos positivos; bandas de confianza | Adoptar el puntaje por hallazgo; no los 5 agentes |
| `claude-code-security-review` | [anthropics](https://github.com/anthropics/claude-code-security-review) · MIT | Reglas duras + juicio individual por hallazgo (`keep_finding`, confianza, justificación) | Igual a lo nuestro: `qa.py` reglas, Juez juicio |
| `verification-before-completion` | [obra/superpowers](https://github.com/obra/superpowers) · MIT | Sin evidencia fresca no hay afirmación; "arreglado" = repetir la prueba | Adoptar en vuelta 2 |
| `requesting-code-review` | obra/superpowers · MIT | Lista "Declined to judge" (lo dejado fuera, con razón) | Adoptar en la ficha |
| `ui-visual-validator` | [wshobson/agents](https://github.com/wshobson/agents) · MIT | "No se cumplió hasta probarlo"; buscar evidencia de que falló | Adoptar la postura |
| `skill-creator/agents/grader.md` | [anthropics/skills](https://github.com/anthropics/skills) · Apache-2.0 | PASS/FAIL con evidencia citada; la carga de la prueba está en pasar; critica también los evals | Adoptar: el Juez critica el brief |
| `write-judge-prompt` + `validate-evaluator` | [hamelsmu/evals-skills](https://github.com/hamelsmu/evals-skills) · MIT | Juez binario por fallo; ejemplos claro/claro/borde con crítica antes del veredicto; medir acuerdo con el experto | Adoptar casos de calibración; rechazar 1–5 |
| `fact-check` | [jwynia/agent-skills](https://github.com/jwynia/agent-skills) · MIT | Log por afirmación: fuente · estado (Confirmada / Parcial / No encontrada / Contradicha); pasada separada | Adoptar la tabla de verdad |
| `brand-review` (instalada) | [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) · Apache-2.0 | Voz y términos; flags legales: superlativos, comparativos, testimonios sin atribución, descargos | Adoptar la lista legal |
| `named-persona-adversarial-review` | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · MIT | "Carga del cero" (un OK nombra 3+ cosas verificadas); leer de atrás hacia adelante | Adoptar ambas, no las personas |
| `adversarial-reviewer` | mismo repo · MIT | 3 personas hostiles; cada una DEBE hallar ≥1 problema | No |
| `design-critique`, `accessibility-review`, `performance-report` (instalada) | knowledge-work-plugins · Apache-2.0 | Rúbricas de UI (contraste WCAG 4,5:1); métricas tras publicar | Solo el número de contraste |
| `code-reviewer`, `qa-expert`; `llm-evaluation` | [VoltAgent](https://github.com/VoltAgent/awesome-claude-code-subagents) · MIT; wshobson · MIT | Listas genéricas; juez 1–10 sin sesgos | No |

Método (no skills): Zheng 2023 [2306.05685](https://arxiv.org/abs/2306.05685) (sesgos de posición, longitud y autopreferencia; mitigar con orden invertido, ejemplos, razonar antes); Wang 2023 [2305.17926](https://arxiv.org/abs/2305.17926) (evidencia antes de calificar); Panickssery 2024 [2404.13076](https://arxiv.org/abs/2404.13076) (el modelo prefiere lo suyo); Anthropic [develop-tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) (rúbricas con fallo automático, salida binaria); Hamel [llm-judge](https://hamel.dev/blog/posts/llm-judge/) (binario con crítica; el experto fija el estándar); Meta [unrealistic outcomes](https://transparency.meta.com/policies/ad-standards/deceptive-content/unrealistic-outcomes); Playwright [visual comparisons](https://playwright.dev/docs/test-snapshots).

## 2. Mejoras al rol de HOY (texto listo para pegar)

### M1. Anclas por criterio, sin escala 1–5 (§ Rúbrica)
Brecha: PASA/FALLA sin definir el caso límite; el #4 de Korvin #4 (lista ≈1,6 s vs ≥2 s) quedó en el aire. Fuente: Hamel, Anthropic.
```
Cada criterio tiene tres anclas:
- FALLA seguro: lo de la columna "P0 si…".
- PASA seguro: cumple el número y se ve en el cuadro.
- BORDE: cumple a medias (p. ej. ≥ la mitad del mínimo) → P1 + pregunta en "Solo tú decides". Nunca P0, nunca se ignora.
Cada ancla tiene un caso real en `juez-casos.md` (M7). Si no hay, se agrega al cerrar el video.
```

### M2. Verificar cada hallazgo antes de reportarlo (§ Proceso 4, § Formato)
Brecha: el hallazgo nace y se reporta en el mismo paso. Fuente: `code-review`, `security-review`, `ui-visual-validator`.
```
Antes de escribir un hallazgo, pruébalo:
- Evidencia: el cuadro extraído (`ffmpeg -ss t`) en `qa/juez-NN.png`, o el campo de `report.json`. Sin evidencia, no entra.
- Confianza: 100 lo veo y lo medí · 75 lo veo, no lo medí · 50 creo que sí · 25 quizá · 0 no lo vi.
- Solo ≥75 va a la tabla. 25–50 va a "Dudas" en la ficha; no bloquea.
- ¿Un editor con oficio lo marcaría, o es gusto? Gusto → P2.
Columna nueva: `Evidencia`.
```

### M3. Tabla de verdad + flags legales (§ Rúbrica criterio 1, § Lecciones #4)
Brecha: el criterio 1 se revisa de memoria; el P0 #1 de Korvin #4 (texto REAL sin fuente) salió a mano. Fuente: `fact-check`, `brand-review`, Meta.
```
Antes de la rúbrica, tabla de verdad con TODO texto en pantalla:
| t | Texto | Tipo (REAL / EJEMPLO / marca / copy) | Fuente (archivo:línea) | Estado |
Estados: CONFIRMADO · PARCIAL (la fuente dice menos) · NO ENCONTRADO · CONTRADICE. Todo lo no CONFIRMADO es P0 hasta que el research lo documente o el texto cambie.
Flags legales (aunque esté en la tabla): superlativos ("el mejor", "#1"), comparativos, garantías, cifras sin descargo, testimonios sin nombre y permiso, antes/después. Cada uno es P0 o pregunta para Yeyow.
```

### M4. Sesgos del Juez (sección nueva + § Errores comunes)
Brecha: el rol no nombra los sesgos medidos en jueces LLM; el Juez es el mismo modelo que el Editor. Fuente: Zheng, Wang, Panickssery, `named-persona`.
```
## Sesgos conocidos y qué hago
- Posición: lo primero pesa más. Segunda pasada de atrás hacia adelante (cierre → intro). Los cuadros se eligen por regla (0, 1,5 s, golpes, cortes, CTA), nunca "los que me llamaron".
- Longitud: una línea más larga o una escena más llena no es "más completa". Manda el tiempo de lectura.
- Autopreferencia: no leo las razones del Editor; escribo la evidencia antes del veredicto; busco señales de que la corrección falló.
- Dos variantes (A/B): juzgo a ciegas y repito con el orden invertido; si el veredicto cambia, es empate y decide Yeyow.
```

### M5. Tres pasadas con herramientas, no de oído (§ Proceso 1, criterio 7)
Brecha: "con y sin sonido" existe, pero sin tamaño de feed ni chequeo numérico del audio. Fuente: Anthropic (lo medible se mide con código); `cues.py`.
```
1. Sin sonido, a tamaño de feed: `ffmpeg -i borrador.mp4 -vf "fps=1,scale=270:-1,tile=8x4" qa/feed.png`. ¿Se leen gancho y CTA? Si no, P0.
2. Con sonido, una vez, sin pausar. Anotar "me iría en".
3. Solo audio con números: en `cues.json`, cada golpe (`boom`, `hit`) a ≤0,034 s de k·0,5 s (120 BPM); SFX 0–0,1 s antes de su animación. Lo que falla, hallazgo con el número.
```

### M6. Ficha para el teléfono (§ Ficha para PUERTA 4)
Brecha: la ficha es texto largo y Yeyow aprueba desde WhatsApp. Fuente: `requesting-code-review`, `named-persona`, regla de intake.
```
## Mira esto — qa/ficha.png
Una columna 9:16 con 3–5 cuadros, el t quemado en cada uno (`drawtext`).
## Solo tú decides (≤4, la recomendada primero)
1. ¿Resumen? a) 2 s como está (recomendado: el cierre no pierde) · b) 2,5 s quitando 0,5 s al cierre
Responde "1a 2b ok" y listo.
## Lo que dejé fuera a conciencia
- t · qué · por qué no es hallazgo. Vacío = no dejé nada fuera.
## Por qué APROBADO
3+ cosas verificadas con su número (no "se ve bien").
```

### M7. Casos de calibración: el Juez aprende de los videos anteriores (§ Lecciones de Korvin #4)
Brecha: las lecciones están en prosa y nadie mide si el Juez acierta. Fuente: Hamel `validate-evaluator`, `grader.md`, Zheng.
```
Archivo `_studio/metodo/juez-casos.md` (el Juez lo lee antes de juzgar; máx. 20 filas, las viejas se condensan):
| Video | t | Criterio | Hallazgo | Juez | Yeyow | Acuerdo | Lección |
Juez = P0/P1/P2/no visto · Yeyow = confirmó / no le importó / lo pidió él.
Al cerrar cada video el Editor agrega los P0 del Juez (¿Yeyow los confirmó?) y las notas de Yeyow que el Juez no vio (las que más importan).
Dos números en `05-revision.md`: P0 confirmados / totales · notas de Yeyow no vistas.
Si Yeyow descarta dos veces el mismo tipo de P0, ese ancla pasa a BORDE. Si un criterio del brief no se cumple sin romper otro (caso #4), es hallazgo contra el brief, no contra el Editor.
```

### M8. Vuelta 2 con evidencia y regresión (§ Proceso 7)
Brecha: "revisar solo lo tocado" no exige probar que lo demás no cambió. Fuente: `verification-before-completion`, Playwright.
```
Vuelta 2:
- Cada P0 se cierra volviendo a extraer el MISMO cuadro (mismo t) y midiendo lo mismo. "Lo movieron" no cierra; el número sí.
- Regresión: `qa/contacto.png` vuelta 1 vs 2, diff de píxeles por cuadro (numpy). Escena no tocada con >1 % distinto = hallazgo nuevo permitido.
- Parto de que la corrección NO funcionó hasta ver el cuadro.
```

## 3. Lo que NO conviene adoptar
- **Escala 1–5 o 1–10 por criterio** (`skill-creator/comparator`, `llm-evaluation`): nadie acuerda qué separa un 3 de un 4 (Hamel); la severidad ya es P0/P1/P2.
- **"Cada revisor DEBE hallar ≥1 problema"** (`adversarial-reviewer`): obliga a inventar. Lo correcto es la carga del cero (M6).
- **5 revisores paralelos + agente filtro** (`code-review`): cuesta más que el reel; un Juez con M2 basta. Dos revisores solo si Yeyow lo pide.
- **Personas con nombre** (Torvalds, Jobs…): lentes de código, no de video.
- **WCAG completa**: teclado y foco no aplican a un reel; solo el contraste 4,5:1 para el criterio 4.

## 4. No verificado
- skillsmp.com no devolvió resultados (JS); claudemarketplaces.com sí. `pm-thought-partner/build-judge` no se pudo clonar; `onewave-ai/brand-consistency-checker` y `jamditis/fact-check-workflow` sin licencia visible, no clonados.
- Los sesgos de Zheng, Wang y Panickssery están medidos en texto, no en video; se asume que aplican.
- "La mayoría ve sin sonido": sin fuente primaria; la pasada sin sonido se mantiene por criterio propio.
- Meta "unrealistic outcomes" cubre salud y empleo; no leí la norma general de claims (los flags de M3 salen de `brand-review`).
- Un `model` distinto para el Juez bajaría la autopreferencia en teoría; no lo medí. Survey LLM-as-a-Judge (arXiv 2411.15594): solo el resumen.
