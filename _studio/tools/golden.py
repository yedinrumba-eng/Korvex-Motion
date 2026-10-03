#!/usr/bin/env python3
"""
Cuadros dorados: regresion entre vueltas del Juez ("lo que no se toco, no cambio").

Uso (desde <CLIENTE>/videos/NN-nombre/):
  python ../../../_studio/tools/golden.py --html index.html --out qa/golden --save            # tras el primer PASS
  python ../../../_studio/tools/golden.py --html index.html --out qa/golden --compare         # en cada vuelta
  python ../../../_studio/tools/golden.py --html index.html --out qa/golden --compare --allow 9.5,cierre

--save renderiza un PNG por cada label del timeline (window.TL.labels, que pone K.install, o window.LABELS)
       o por cada instante de --times 0,1.5,... y escribe golden.json (tiempos, labels, md5, escala).
--compare vuelve a renderizar los MISMOS instantes guardados y los compara con absdiff (opencv/numpy):
       % de pixeles distintos por cuadro (un pixel cuenta si algun canal cambia mas de --tol niveles).
       Un cuadro con mas de --pct % (1 % por defecto) cambio: escribe diff-<t>.png (guardado | nuevo | mapa)
       y sale con codigo 1, salvo que ese t (o su label) este en --allow (lo que si se toco a proposito).
Render sin motion blur, con las mismas banderas de Chromium que render.py; --scale 0.5 para ir rapido.
"""
import argparse, base64, hashlib, json, pathlib, sys
import numpy as np, cv2
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument('--html', required=True)
ap.add_argument('--out', default='qa/golden')
g = ap.add_mutually_exclusive_group(required=True)
g.add_argument('--save', action='store_true', help='guarda los cuadros dorados')
g.add_argument('--compare', action='store_true', help='compara contra los guardados')
ap.add_argument('--times', help='instantes en s separados por coma (si no, los labels del timeline)')
ap.add_argument('--scale', type=float, default=1.0, help='1 = 1080x1920; 0.5 = rapido')
ap.add_argument('--w', type=int, default=1080)
ap.add_argument('--h', type=int, default=1920)
ap.add_argument('--pct', type=float, default=1.0, help='%% de pixeles distintos a partir del cual un cuadro cambio')
ap.add_argument('--tol', type=int, default=8, help='niveles (0-255) que puede cambiar un pixel sin contar como distinto')
ap.add_argument('--allow', default='', help='t o labels que SI pueden cambiar (separados por coma)')
a = ap.parse_args()

out = pathlib.Path(a.out)
man_path = out / 'golden.json'
name = lambda t: f'{t:.3f}'


def render(times, scale):
    """Renderiza cada t (sin blur) y devuelve [(t, imagen BGR)], mas los labels de la pagina."""
    html = pathlib.Path(a.html).resolve()
    imgs = []
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--force-device-scale-factor=1', '--font-render-hinting=none',
                                    '--disable-lcd-text', '--hide-scrollbars'])
        pg = b.new_page(viewport={'width': a.w, 'height': a.h}, device_scale_factor=1)
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto(html.as_uri())
        cdp = pg.context.new_cdp_session(pg)
        try:
            pg.wait_for_function('() => typeof window.seek === "function" && (window.READY === undefined || window.READY === true)',
                                 timeout=60000)
        except Exception:
            print('la pagina no quedo READY', errs[:10]); b.close(); sys.exit(2)
        pg.evaluate('document.fonts.ready.then(() => 0)')
        pg.evaluate('Promise.all([...document.fonts].map(f => f.load().catch(() => 0))).then(() => 0)')   # todas las fuentes, como render.py
        pg.wait_for_timeout(300)
        labels = pg.evaluate('() => { const L = window.LABELS || (window.TL && window.TL.labels) || {}; '
                             'return Object.fromEntries(Object.entries(L).map(([k, v]) => [k, +v])); }')
        if times is None:
            times = sorted(set(round(v, 4) for v in labels.values()))
        for t in times:
            pg.evaluate('t => { window.seek(t); }', t)
            png = base64.b64decode(cdp.send('Page.captureScreenshot', {'format': 'png', 'optimizeForSpeed': True,
                                   'clip': {'x': 0, 'y': 0, 'width': a.w, 'height': a.h, 'scale': scale}})['data'])
            imgs.append((t, cv2.imdecode(np.frombuffer(png, np.uint8), cv2.IMREAD_COLOR)))
        b.close()
    return imgs, labels


def label_of(t, labels):
    ks = [k for k, v in labels.items() if abs(v - t) < 1e-3]
    return ','.join(ks)


