# CLAUDE.md: estudio Korvex Motion

Aquí se hacen videos de motion graphics en código para los clientes de Yeyow. Habla con Yeyow en español, directo e informal. Usa términos técnicos en español básico.

## Antes de cualquier cosa
- Lee `README.md` (cómo se trabaja), `PRODUCTOS.md` (clientes) y el `perfil.md` del cliente con el que vas a trabajar.
- El motor está en `_studio/` y su manual en `_studio/README.md`. El método de cada rol está en `_studio/metodo/`.
- Para cualquier video nuevo usa el flujo del plugin **korvex-motion**: `/korvex-motion <idea>` → intake con preguntas → investigador → productor (PUERTA 1) → guionista (PUERTA 2) → editor + QA + juez → PUERTA 4 → entrega.

## Reglas
1. **Una carpeta por cliente.** Nunca uses logos, fotos, datos ni copy de otro cliente. Los proyectos de los clientes (su código, su web, sus carpetas) son de **solo lectura**.
2. **No inventes.**
   - Funciones, cifras, testimonios, clientes y precios salen del perfil, de la web/código del cliente o de Yeyow.
   - Lo generado va con "Imágenes conceptuales" y los datos de ejemplo con "EJEMPLO" / "DATOS DE DEMOSTRACIÓN".
3. **Intake primero:** preguntas con opciones, ≤4 por ronda, la recomendada primero. No preguntes lo que el perfil ya responde.
4. **Puertas:**
   - Nunca escribas `aprobado: true`, `aprobado_por` ni `veredicto_yeyow: APROBADO` sin que Yeyow lo haya dicho en esta conversación (o usado `/korvex-motion:aprobar`).
   - Una corrección no es una aprobación.
   - Si el hook `gate_check.py` bloquea algo, presenta la puerta y espera. No lo esquives.
5. **Marca desde el cuadro 0:** todo video abre con el intro de marca (receta R1), salvo un bumper.
6. **Determinismo:** todo sale de `window.seek(t)`. Nada de `requestAnimationFrame`, `Date` ni `Math.random` sin semilla. Los estados del cuadro 0 van con `gsap.set` inmediato.
7. **Calidad antes de entregar:**
   - `qa.py` sin FAIL;
   - texto en la zona segura;
   - -14 LUFS / ≤ -1 dBTP (`synth.master_lufs`);
   - ≤20 MB;
   - el poster es un cuadro asentado y con marca.
8. **El render final se hace en esta misma máquina.** Los borradores salen con `--draft`.
9. **Nunca uses `pkill -f`** con un patrón que esté en tu propio comando. Usa el PID.
10. **Al entregar,** actualiza la serie, la tabla Huella y el copy aprobado en el `perfil.md` del cliente, `PRODUCTOS.md` y el README si cambió algo del motor.
11. **Que un cliente no se vea siempre igual:** repetir gancho, receta o método se vale, y una estructura de un cliente sirve para otra marca. Lo que rota es el look de cada cliente (técnica firma, transiciones, forma del motion): hasta 3–4 videos seguidos y después cambia. El registro es la tabla Huella del perfil (`rol-productor.md`, paso 3b). El catálogo de técnicas (`_studio/refs/tendencias.md`) lo actualiza el Investigador dentro del research cuando tiene más de 30 días. Apify va por defecto (Yeyow, 03/10/2026).

## Comandos frecuentes (desde `<CLIENTE>/videos/NN-nombre/`)
```bash
python ../../../_studio/preview.py index.html prev.png 1,5,10 6
python ../../../_studio/cues.py index.html cues.json && python music.py
python ../../../_studio/render.py --html index.html --out borrador.mp4 --workers 4 --draft --audio music.wav
python ../../../_studio/tools/qa.py --video borrador.mp4 --html index.html --out qa
python ../../../_studio/render.py --html index.html --out master.mp4 --w 1080 --h 1920 --fps 30 --sub 4 --workers 4 --audio music.wav
python ../../../_studio/tools/deliver.py --video master.mp4 --poster-t <s> --out ../../entregas/<cliente>-NN-nombre.mp4
```
