#!/usr/bin/env python3
"""
Candado de puertas del flujo korvex-motion (hook PreToolUse de Claude Code para Write|Edit|MultiEdit).

Lee el JSON del hook por stdin y BLOQUEA (exit 2 + motivo en stderr) cuando se intenta:
  - escribir 03-guion.md            sin 02-brief.md aprobado por Yeyow          (PUERTA 1)
  - escribir index.html / music.py  sin 03-guion.md aprobado por Yeyow          (PUERTA 2)
  - escribir en <CLIENTE>/entregas/ el video NN sin 05-revision.md APROBADO     (PUERTA 4)
Solo aplica a videos del flujo nuevo (los que tienen 02-brief.md). Los videos viejos (solo plan.md) no se tocan.
Ante cualquier error de lectura deja pasar (exit 0): el candado nunca debe romper otro trabajo.

Prueba manual:
  echo '{"tool_name":"Write","tool_input":{"file_path":"KORVIN/videos/04-x/index.html"}}' | python _studio/tools/gate_check.py
"""
import json, re, sys, pathlib


def fm(path):
    """frontmatter YAML simple -> dict (clave: valor sin comentario)."""
    try:
        t = path.read_text(encoding='utf-8')
    except Exception:
        return None
    m = re.match(r'^---\s*\n(.*?)\n---', t, re.S)
    if not m:
        return {}
    d = {}
    for ln in m.group(1).splitlines():
        mm = re.match(r'^(\w+):\s*(.*?)\s*(#.*)?$', ln)
        if mm:
            d[mm.group(1)] = mm.group(2).strip().strip('"').strip("'")
    return d


def aprobado(path):
    d = fm(path)
    if d is None:
        return False, f'falta {path.name}'
    ok = d.get('aprobado', '').lower() in ('true', 'si', 'sí', 'yes') and d.get('aprobado_por', '').strip() != ''
    return ok, '' if ok else f'{path.name} no tiene "aprobado: true" + "aprobado_por: Yeyow"'


def block(msg):
    sys.stderr.write('PUERTA CERRADA (korvex-motion): ' + msg +
                     '\nPresenta el documento a Yeyow y espera su aprobacion (/korvex-motion:aprobar). No escribas la aprobacion por tu cuenta.\n')
    sys.exit(2)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    ti = data.get('tool_input') or {}
    fp = ti.get('file_path') or ti.get('path') or ''
    if not fp:
        sys.exit(0)
    p = pathlib.Path(fp)
    if not p.is_absolute():
        p = pathlib.Path(data.get('cwd') or '.') / p
    parts = [x.lower() for x in p.parts]
    name = p.name.lower()

    # ---- archivos dentro de <CLIENTE>/videos/<NN-nombre>/
    if 'videos' in parts:
        i = len(parts) - 1 - parts[::-1].index('videos')
        if len(p.parts) <= i + 2:
            sys.exit(0)                                       # no es un archivo dentro de videos/NN-nombre/
        vdir = pathlib.Path(*p.parts[:i + 2])
        if not (vdir / '02-brief.md').exists():
            sys.exit(0)                                       # video del flujo viejo: sin candado
        if name == '03-guion.md':
            ok, why = aprobado(vdir / '02-brief.md')
            if not ok:
                block(f'PUERTA 1 — {why}. El guion se escribe despues de aprobar el brief.')
        if name in ('index.html', 'music.py'):
            ok, why = aprobado(vdir / '03-guion.md')
            if not ok:
                block(f'PUERTA 2 — {why}. El video se construye despues de aprobar el guion.')
        sys.exit(0)

    # ---- entregas: <CLIENTE>/entregas/<cliente>-NN-....
    if 'entregas' in parts:
        i = len(parts) - 1 - parts[::-1].index('entregas')
        cdir = pathlib.Path(*p.parts[:i])
        m = re.search(r'-(\d{2})-', name)
        if not m:
            sys.exit(0)
        cands = sorted((cdir / 'videos').glob(m.group(1) + '-*')) if (cdir / 'videos').exists() else []
        for vdir in cands:
            if (vdir / '02-brief.md').exists():
                d = fm(vdir / '05-revision.md') or {}
                if d.get('veredicto_yeyow', '').upper() != 'APROBADO':
                    block(f'PUERTA 4 — {vdir.name}/05-revision.md no dice "veredicto_yeyow: APROBADO". '
                          'La entrega final va despues de que Yeyow apruebe el borrador.')
        sys.exit(0)
    sys.exit(0)


if __name__ == '__main__':
    main()
