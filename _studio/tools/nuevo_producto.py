#!/usr/bin/env python3
"""Crea la carpeta de un producto nuevo a partir de _PLANTILLA-PRODUCTO.
Uso (desde MOTIONS DESIGN):  python _studio/tools/nuevo_producto.py KORVEXCIO"""
import sys, shutil, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
name = sys.argv[1].strip().upper().replace(' ', '-')
dst = root / name
if dst.exists():
    sys.exit(f'Ya existe {dst} — no se toca.')
shutil.copytree(root / '_PLANTILLA-PRODUCTO', dst)
for f in ('perfil.md', 'marca.js'):
    p = dst / f
    t = p.read_text(encoding='utf-8').replace('NOMBRE-DEL-PRODUCTO', name).replace("'NOMBRE'", f"'{name.title()}'")
    if f == 'perfil.md':  # quita la nota de plantilla y deja la regla de la carpeta
        lines = [l for l in t.splitlines() if not l.startswith('>')]
        lines.insert(1, f'\n> Todo lo de {name} sale de esta carpeta: este perfil, `marca.js`, `logos/` y `assets/`.\n> No uses nada de la carpeta de otro producto.')
        t = '\n'.join(lines) + '\n'
    p.write_text(t, encoding='utf-8')
print(f'Listo: {dst}  -> llena perfil.md y marca.js, pon los logos en logos/ y los assets en assets/')
