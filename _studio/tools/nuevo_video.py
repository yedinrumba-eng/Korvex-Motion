#!/usr/bin/env python3
"""
Crea la carpeta de un video nuevo con las plantillas del flujo korvex-motion (01-research … 05-revision).

Uso (desde MOTIONS DESIGN):
  python _studio/tools/nuevo_video.py PANADERIA-EJEMPLO "receta-boda" --idea "un reel de la receta de una mesa de boda"
  -> PANADERIA-EJEMPLO/videos/04-receta-boda/ con 01-research.md … 05-revision.md (NN = siguiente de la serie)
"""
import argparse, pathlib, re, sys, datetime
root = pathlib.Path(__file__).resolve().parents[2]
ap = argparse.ArgumentParser()
ap.add_argument('cliente'); ap.add_argument('nombre'); ap.add_argument('--idea', default='')
a = ap.parse_args()
cli = a.cliente.strip().upper().replace(' ', '-')
cdir = root / cli
if not (cdir / 'perfil.md').exists():
    sys.exit(f'No existe {cdir}/perfil.md. Crea el cliente primero: python _studio/tools/nuevo_producto.py {cli}')
vids = cdir / 'videos'; vids.mkdir(exist_ok=True)
nums = [int(m.group(1)) for d in vids.iterdir() if d.is_dir() and (m := re.match(r'(\d{2})-', d.name))]
slug = re.sub(r'[^a-z0-9]+', '-', a.nombre.lower()).strip('-')
nn = f'{(max(nums) + 1) if nums else 1:02d}'
vdir = vids / f'{nn}-{slug}'
vdir.mkdir()
for t in sorted((root / '_studio' / 'plantillas').glob('0*.md')):
    txt = t.read_text(encoding='utf-8').replace('{{CLIENTE}}', cli).replace('{{VIDEO}}', vdir.name).replace('{{IDEA}}', a.idea.replace('"', "'"))
    (vdir / t.name).write_text(txt, encoding='utf-8')
(vdir / 'qa').mkdir()
print(f'Listo: {vdir}')
print('Siguiente: intake (preguntas) -> 01-research.md -> 02-brief.md (PUERTA 1) -> 03-guion.md (PUERTA 2) -> build -> PUERTA 4')
