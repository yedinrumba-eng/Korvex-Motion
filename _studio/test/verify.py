"""Las 3 pruebas del estudio + test.png (primer, medio y ultimo cuadro).

Solo determinismo de otra pagina (1080x1920, 30 fps, 4 sub-cuadros con blur):
  python verify.py --html seams-demo.html --frames 30,54,102,150,174
  -> renderiza cada cuadro dos veces (dos lanzamientos de Chromium) y compara el MD5; codigo 1 si alguno cambia.
"""
import subprocess, hashlib, sys, argparse, pathlib, numpy as np, cv2, wave

ap = argparse.ArgumentParser()
ap.add_argument('--html', help='solo determinismo de esta pagina (si no, las 3 pruebas de siempre con index.html)')
ap.add_argument('--frames', default='0,45,90', help='cuadros a comparar (con --html)')
ap.add_argument('--fps', default='30')
ap.add_argument('--out', default='det', help='carpeta para los PNG (con --html)')
args = ap.parse_args()
md5 = lambda f: hashlib.md5(open(f, 'rb').read()).hexdigest()
if args.html:
    out = pathlib.Path(args.out); out.mkdir(parents=True, exist_ok=True)
    stem, bad = pathlib.Path(args.html).stem, 0
    for f in [int(x) for x in args.frames.split(',')]:
        h = []
        for n in ('a', 'b'):
            png = out / f'{stem}-f{f}-{n}.png'
            subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent.parent / 'render.py'), '--html', args.html,
                            '--w', '1080', '--h', '1920', '--fps', args.fps, '--sub', '4', '--frame', str(f), '--png', str(png)],
                           check=True, capture_output=True)
            h.append(md5(png))
        bad += h[0] != h[1]
        print(f'[det] {args.html} cuadro {f:>4}  md5 a={h[0]}  b={h[1]}  ->', 'IDENTICOS' if h[0] == h[1] else 'DISTINTOS')
    print('DETERMINISMO', 'PASS' if not bad else f'FAIL ({bad} cuadros distintos)')
    sys.exit(1 if bad else 0)

R = ['python3', '../render.py', '--html', 'index.html', '--w', '1920', '--h', '1080', '--fps', '60', '--sub', '4']

# 1) Determinismo: el cuadro 90 dos veces, en dos lanzamientos separados del navegador
for n in ('a', 'b'):
    subprocess.run(R + ['--frame', '90', '--png', f'f90_{n}.png'], check=True, capture_output=True)
A, B = cv2.imread('f90_a.png'), cv2.imread('f90_b.png')
md5 = lambda f: hashlib.md5(open(f, 'rb').read()).hexdigest()
diff = int(np.abs(A.astype(int) - B.astype(int)).max())
print(f'[1] determinismo  md5 a={md5("f90_a.png")}  b={md5("f90_b.png")}  max|dif|={diff}  ->',
      'IDENTICOS' if diff == 0 else 'DISTINTOS')

# 2) Motion blur: cuadro 64 (t=1.067 s, pleno estiramiento) con 4 sub-cuadros vs 1 sub-cuadro
subprocess.run(R + ['--frame', '64', '--png', 'blur_4sub.png'], check=True, capture_output=True)
subprocess.run(R[:-1] + ['1', '--frame', '64', '--png', 'blur_1sub.png'], check=True, capture_output=True)
b4, b1 = cv2.imread('blur_4sub.png'), cv2.imread('blur_1sub.png')
def edge_width(img):
    row = img[540, :, 1].astype(float)            # canal verde, fila central
    g = (row - row.min()) / (row.max() - row.min() + 1e-9)
    return int(((g > 0.1) & (g < 0.9)).sum())      # pixeles de transicion en los bordes
print(f'[2] motion blur   ancho de borde (px de transicion): 1 sub={edge_width(b1)}  4 sub={edge_width(b4)}')
crop = lambda im: im[380:700, 560:1360]
side = np.hstack([crop(b1), np.full((320, 12, 3), 255, np.uint8), crop(b4)])
cv2.putText(side, '1 sub-cuadro', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255, 255, 255), 2)
cv2.putText(side, '4 sub-cuadros (motion blur)', (832, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255, 255, 255), 2)
cv2.imwrite('blur_compare.png', side)

# 3) Audio: decodificar el MP4 final y ubicar el pico del beep
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', 'test.mp4', '-vn', '-ac', '1', '-ar', '48000',
                '-f', 'wav', 'decoded.wav'], check=True)
with wave.open('decoded.wav') as w:
    x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float); sr = w.getframerate()
env = np.abs(x)
peak = int(np.argmax(env)); onset = int(np.argmax(env > 0.1 * env.max()))
print(f'[3] audio         onset={onset/sr*1000:.2f} ms  pico={peak/sr*1000:.2f} ms  '
      f'(objetivo 1000 ms; 1 cuadro a 60 fps = 16.67 ms)')

# test.png: primer, medio y ultimo cuadro del MP4 final
frames = []
for i in (0, 90, 179):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', 'test.mp4', '-vf', f'select=eq(n\\,{i})',
                    '-vframes', '1', f'_f{i}.png'], check=True)
    im = cv2.imread(f'_f{i}.png'); im = cv2.resize(im, (960, 540), interpolation=cv2.INTER_AREA)
    cv2.putText(im, f'frame {i}', (24, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)
    frames.append(im)
sep = np.full((540, 10, 3), 255, np.uint8)
cv2.imwrite('test.png', np.hstack([frames[0], sep, frames[1], sep, frames[2]]))
print('test.png ok')
