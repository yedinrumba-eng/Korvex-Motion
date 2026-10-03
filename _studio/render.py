#!/usr/bin/env python3
"""
Motion Design Studio — renderer determinista.

Carga un index.html que expone window.seek(t) (t en segundos), captura cada
cuadro con Chromium headless, promedia N sub-cuadros para motion blur y
entrega los cuadros crudos a ffmpeg. Opcionalmente mezcla un WAV.

Uso:
  python3 render.py --html test/index.html --out test/out.mp4 --w 1920 --h 1080 \
      --fps 60 --dur 3 --sub 4 --audio test/beep.wav
  python3 render.py --html test/index.html --frame 90 --png f90.png ...   (un solo cuadro)
  --draft        borrador: 540x960, sin blur, crf 24, preset veryfast (para la puerta de revision)
  --linear       promedia el blur en luz lineal (mas fisico; un poco mas lento)
  --no-adaptive  por defecto, si el primer y el ultimo sub-cuadro son iguales (cuadro quieto) se usa 1 captura
"""
import argparse, subprocess, sys, time, pathlib, base64
import numpy as np, cv2
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument('--html', required=True)
ap.add_argument('--out')
ap.add_argument('--w', type=int, default=1080)
ap.add_argument('--h', type=int, default=1920)
ap.add_argument('--fps', type=int, default=30)
ap.add_argument('--dur', type=float)
ap.add_argument('--sub', type=int, default=4, help='sub-cuadros por cuadro (motion blur)')
ap.add_argument('--shutter', type=float, default=0.5, help='fraccion del intervalo con obturador abierto (0.5 = 180 grados)')
ap.add_argument('--audio')
ap.add_argument('--frame', type=int, help='renderiza solo este cuadro')
ap.add_argument('--png', help='salida PNG del cuadro unico')
ap.add_argument('--start', type=int, default=0)
ap.add_argument('--end', type=int)
ap.add_argument('--crf', type=int, default=16)
ap.add_argument('--workers', type=int, default=1, help='procesos en paralelo (cada uno con su Chromium)')
ap.add_argument('--part', help=argparse.SUPPRESS)
ap.add_argument('--draft', action='store_true', help='borrador rapido: mitad de resolucion, sin blur, crf 24 (para revisar antes del final)')
ap.add_argument('--linear', action='store_true', help='promedia los sub-cuadros en luz lineal (blur mas fisico)')
ap.add_argument('--no-adaptive', action='store_true', help='captura todos los sub-cuadros aunque el cuadro este quieto')
a = ap.parse_args()
SCALE = 0.5 if a.draft else 1.0
if a.draft:
    a.sub = 1
    a.crf = max(a.crf, 24)
OW, OH = int(a.w * SCALE), int(a.h * SCALE)

html = pathlib.Path(a.html).resolve()


def sub_times(f):
    """Instantes de los sub-cuadros del cuadro f, centrados en f/fps."""
    base = f / a.fps
    if a.sub <= 1:
        return [base]
    span = a.shutter / a.fps
    return [max(0.0, base + ((k + 0.5) / a.sub - 0.5) * span) for k in range(a.sub)]


CDP = None


def shot(page):
    # PNG sin perdida via CDP (optimizeForSpeed = compresion rapida, mismos pixeles)
    return base64.b64decode(CDP.send('Page.captureScreenshot', {'format': 'png', 'optimizeForSpeed': True,
            'clip': {'x': 0, 'y': 0, 'width': a.w, 'height': a.h, 'scale': SCALE}})['data'])


ACC = None
_LIN = (np.where(np.arange(256) / 255 <= 0.04045, np.arange(256) / 255 / 12.92,
                 ((np.arange(256) / 255 + 0.055) / 1.055) ** 2.4) * 255).astype(np.float32)


def _to_srgb(x):
    x = np.clip(x / 255.0, 0, 1)
    return np.where(x <= 0.0031308, x * 12.92, 1.055 * np.power(x, 1 / 2.4) - 0.055) * 255.0


def grab(page, f):
    # buffer reutilizado: evita que la memoria crezca cuadro a cuadro
    global ACC
    if ACC is None:
        ACC = np.zeros((OH, OW, 3), np.float32)
    ACC.fill(0)
    ts = sub_times(f)

    def cap(t):
        page.evaluate('t => window.seek(t)', t)
        return cv2.imdecode(np.frombuffer(shot(page), np.uint8), cv2.IMREAD_COLOR)

    imgs = [cap(ts[0])]
    if len(ts) > 1:
        last = cap(ts[-1])
        if not a.no_adaptive and np.array_equal(imgs[0], last):
            imgs = [imgs[0]]                      # cuadro quieto: no hace falta blur
        else:
            imgs += [cap(t) for t in ts[1:-1]] + [last]
    for img in imgs:
        if a.linear:
            np.add(ACC, _LIN[img], out=ACC)
        else:
            np.add(ACC, img, out=ACC, casting='unsafe')
    ACC *= 1.0 / len(imgs)
    if a.linear:
        return (_to_srgb(ACC) + 0.5).astype(np.uint8)
    ACC += 0.5
    return ACC.astype(np.uint8)


