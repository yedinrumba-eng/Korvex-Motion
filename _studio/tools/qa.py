#!/usr/bin/env python3
"""
QA automatico ("oraculo") de un video del estudio — la PUERTA 3 del flujo spec-driven.

Uso:
  python ../../../_studio/tools/qa.py --video borrador.mp4 --html index.html --out qa
  python ../../../_studio/tools/qa.py --video master.mp4 --max-mb 19.5          (solo el archivo)

Revisa:
  - archivo: duracion, cuadros, fps, resolucion, peso (<= --max-mb)
  - imagen: % de cuadros quietos, cortes y variacion de duracion de tomas (CV), saltos de UN cuadro ("pops"),
            cuadros negros/vacios al inicio
  - audio:  loudness integrado (LUFS) y true peak (dBTP) con ffmpeg ebur128
  - texto (con --html): texto visible fuera de la zona segura de IG (y<150, y>1550, o x>950 entre y 900–1700)
  - hojas: qa/contacto.png (1 cuadro por segundo) y qa/transiciones.png (los cuadros de mas movimiento)
Escribe qa/report.json y termina con codigo 1 si hay FAIL.
Ideas de onetake (verify_promo) y HyperFrames, reimplementadas.
"""
import argparse, json, subprocess, pathlib, sys
import numpy as np, cv2

ap = argparse.ArgumentParser()
ap.add_argument('--video', required=True)
ap.add_argument('--html')
ap.add_argument('--out', default='qa')
ap.add_argument('--max-mb', type=float, default=19.5)
ap.add_argument('--lufs', type=float, default=-14.0, help='objetivo de loudness (IG/TikTok normalizan cerca de -14)')
ap.add_argument('--safe', default='150,1550,950,900,1700', help='y_top,y_bottom,x_right,y_right0,y_right1 (en 1080x1920)')
a = ap.parse_args()
out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
R = {'video': a.video, 'fail': [], 'warn': [], 'info': {}}


def probe(f):
    j = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-print_format', 'json', '-show_streams', '-show_format', f],
                                  capture_output=True, text=True).stdout)
    v = [s for s in j['streams'] if s['codec_type'] == 'video'][0]
    num, den = map(int, v['r_frame_rate'].split('/'))
    return {'w': v['width'], 'h': v['height'], 'fps': num / den, 'dur': float(j['format']['duration']),
            'mb': int(j['format']['size']) / 1048576, 'audio': any(s['codec_type'] == 'audio' for s in j['streams'])}


P = probe(a.video); R['info']['archivo'] = P
if P['mb'] > a.max_mb:
    R['fail'].append(f"pesa {P['mb']:.1f} MB (> {a.max_mb} MB): pasalo por deliver.py")
if (P['w'], P['h']) != (1080, 1920):
    R['warn'].append(f"resolucion {P['w']}x{P['h']} (los reels van a 1080x1920)")

# ------------------------------------------------ imagen: cuadros chicos en gris
SW, SH = 135, 240
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', a.video, '-vf', f'scale={SW}:{SH},format=gray', '-f', 'rawvideo', '-'],
                     capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, SH, SW).astype(np.float32)
n = len(fr); fps = P['fps']
d = np.abs(np.diff(fr, axis=0)).mean((1, 2))                      # d[i] = cambio del cuadro i al i+1
still = float((d < 0.6).mean() * 100)
med = float(np.median(d) + 1e-6)
cuts = [i + 1 for i in range(len(d)) if d[i] > max(22.0, 6 * med)]
bounds = [0] + cuts + [n]
shots = [(bounds[i + 1] - bounds[i]) / fps for i in range(len(bounds) - 1) if bounds[i + 1] > bounds[i]]
cv = float(np.std(shots) / np.mean(shots)) if len(shots) > 1 else 0.0
pops = []
for i in range(1, len(d)):
    # el cuadro i es distinto a sus dos vecinos, pero los vecinos se parecen entre si
    if d[i - 1] > max(8, 3 * med) and d[i] > max(8, 3 * med):
        if np.abs(fr[i - 1] - fr[i + 1]).mean() < 0.35 * min(d[i - 1], d[i]):
            pops.append(round(i / fps, 3))
