# Propuestas para el rol Productor — research en marketplaces (03/10/2026)

Revisión de marketplaces de skills para mejorar `rol-productor.md` y `agents/productor.md`. Solo propuestas; no se tocó el método. No se repiten las fuentes del 02/10. Caso de prueba: `KORVIN/videos/04-como-funciona/02-brief.md`.

## 1. Skills revisadas

| Skill | Repo | Lic. | Qué hace | Veredicto |
|---|---|---|---|---|
| `creative-director` | [smixs/creative-director-skill](https://github.com/smixs/creative-director-skill) | CC BY 4.0 | Insight con tensión; 8–12 ideas; 6 criterios ponderados; prueba del competidor; pre-mortem | **Adoptar** insight, matriz, pre-mortem; no su biblioteca de campañas |
| `creative-strategy-engine` · `creative-mechanics` · `brand-intake` | [motion-team/creative-strategy-skills](https://github.com/motion-team/creative-strategy-skills) | MIT | Dolor × persona = ángulo; 5 etapas de conciencia; 8 mecánicas con nombre | **Adoptar** ángulo, 3 etapas, mecánicas |
| `creative-roadmap.md` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/main/skills/ad-creative/references/creative-roadmap.md) (no visto el 02/10) | MIT | Evidencia en 6 niveles; producción T1/T2/T3; retro "juzga conceptos, no anuncios" | **Adoptar** niveles y retro |
| `product-position` · `motion-picture` | [firatcand/founder-skills](https://github.com/firatcand/founder-skills) | MIT | Dunford (alternativas incl. "no hacer nada"), Raskin (por qué ahora), Laja; prueba sin sonido | **Adoptar** alternativa y por qué ahora |
| `pitch-position` · `pitch-message` | [jeremylongshore/… tonone](https://github.com/jeremylongshore/claude-code-plugins-plus-skills/tree/main/plugins/ai-agency/tonone) | MIT | UNA alternativa principal; pruebas "¿y qué?" y "suena como todos" | **Adoptar** las pruebas |
| `product-brainstorming` | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management) | Apache-2.0 | Diverge → provoca → converge; "¿quién odiaría esto?", "quitar algo", inversión | **Adoptar** provocaciones |
| `brainstorming` | [obra/superpowers](https://github.com/obra/superpowers) | MIT | Visual solo si la pregunta es visual; se aprueba lo presentado; auto-revisión | **Adoptar** |
| `naming/evaluation.md` | [glacierphonk/naming](https://github.com/glacierphonk/naming) | MIT | Puerta previa → rúbrica ponderada 1–5 | **Adoptar** la estructura |
| `vox-director` | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | MIT | Bake-off de estilos: "la IA propone, el humano elige a ojo" | Idea para la hoja de ganchos |
| `campaign-plan` · `brand-review` · `content-strategy` (instaladas) | knowledge-work-plugins | Apache-2.0 | KPI con número y cadencia; claims sin sustento | Parcial; `brand-review` es del Juez |
| `positioning-basics` · `copywriter` (Ralph) | [brianrwagner](https://github.com/brianrwagner/ai-marketing-claude-code-skills) · [muratcankoylan](https://github.com/muratcankoylan/ralph-wiggum-marketer) | MIT (el 2.º sin LICENSE) | "Ellos ganan cuando"; "¿lo publicaría tal cual?" | Parcial |
| `creative-brief-framework` · `creative-strategy` · `brand-strategist` · `video-content-strategist` · `content-marketer` | gtm-agents · omer-metin/skills-for-antigravity · borghei · alirezarezvani · wshobson, VoltAgent, davila7 | Apache / MIT | Plantillas de 30 líneas, genéricos o espejos de marketingskills | **Descartar** |

## 2. Mejoras concretas al rol de hoy

### 2.1 El mensaje se escribe contra UNA alternativa y dice por qué ahora
**Brecha:** el paso 2 fija el mensaje sin preguntar contra qué compite; § 1 pide "por qué ahora" sin método. En Korvin 04 la alternativa ("contestar yo mismo", "un bot que inventa") quedó implícita.
**Pegar al final del paso 2:**
```
- Nombra la alternativa principal: lo que el dueño hace HOY en vez del producto (contestar a mano, una
  secretaria, respuestas automáticas, otro bot, nada). UNA sola; contra todas, el mensaje no le llega a nadie.
- El mensaje dice qué cambia frente a esa alternativa, en palabras del dueño.
- Prueba "suena como todos": pon un competidor en la frase. ¿Sigue valiendo? No es mensaje.
- "Por qué ahora" en una línea: qué cambió en el mundo del dueño (del research). Si no hay, se omite.
```
**Fuente:** founder-skills `product-position`; tonone `pitch-position`; motion-team `brand-intake`.

### 2.2 Insight con tensión antes de los conceptos
**Brecha:** la frase Get/Who/To/By lleva el insight sin prueba de calidad; a veces es una descripción, no una tensión.
**Pegar en el paso 1, después de la frase:**
```
- La tensión en una línea: "<audiencia> quiere <X>, pero <Y> se lo impide, porque <Z>".
  Tipos: de categoría (lo que prometen los bots vs lo que hacen) · humana (descansar vs miedo a perder
  clientes) · cultural (lo que se dice vs lo que se hace).
- Prueba: ¿el dueño diría "sí, exacto, pero nunca lo había dicho así"? Si cualquier marca lo sabe, cava más.
- Cada concepto se ata a esa tensión; el que no la toca, se cae.
```
**Fuente:** smixs (reescrito).

### 2.3 Ronda de conceptos más fuerte
**Brecha:** el paso 4 pide 5 conceptos por 5 caminos; no dice cómo escapar de los obvios ni qué mecanismo usa cada uno.
**Pegar en los pasos 4–5:**
```
- Genera 8 en privado; los 3 primeros son calentamiento. Los 5 que se muestran salen sobre todo del 4 al 8.
- Tres provocaciones antes de cerrar: "¿quién odiaría este video?" · "la versión que QUITA algo (sin chat,
  sin texto, sin pasos)" · "¿cómo sería el peor video de este tema?" → invertirlo.
- Cada concepto nombra su mecánica (cómo llega el espectador al mensaje): respuesta implícita (pregunta +
  la imagen contesta) · testigo · contraste sin comentario · reencuadre ("no es X, es Y") · el formato es la idea.
- Prueba de especificidad: cambia KORVIN por un competidor. ¿Igual? Es genérico.
```
**Fuente:** smixs; knowledge-work `product-brainstorming`; motion-team `creative-mechanics`.

### 2.4 Puntuar antes de recomendar
**Brecha:** la tabla solo lleva "Prob. típica" y la recomendación una razón. Sin puerta ni matriz, se recomienda por olfato.
**Pegar como sección privada "Puntaje" (a Yeyow se le muestra el resultado, no la tabla):**
```
Puerta (un "no" descalifica): un mensaje · todo claim con fuente en § 7 · assets que existen o alguien
consigue · silueta distinta · cabe en la duración · es un video, no una campaña.
Matriz 1–5: Específico ×3 (prueba del competidor) · Gancho en el cuadro 1 ×3 (se ve y se lee en 1,5 s) ·
Trazable al mensaje ×2 · Emoción concreta ×2 (alivio, orgullo, vergüenza ajena; no "positivo") ·
Factible en el motor ×2 (kit, assets, horas) · Sirve para serie ×1. Máx. 65.
Recomendación = el más alto; si Yeyow pidió "sorpréndeme", el más alto con Específico ≥4.
Abogado del diablo: una línea en contra del recomendado. Si pesa más que el concepto, cambia.
```
**Fuente:** smixs ("mata a tus favoritos"); `naming`; `creative-roadmap.md` (evidencia antes de prioridad).

### 2.5 PUERTA 1 para decidir desde el teléfono
**Brecha:** la tabla de 5 columnas se rompe en el teléfono. No dice qué se descartó ni qué va en contra del recomendado.
**Reemplazar el bloque "Cómo se presenta la PUERTA 1":**
```
Este video le dice a <audiencia> que <mensaje>. Contra: <alternativa>.

1. **<Nombre>** — <qué pasa, una frase>.
   Cuadro 1: "<texto>" + <qué se ve>. · <receta · tono · s>
2. … (3–5; el recomendado nunca va primero)

Descartados: <2–3, media línea cada uno, por qué no>.
Recomiendo el <n>: <razón>. En contra: <abogado del diablo>.
El Juez va a medir: <5 criterios>.
Responde con el número, "mezcla 2+4", "dale", o lo que cambias.
```
Opcional, si los conceptos se distinguen por imagen: `hoja-ganchos.html` → PNG con el cuadro 1 de cada concepto (texto y marca reales), 3–5 miniaturas en fila.
**Fuente:** superpowers; vox-director (bake-off a ojo); smixs ("descartados").

### 2.6 Series y variantes como parte del método
**Brecha:** Korvin 04 inventó sobre la marcha la tabla "Lo que cambia por versión"; el rol no la contempla, ni dice cuánto cuesta cada variante ni a qué etapa del espectador habla.
**Pegar en el frontmatter y como § 4b de la plantilla:**
```
versiones: [] · piloto: · etapa: problema | solucion | producto   # qué sabe ya el espectador

## 4b. Variantes (si versiones > 1)
- Una estructura, una tabla. Cambian solo las filas: preguntas R1 · ejemplo · dato del negocio · final real · CTA.
- Nivel: N1 cambiar textos/ejemplo (horas) · N2 misma receta, otra categoría o cliente (días) ·
  N3 concepto nuevo (es otro brief).
- Ángulo = dolor × persona: el mismo dolor dicho por el rent-a-car y por el salón son dos ángulos.
- A/B (ads): cambia UNA variable, casi siempre el gancho; la rampa se reescribe, no se pega.
```
**Fuente:** motion-team `creative-strategy-engine`; `creative-roadmap.md` (T1/T2/T3); iart (02/10).

### 2.7 Orgánico vs ad: lo que cambia en el brief
**Brecha:** `uso:` solo mueve la zona segura y el CTA. Etapa, gancho, variantes, KPI y caption se deciden igual.
**Pegar al final del paso 8:**
```
| | organico | ad |
|---|---|---|
| etapa | problema o solución | producto (ya saben que existe) |
| gancho | pregunta/observación del dueño | promesa que el CTA paga |
| CTA | suave: guárdalo, pregúntame | verbo + beneficio, ≥2,5 s, por encima de y≈1250 |
| variantes | 1 video o serie por categoría | 3–5 ganchos, resto igual |
| KPI a 7 días | % que llega al final, guardados y envíos por alcance | vistas 3 s/impresiones · 15 s/3 s · CTR · costo por mensaje |
| caption | 1–3 frases + 3–5 hashtags | la promesa del gancho en una línea |
```
**Fuente:** motion-team (etapas); `categorias.md` § KPIs; `creative-roadmap.md` ("lee el embudo, no el ROAS").

### 2.8 Riesgos como pre-mortem y una sección de medición
**Brecha:** § 12 es libre ("4 renders de 14 min") y el brief termina al aprobar: nadie anota qué pasó con el video ni qué aprendimos.
**Reemplazar § 12 y añadir § 16:**
```
## 12. Pre-mortem (imagina que salió y falló: ¿por qué?)
- Marca: ¿el producto hace de verdad lo que se ve? ¿Un escéptico ve hueco entre promesa y producto?
- Gente: ¿quién podría sentirse burlado (el dueño caricaturizado, la empleada "reemplazada")?
- Producción: ¿qué asset o módulo, si falla, tumba el concepto? Plan B.
- Métrica: ¿produce el KPI de la categoría o uno que no podemos reportar?
Veredicto: sigue / revisa / mata.

## 16. Medición y aprendizaje (7 días después de publicar)
- KPI principal (categorias.md) y el número, comparado con nuestros videos, no con blogs.
- Qué ganó / qué perdió y por qué (gancho, rampa, oferta). Juzga el concepto, no un render:
  un video flojo no mata la idea; tres sí.
- Qué va a la tabla Serie del perfil: repetir · variar · retirar.
```
Checklist de "listo": añadir "Auto-revisión: sin TBD, sin contradicciones entre § 3 y § 4, cada criterio con un solo sentido".
**Fuente:** smixs (pre-mortem); `creative-roadmap.md` (retro); knowledge-work `campaign-plan` (KPI con número y cadencia); superpowers (auto-revisión).

## 3. Lo que NO conviene adoptar

- **smixs completo** (569 campañas, escalas Cannes/HumanKind, 5 pasadas hasta 9+): son reels de 20 s para pymes; manda verdad + específico, no premio. Costaría más que el video.
- **`motion-picture`: "si abre con logo, falla".** Choca con la marca desde el cuadro 0; R1 es marca y gancho a la vez.
- **motion-team `hook-tactics` / `visual-formats`** (35 tácticas, 45 formatos de Meta, en inglés): son del Guionista/Editor; ya hay recetas.
- **`campaign-plan`** es para campañas multicanal, no para un video; **`brand-review`** le sirve al Juez. **Cinco etapas de conciencia:** con un canal, tres bastan.
- **gtm-agents, antigravity, borghei, davila7, alirezarezvani:** genéricos o espejos; borghei con Commons Clause.

## 4. No verificado

- Cifras de retención en vox-director ("65 % decide en 3 s") y `video-content-strategist` ("85 % ve sin sonido"): sin fuente primaria; no entran.
- La matriz de 2.4 (pesos, máximo 65) es adaptación nuestra: calibrar con los primeros 3 briefs. Los pesos de smixs son práctica del autor, no un estudio.
- `paid-media-creative-strategist` (stevenke1981) y `master-creative-director` (0xzgbot) en claudskills.com: solo vistos en el directorio; no se clonaron.
- ComposioHQ `competitive-ads-extractor`: ejemplo inventado, sin LICENSE.
- `gh api` no permite buscar código desde este sandbox; todo se revisó con `git clone --depth 1` y directorios web (claudemarketplaces.com, claudskills.com; skillsmp.com no dio resultados propios).