if a.workers > 1 and a.frame is None:
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        pg.goto(html.as_uri()); pg.wait_for_function('() => typeof window.seek === "function" && (window.READY === undefined || window.READY === true)', timeout=60000)
        dur = a.dur if a.dur else pg.evaluate('window.DURATION'); b.close()
    n = int(round(dur * a.fps)); step = -(-n // a.workers); procs = []; parts = []
    t0 = time.time()
    for w in range(a.workers):
        st, en = w * step, min(n, (w + 1) * step)
        part = f'{a.out}.part{w}.mp4'; parts.append(part)
        cmd = [sys.executable, __file__, '--html', a.html, '--out', part, '--w', str(a.w), '--h', str(a.h), '--fps', str(a.fps),
               '--dur', str(dur), '--sub', str(a.sub), '--shutter', str(a.shutter), '--start', str(st), '--end', str(en), '--crf', str(a.crf)]
        cmd += (['--draft'] if a.draft else []) + (['--linear'] if a.linear else []) + (['--no-adaptive'] if a.no_adaptive else [])
        import os
        procs.append(subprocess.Popen(cmd, env={**os.environ, 'MALLOC_ARENA_MAX': '2'}))
    for pr in procs: pr.wait()
    lst = a.out + '.txt'; open(lst, 'w').write(''.join(f"file '{pathlib.Path(x).resolve()}'\n" for x in parts))
    cat = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst]
    if a.audio: cat += ['-i', a.audio, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-t', f'{dur:.3f}']
    else: cat += ['-c', 'copy']
    subprocess.run(cat + ['-movflags', '+faststart', a.out], check=True)
    for x in parts + [lst]: pathlib.Path(x).unlink()
    print(f'listo: {a.out}  ({n} cuadros, {a.workers} procesos, {time.time()-t0:.0f}s)')
    sys.exit(0)

with sync_playwright() as p:
    browser = p.chromium.launch(args=['--force-device-scale-factor=1', '--font-render-hinting=none',
                                      '--disable-lcd-text', '--hide-scrollbars'])
    page = browser.new_page(viewport={'width': a.w, 'height': a.h}, device_scale_factor=1)
    page.goto(html.as_uri())
    CDP = page.context.new_cdp_session(page)
    page.wait_for_function('() => typeof window.seek === "function" && (window.READY === undefined || window.READY === true)', timeout=60000)
    page.evaluate('document.fonts.ready')
    # carga YA todas las fuentes declaradas: una fuente que se usa recien a mitad del video (texto que aparece tarde)
    # se pedia al pintarla y salia invisible o a medias en algunos renders (kit-motion: K.scramble en JetBrains Mono)
    page.evaluate('Promise.all([...document.fonts].map(f => f.load().catch(() => 0))).then(() => 0)')
    page.wait_for_timeout(300)

    if a.frame is not None:
        img = grab(page, a.frame)
        cv2.imwrite(a.png, img)
        print(f'frame {a.frame} -> {a.png}')
        browser.close()
        sys.exit(0)

    dur = a.dur if a.dur else page.evaluate('window.DURATION')
    n = int(round(dur * a.fps))
    end = a.end if a.end else n
    silent_out = a.out if not a.audio else a.out + '.video.mp4'
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24',
           '-s', f'{OW}x{OH}', '-r', str(a.fps), '-i', '-',
           '-c:v', 'libx264', '-preset', 'veryfast' if a.draft else 'medium', '-crf', str(a.crf), '-pix_fmt', 'yuv420p',
           '-movflags', '+faststart', silent_out]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    t0 = time.time()
    for f in range(a.start, end):
        ff.stdin.write(grab(page, f).tobytes())
        if f % 30 == 0:
            el = time.time() - t0
            try:   # /proc only exists on Linux; on Windows the progress line goes without RSS
                mem = f"{int(open('/proc/self/status').read().split('VmRSS:')[1].split()[0]) // 1024}MB"
            except OSError:
                mem = 'n/a'
            print(f'  cuadro {f}/{end}  {el:.0f}s  rss={mem}', flush=True)
    ff.stdin.close(); ff.wait()
    browser.close()

    if a.audio:
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', silent_out, '-i', a.audio,
                        '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000',
                        '-t', f'{dur:.3f}', '-movflags', '+faststart', a.out], check=True)
        pathlib.Path(silent_out).unlink()
    print(f'listo: {a.out}  ({n} cuadros, {time.time()-t0:.0f}s)')