R['info']['imagen'] = {'cuadros': n, 'quietos_pct': round(still, 1), 'cortes_s': [round(c / fps, 2) for c in cuts],
                       'tomas_s': [round(s, 2) for s in shots], 'cv_tomas': round(cv, 2), 'pops_s': pops}
if pops:
    R['warn'].append(f"{len(pops)} salto(s) de un cuadro en {pops[:8]}s: revisa esos cuadros (sets a destiempo, fromTo con immediateRender)")
if len(shots) >= 3 and cv < 0.25:
    R['warn'].append(f"las tomas duran casi lo mismo (CV {cv:.2f} < 0.25): varia el ritmo, mete una pausa")
if still < 6:
    R['warn'].append(f"solo {still:.0f}% de cuadros quietos: el ojo necesita pausas (holds) para leer")
first_dark = fr[0].mean() < 6 and fr[min(2, n - 1)].mean() < 6
if first_dark:
    R['warn'].append('los primeros cuadros estan en negro: el cuadro 0 es la portada en IG (usa deliver.py --poster-t)')

# hojas de contacto
def sheet(idx, path, cols=8, label=True):
    if not idx:
        return
    tw, th = 216, 384
    tiles = []
    for i in idx:
        t = i / fps
        im = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.3f}', '-i', a.video, '-frames:v', '1', '-vf', f'scale={tw}:{th}',
                             '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True).stdout
        if len(im) != tw * th * 3:
            continue
        im = np.frombuffer(im, np.uint8).reshape(th, tw, 3).copy()
        if label:
            cv2.putText(im, f'{t:.2f}s', (6, 22), cv2.FONT_HERSHEY_SIMPLEX, .6, (0, 255, 255), 2)
        tiles.append(im)
    while len(tiles) % cols:
        tiles.append(np.zeros_like(tiles[0]))
    rows = [np.hstack(tiles[i:i + cols]) for i in range(0, len(tiles), cols)]
    cv2.imwrite(str(path), np.vstack(rows))

sheet([int(round(s * fps)) for s in np.arange(0.5, P['dur'], 1.0)], out / 'contacto.png')
peaks = sorted(np.argsort(d)[-16:].tolist())
sheet([p + 1 for p in peaks], out / 'transiciones.png')

