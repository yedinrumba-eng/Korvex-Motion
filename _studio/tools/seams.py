#!/usr/bin/env python3
"""
Costuras medidas: revisa cada costura (transicion) de un video con la ley del vector.

Uso (desde <CLIENTE>/videos/NN-nombre/):
  python ../../../_studio/tools/seams.py --html index.html [--out qa/seams.json]

Lee window.SEAMS = [{t, out, in, axis: 'x'|'y'|'z', dir: -1|1}, ...] (K.cut las registra solas; una costura hecha
a mano se registra con window.SEAMS.push({...}) usando selectores CSS). Para cada costura mide con Playwright, en
t-2/30, t-1/30, t, t+1/30 y t+2/30, el getBoundingClientRect (centro y escala aproximada) y la opacidad efectiva
(la del elemento por la de sus ancestros) del que sale (A) y del que entra (B).

FAIL si:
  - A no se mueve en [t-2/30, t] o B no se mueve en [t, t+2/30]   (el corte va con los dos a mitad de vuelo)
  - la direccion no cuadra con axis/dir: en x/y el desplazamiento va en el signo de dir y domina el otro eje;
    en z el signo del cambio de escala es dir (dir -1: A se encoge y B llega grande y baja a 1; dir +1: al reves)
  - A y B estan legibles a la vez (opacidad efectiva > 0,6 los dos) en t-1/30, t o t+1/30 (doble exposicion)
Imprime una tabla, escribe el JSON y termina con codigo 1 si hay algun FAIL.
"""
import argparse, json, pathlib, sys
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument('--html', required=True)
ap.add_argument('--out', default='qa/seams.json')
ap.add_argument('--fps', type=float, default=30.0, help='un cuadro = 1/fps s (las muestras van a ±1 y ±2 cuadros)')
ap.add_argument('--min-px', type=float, default=2.0, help='desplazamiento minimo para contar como movimiento')
ap.add_argument('--min-scale', type=float, default=0.01, help='cambio de escala minimo para contar como movimiento')
ap.add_argument('--legible', type=float, default=0.6, help='opacidad efectiva a partir de la cual algo se lee')
a = ap.parse_args()

MEASURE = """(sel) => {
  let els = []; try { els = [...document.querySelectorAll(sel)]; } catch (e) { return null; }
  if (!els.length) return null;
  const opa = el => { if (getComputedStyle(el).visibility === 'hidden') return 0;
    let o = 1; for (let e = el; e && e.nodeType === 1; e = e.parentElement) { const cs = getComputedStyle(e);
      if (cs.display === 'none') return 0; o *= parseFloat(cs.opacity); } return o; };
  let l = 1e9, t = 1e9, r = -1e9, b = -1e9, op = 0, sc = null;
  for (const el of els) { const q = el.getBoundingClientRect();
    l = Math.min(l, q.left); t = Math.min(t, q.top); r = Math.max(r, q.right); b = Math.max(b, q.bottom);
    op = Math.max(op, opa(el));
    if (sc === null && el.offsetWidth) sc = q.width / el.offsetWidth; }
  return { n: els.length, cx: (l + r) / 2, cy: (t + b) / 2, w: r - l, h: b - t, scale: sc, op };
}"""

html = pathlib.Path(a.html).resolve()
F = 1.0 / a.fps
KS = (-2, -1, 0, 1, 2)
sgn = lambda v: (v > 0) - (v < 0)

with sync_playwright() as p:
    b = p.chromium.launch(args=['--force-device-scale-factor=1', '--font-render-hinting=none', '--hide-scrollbars'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1920}, device_scale_factor=1)
    msgs = []
    pg.on('pageerror', lambda e: msgs.append('ERR ' + str(e)))
    pg.goto(html.as_uri())
    try:
        pg.wait_for_function('() => typeof window.seek === "function" && window.READY === true', timeout=60000)
    except Exception:
        print('la pagina no quedo READY', msgs[:10]); b.close(); sys.exit(2)
    pg.evaluate('document.fonts.ready.then(() => 0)')
    pg.evaluate('Promise.all([...document.fonts].map(f => f.load().catch(() => 0))).then(() => 0)')   # todas las fuentes, como render.py
    pg.wait_for_timeout(200)
    seams = pg.evaluate('JSON.parse(JSON.stringify(window.SEAMS || []))')
    res = []
    for i, s in enumerate(seams):
        t0 = float(s['t'])
        smp = {}
        for k in KS:
            pg.evaluate('t => { window.seek(t); }', t0 + k * F)
            smp[k] = {'t': round(t0 + k * F, 4), 'out': pg.evaluate(MEASURE, s['out']), 'in': pg.evaluate(MEASURE, s['in'])}
        res.append({'i': i + 1, **s, 'samples': smp})
    pg.evaluate('() => { window.seek(0); }')
    b.close()