if a.save:
    times = [float(x) for x in a.times.split(',')] if a.times else None
    imgs, labels = render(times, a.scale)
    if not imgs:
        print('el timeline no tiene labels: agrega tl.addLabel(...) por beat o usa --times 0,1.5,...'); sys.exit(2)
    out.mkdir(parents=True, exist_ok=True)
    for f in list(out.glob('golden-*.png')) + list(out.glob('diff-*.png')):
        f.unlink()
    frames = []
    for t, im in imgs:
        f = out / f'golden-{name(t)}.png'
        cv2.imwrite(str(f), im)
        frames.append({'t': t, 'label': label_of(t, labels), 'file': f.name, 'md5': hashlib.md5(f.read_bytes()).hexdigest()})
    man_path.write_text(json.dumps({'html': a.html, 'scale': a.scale, 'w': a.w, 'h': a.h, 'frames': frames}, indent=1, ensure_ascii=False))
    for fr in frames:
        print(f"  {fr['t']:7.3f}s  {fr['label'] or '-':<14} {fr['file']}  {fr['md5']}")
    print(f'GOLDEN guardados: {len(frames)} cuadros en {out}  (escala {a.scale})')
    sys.exit(0)

# ------------------------------------------------ --compare
if not man_path.exists():
    print(f'no hay cuadros dorados en {out}: corre primero con --save'); sys.exit(2)
M = json.loads(man_path.read_text())
if a.scale != 1.0 and a.scale != M['scale']:
    print(f"AVISO: los dorados se guardaron a escala {M['scale']}; comparo a esa escala")
times = [fr['t'] for fr in M['frames']]
imgs, labels = render(times, M['scale'])
allow = [x.strip() for x in a.allow.split(',') if x.strip()]


def allowed(fr):
    for x in allow:
        try:
            if abs(float(x) - fr['t']) < 1e-3:
                return True
        except ValueError:
            if x in fr['label'].split(','):
                return True
    return False


for f in out.glob('diff-*.png'):
    f.unlink()
rows, bad = [], 0
for fr, (t, new) in zip(M['frames'], imgs):
    old = cv2.imread(str(out / fr['file']))
    if old is None or old.shape != new.shape:
        pct, mx = 100.0, 255
    else:
        d = cv2.absdiff(old, new).max(axis=2)
        pct, mx = float((d > a.tol).mean() * 100), int(d.max())
    changed = pct > a.pct
    ok_allowed = changed and allowed(fr)
    if changed:
        # guardado | nuevo | mapa de diferencias (rojo) sobre el guardado en gris
        h, w = new.shape[:2]
        o = old if old is not None and old.shape == new.shape else np.zeros_like(new)
        m = cv2.absdiff(o, new).max(axis=2) > a.tol
        heat = cv2.cvtColor(cv2.cvtColor(o, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR) // 3
        heat[m] = (40, 40, 255)
        sep = np.full((h, 8, 3), 255, np.uint8)
        side = np.hstack([o, sep, new, sep, heat])
        k = 1600 / side.shape[1]
        side = cv2.resize(side, (1600, int(side.shape[0] * k)), interpolation=cv2.INTER_AREA) if k < 1 else side
        for x, txt in ((10, 'guardado'), (side.shape[1] // 3 + 10, 'nuevo'), (2 * side.shape[1] // 3 + 10, f'distinto {pct:.2f}%')):
            cv2.putText(side, txt, (x, 34), cv2.FONT_HERSHEY_SIMPLEX, .9, (0, 255, 255), 2)
        cv2.imwrite(str(out / f'diff-{name(t)}.png'), side)
    state = 'igual' if not changed else ('cambio (permitido)' if ok_allowed else 'CAMBIO')
    bad += changed and not ok_allowed
    rows.append({'t': t, 'label': fr['label'], 'pct': round(pct, 3), 'max': mx, 'estado': state})

print(f"{'t':>8}  {'label':<14} {'distinto':>9} {'max':>4}  estado")
for r in rows:
    print(f"{r['t']:7.3f}s  {r['label'] or '-':<14} {r['pct']:8.3f}% {r['max']:>4}  {r['estado']}")
new_labels = sorted(k for k, v in labels.items() if all(abs(v - t) > 1e-3 for t in times))
if new_labels:
    print(f'  labels nuevos o que se movieron desde el --save (no se comparan): {", ".join(new_labels)}')
(out / 'compare.json').write_text(json.dumps({'html': a.html, 'umbral_pct': a.pct, 'tol': a.tol, 'allow': allow,
                                              'veredicto': 'FAIL' if bad else 'PASS', 'cuadros': rows}, indent=1, ensure_ascii=False))
print(f"GOLDEN {'FAIL' if bad else 'PASS'} · {len(rows)} cuadros · {bad} cambiaron sin permiso · {out / 'compare.json'}")
sys.exit(1 if bad else 0)