# ------------------------------------------------ audio
if P['audio']:
    log = subprocess.run(['ffmpeg', '-nostats', '-i', a.video, '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    summ = log[log.rfind('Summary:'):]
    def grab(key):
        for ln in summ.splitlines():
            if ln.strip().startswith(key):
                try:
                    return float(ln.split(':')[1].split()[0])
                except Exception:
                    return None
    I, TP = grab('I:'), grab('Peak:')
    R['info']['audio'] = {'lufs': I, 'true_peak_db': TP}
    if TP is not None and TP > -0.5:
        R['fail'].append(f'true peak {TP} dBTP: se va a distorsionar al recodificar (usa synth.master_lufs)')
    elif TP is not None and TP > -1.0:
        R['warn'].append(f'true peak {TP} dBTP (> -1): bajalo con synth.master_lufs')
    if I is not None and abs(I - a.lufs) > 3:
        R['warn'].append(f'loudness {I} LUFS (objetivo {a.lufs}): IG lo va a {"bajar" if I > a.lufs else "subir"}; usa synth.master_lufs')
else:
    R['warn'].append('el video no tiene audio')

# ------------------------------------------------ texto en zona segura (necesita el index.html)
if a.html:
    from playwright.sync_api import sync_playwright
    yt, yb, xr, yr0, yr1 = [float(x) for x in a.safe.split(',')]
    JS = """([yt,yb,xr,yr0,yr1]) => {
      const out = []; const st = document.getElementById('stage') || document.body; const sb = st.getBoundingClientRect();
      const op = el => { let o = 1; for (let e = el; e && e.nodeType === 1; e = e.parentElement) { const cs = getComputedStyle(e);
          if (cs.display === 'none' || cs.visibility === 'hidden') return 0; o *= parseFloat(cs.opacity); } return o; };
      const clip = el => { let r = el.getBoundingClientRect(); r = {l: r.left, t: r.top, r: r.right, b: r.bottom};
        for (let e = el.parentElement; e && e !== document.body; e = e.parentElement) { const cs = getComputedStyle(e);
          if (cs.overflow !== 'visible' || cs.clipPath !== 'none') { const q = e.getBoundingClientRect();
            r = {l: Math.max(r.l, q.left), t: Math.max(r.t, q.top), r: Math.min(r.r, q.right), b: Math.min(r.b, q.bottom)}; } }
        return r; };
      const walker = document.createTreeWalker(st, NodeFilter.SHOW_TEXT);
      const seen = new Set();
      while (walker.nextNode()) { const tn = walker.currentNode, el = tn.parentElement; if (!el || seen.has(el)) continue;
        if (!tn.textContent.trim()) continue; seen.add(el);
        if (el.closest('svg') && !el.closest('text')) continue;
        if (op(el) < 0.15) continue;
        // caja del TEXTO (no del elemento, que puede ser de ancho completo) recortada por los ancestros con overflow/clip
        const rg = document.createRange(); rg.selectNodeContents(tn); const tr = rg.getBoundingClientRect(); const cr = clip(el);
        const r = {l: Math.max(tr.left, cr.l), t: Math.max(tr.top, cr.t), r: Math.min(tr.right, cr.r), b: Math.min(tr.bottom, cr.b)};
        if (r.r - r.l < 4 || r.b - r.t < 4) continue;
        // tapado por otra capa opaca encima (p. ej. un intro): no cuenta
        const cx = Math.min(1079, Math.max(0, (r.l + r.r) / 2)), cy = Math.min(1919, Math.max(0, (r.t + r.b) / 2));
        const top = document.elementsFromPoint(cx, cy).find(e => op(e) >= 0.15 && getComputedStyle(e).pointerEvents !== 'none');
        if (top && !(top === el || el.contains(top) || top.contains(el))) continue;
        const x0 = r.l - sb.left, y0 = r.t - sb.top, x1 = r.r - sb.left, y1 = r.b - sb.top;
        if (x1 < 0 || x0 > 1080 || y1 < 0 || y0 > 1920) continue;
        const bad = y0 < yt - 8 || y1 > yb + 8 || (x1 > xr + 8 && y1 > yr0 && y0 < yr1);
        if (bad) out.push({txt: tn.textContent.trim().slice(0, 40), x0: Math.round(x0), y0: Math.round(y0), x1: Math.round(x1), y1: Math.round(y1)}); }
      return out; }"""
    found = {}
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(pathlib.Path(a.html).resolve().as_uri()); pg.wait_for_function('() => window.READY === true', timeout=60000)
        dur = pg.evaluate('window.DURATION')
        if abs(dur - P['dur']) > 0.1:
            R['fail'].append(f'el video dura {P["dur"]:.2f}s pero window.DURATION = {dur}')
        for t in np.arange(0.0, dur, 0.25):
            pg.evaluate('t => window.seek(t)', float(t))
            for o in pg.evaluate(JS, [yt, yb, xr, yr0, yr1]):
                k = o['txt']
                if k not in found:
                    found[k] = {'desde_s': round(float(t), 2), **o}
        b.close()
    R['info']['texto_fuera_de_zona'] = list(found.values())
    for o in list(found.values())[:12]:
        R['warn'].append(f"texto fuera de zona segura desde {o['desde_s']}s: \"{o['txt']}\" ({o['x0']},{o['y0']})–({o['x1']},{o['y1']})")

R['veredicto'] = 'FAIL' if R['fail'] else ('PASS con avisos' if R['warn'] else 'PASS')
(out / 'report.json').write_text(json.dumps(R, indent=1, ensure_ascii=False))
print(f"QA {R['veredicto']} · {P['dur']:.2f}s {P['w']}x{P['h']} {P['mb']:.1f} MB · quietos {still:.0f}% · cortes {len(cuts)} · CV {cv:.2f}"
      + (f" · {R['info']['audio']['lufs']} LUFS / {R['info']['audio']['true_peak_db']} dBTP" if P['audio'] else ''))
for f in R['fail']:
    print('  FAIL', f)
for w in R['warn']:
    print('  WARN', w)
print(f"  hojas: {out / 'contacto.png'} · {out / 'transiciones.png'} · {out / 'report.json'}")
sys.exit(1 if R['fail'] else 0)
