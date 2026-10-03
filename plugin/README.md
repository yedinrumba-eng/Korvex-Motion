# korvex-motion (plugin de Claude Code)

El estudio de motion graphics de Korvex Motion con un flujo spec-driven por roles. Trabaja sobre la carpeta de este repo.

## Instalar en Claude Code
```text
/plugin marketplace add yedinrumba-eng/korvex-motion
/plugin install korvex-motion@korvex
```
Reinicia Claude Code y abre la sesión **en la carpeta del repo** (clonado), porque el flujo usa rutas relativas a esa carpeta. Antes, corre `python _studio/setup/get_gsap.py`.

## Qué trae
| Pieza | Qué hace |
|---|---|
| Skill `korvex-motion` | El orquestador: `/korvex-motion <idea o referencia>` |
| Agentes `investigador`, `productor`, `guionista`, `editor`, `juez` | Un rol cada uno. El método completo de cada rol está en `_studio/metodo/rol-*.md` |
| `/korvex-motion:aprobar brief\|guion\|video [notas]` | Tu aprobación de una puerta |
| `/korvex-motion:cambios <fase> "notas"` | Pides cambios; se clasifican y se rehace solo lo nombrado |
| `/korvex-motion:estado [CLIENTE]` | En qué puerta va cada video |
| `/korvex-motion:nuevo-cliente NOMBRE [ruta/web]` | Alta de un cliente nuevo |
| `/korvex-motion:radar [CLIENTE \| ig c1 c2 c3 \| estados]` | Radar de tendencias: actualiza `_studio/refs/tendencias.md` y propone técnicas que no se han repetido |
| Hook `gate_check.py` | No deja escribir el guion, el video ni la entrega final sin tu aprobación |

El hook necesita `python` en el PATH de Windows. Prueba que funcione con:
```text
echo {"tool_name":"Write","tool_input":{"file_path":"X/videos/01-a/index.html"}} | python _studio\tools\gate_check.py
```

## Actualizar
Cuando se modifiquen los archivos del plugin: `/plugin marketplace update korvex` y después `/plugin update korvex-motion@korvex`.
