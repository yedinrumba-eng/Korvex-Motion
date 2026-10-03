#!/usr/bin/env python3
"""
Entrega final (paso "deliver" de /brag adaptado al estudio):
  1. Saca el poster (el cuadro mas fuerte YA ASENTADO, no a mitad de transicion) -> <out>.jpg
  2. Lo "hornea" como cuadro 0 del MP4: todas las plataformas usan el cuadro 0 de miniatura.
     Se REEMPLAZA el cuadro 0 (no se agrega): misma duracion, mismo sync de audio.
  3. Re-encodea buscando el CRF mas bajo que quepa en --max-mb (carpeta 20 MB, chat 30 MB).

Uso:
  python tools/deliver.py --video master.mp4 --poster-t 28.8 --out KORVIN/korvin-01.mp4 --max-mb 19.5
"""
import argparse, subprocess, os, sys

ap = argparse.ArgumentParser()
ap.add_argument('--video', required=True, help='master renderizado (calidad alta)')
ap.add_argument('--poster-t', type=float, required=True, help='segundo del cuadro mas fuerte, ya asentado')
ap.add_argument('--out', required=True)
ap.add_argument('--max-mb', type=float, default=19.5)
ap.add_argument('--crf', type=int, default=19, help='CRF inicial (19 suele dar ~19 MB en 30 s a 1080x1920)')
a = ap.parse_args()

poster = os.path.splitext(a.out)[0] + '.jpg'
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{a.poster_t:.3f}', '-i', a.video, '-frames:v', '1', '-q:v', '2', poster], check=True)

import math
crf, tries = a.crf, 0
while True:
    tries += 1
    if crf > 28 or tries > 5:
        sys.exit('no cupo ni con CRF 28 — baja duracion o resolucion')
    tmp = a.out + '.tmp.mp4'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', a.video, '-i', poster,
                    '-filter_complex', "[0:v][1:v]overlay=0:0:enable='eq(n,0)'[v]",
                    '-map', '[v]', '-map', '0:a?', '-c:v', 'libx264', '-crf', str(crf), '-preset', 'slow',
                    '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-c:a', 'copy', '-movflags', '+faststart', tmp], check=True)
    mb = os.path.getsize(tmp) / 1048576
    print(f'crf {crf}: {mb:.1f} MB')
    if mb <= a.max_mb:
        os.replace(tmp, a.out)
        break
    # +6 de CRF ~ la mitad de peso: salta directo al CRF estimado (texturas como el grano pesan mucho)
    crf = max(crf + 1, crf + math.ceil(math.log(mb / a.max_mb) / 0.1155))

# verificacion: mismos cuadros y duracion que el master
q = lambda f: subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0', '-show_entries',
                              'stream=nb_read_frames:format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout.split()
print('master:', q(a.video), '| final:', q(a.out))
print('listo:', a.out, '+', poster)