def motion(m0, m1, axis):
    """Desplazamiento de m0 a m1: en el eje pedido, en el otro eje y en escala relativa."""
    dx, dy = m1['cx'] - m0['cx'], m1['cy'] - m0['cy']
    ds = (m1['w'] / m0['w'] - 1) if m0['w'] > 0 else 0.0
    if axis == 'y':
        return dy, dx, ds
    return dx, dy, ds


fails = 0
for r in res:
    S, axis, d = r['samples'], r.get('axis', 'x'), (1 if r.get('dir', -1) > 0 else -1)
    why = []
    if any(S[k]['out'] is None for k in KS) or any(S[k]['in'] is None for k in KS):
        why.append(f"no encuentro {'sale ' + r['out'] if S[0]['out'] is None else 'entra ' + r['in']} en la pagina")
        r['mov'] = None
    else:
        mo = motion(S[-2]['out'], S[0]['out'], axis)      # A: los 2 cuadros antes del corte
        mi = motion(S[0]['in'], S[2]['in'], axis)         # B: los 2 cuadros despues del corte
        r['mov'] = {'sale': {'eje': round(mo[0], 2), 'otro': round(mo[1], 2), 'escala': round(mo[2], 4)},
                    'entra': {'eje': round(mi[0], 2), 'otro': round(mi[1], 2), 'escala': round(mi[2], 4)}}
        for name, (de, do, ds) in (('sale', mo), ('entra', mi)):
            moving = abs(de) >= a.min_px or abs(do) >= a.min_px or abs(ds) >= a.min_scale
            if not moving:
                why.append(f'{name}: no se mueve alrededor del corte')
            elif axis == 'z':
                if abs(ds) < a.min_scale or sgn(ds) != d:
                    why.append(f"{name}: la escala va {'+' if ds > 0 else '-'}{abs(ds) * 100:.1f}% y la regla pide "
                               f"{'crecer' if d > 0 else 'achicarse'} (dir {d:+d})")
            else:
                if abs(de) < a.min_px or sgn(de) != d or abs(de) < abs(do):
                    why.append(f'{name}: se mueve {de:+.1f}px en {axis} ({do:+.1f}px en el otro eje); '
                               f'la costura pide {"+" if d > 0 else "-"}{axis}')
        for k in (-1, 0, 1):
            oo, oi = S[k]['out']['op'], S[k]['in']['op']
            if oo > a.legible and oi > a.legible:
                why.append(f'doble exposicion en t{k:+d}f: sale {oo:.2f} y entra {oi:.2f} (los dos > {a.legible})')
                break
    r['veredicto'] = 'FAIL' if why else 'PASS'
    r['motivos'] = why
    fails += bool(why)

# ------------------------------------------------ tabla
fmt = lambda v: f'{v:+7.1f}' if v is not None else '   -   '
print(f'costuras de {a.html}: {len(res)}')
if res:
    print(f"{'#':>2} {'t':>6}  eje dir  {'sale':<14}{'mov':>9}  {'entra':<14}{'mov':>9}   opac sale/entra en -1f | 0 | +1f      veredicto")
for r in res:
    S = r['samples']
    if r['mov'] is None:
        print(f"{r['i']:>2} {r['t']:6.3f}  {r.get('axis','x'):>3} {r.get('dir',-1):+3d}  {str(r['out'])[:13]:<14}{'':>9}  {str(r['in'])[:13]:<14}{'':>9}   {'':<38}  FAIL")
    else:
        unit = lambda m: (f"{m['escala'] * 100:+7.1f}%" if r.get('axis') == 'z' else f"{m['eje']:+7.1f}px")
        ops = ' | '.join(f"{S[k]['out']['op']:.2f}/{S[k]['in']['op']:.2f}" for k in (-1, 0, 1))
        print(f"{r['i']:>2} {r['t']:6.3f}  {r.get('axis','x'):>3} {r.get('dir',-1):+3d}  {str(r['out'])[:13]:<14}{unit(r['mov']['sale']):>9}  "
              f"{str(r['in'])[:13]:<14}{unit(r['mov']['entra']):>9}   {ops:<38}  {r['veredicto']}")
    for m in r['motivos']:
        print(f'      - {m}')

verdict = 'FAIL' if fails else ('PASS' if res else 'SIN COSTURAS')
out = pathlib.Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps({'html': a.html, 'fps': a.fps, 'veredicto': verdict, 'fallas': fails,
                           'costuras': [{**r, 'samples': {str(k): v for k, v in r['samples'].items()}} for r in res]},
                          indent=1, ensure_ascii=False))
if not res:
    print('AVISO: window.SEAMS esta vacio (usa K.cut o registra las costuras a mano)')
print((f'COSTURAS {verdict}' if res else 'COSTURAS: ninguna registrada') + (f' · {fails} de {len(res)} con FAIL' if fails else '') + f' · {out}')
sys.exit(1 if fails else 0)
