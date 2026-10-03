#!/usr/bin/env python3
"""Hoja de contacto: renderiza instantes sueltos (sin blur) y los pone en una grilla."""
import sys, pathlib, numpy as np, cv2
from playwright.sync_api import sync_playwright
html = pathlib.Path(sys.argv[1]).resolve(); out = sys.argv[2]
times = [float(x) for x in sys.argv[3].split(',')]
cols = int(sys.argv[4]) if len(sys.argv) > 4 else 5
W, H = 1080, 1920; tw = 360; th = 640
tiles = []
with sync_playwright() as p:
    b = p.chromium.launch(args=['--force-device-scale-factor=1', '--font-render-hinting=none'])
    pg = b.new_page(viewport={'width': W, 'height': H})
    msgs = []
    pg.on('console', lambda m: msgs.append(m.text)); pg.on('pageerror', lambda e: msgs.append('ERR ' + str(e)))
    pg.goto(html.as_uri())
    try:
        pg.wait_for_function('() => window.READY === true', timeout=30000)
    except Exception as e:
        print('NOT READY', msgs); raise
    pg.wait_for_timeout(200)
    for t in times:
        pg.evaluate('t => window.seek(t)', t)
        im = cv2.imdecode(np.frombuffer(pg.screenshot(type='png'), np.uint8), 1)
        im = cv2.resize(im, (tw, th), interpolation=cv2.INTER_AREA)
        cv2.putText(im, f'{t:.2f}s', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, .8, (0, 255, 255), 2)
        tiles.append(im)
    if msgs: print('\n'.join(msgs[:20]))
    b.close()
while len(tiles) % cols: tiles.append(np.zeros_like(tiles[0]))
rows = [np.hstack(tiles[i:i + cols]) for i in range(0, len(tiles), cols)]
cv2.imwrite(out, np.vstack(rows)); print('ok', out)
