#!/usr/bin/env python3
"""Exporta window.CUES (efectos sincronizados) de un index.html a JSON."""
import sys, json, pathlib
from playwright.sync_api import sync_playwright
html = pathlib.Path(sys.argv[1]).resolve()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto(html.as_uri()); pg.wait_for_function('() => window.READY === true', timeout=30000)
    cues = pg.evaluate('window.CUES'); dur = pg.evaluate('window.DURATION'); b.close()
json.dump({'duration': dur, 'cues': sorted(cues, key=lambda c: c['t'])}, open(sys.argv[2], 'w'), indent=0)
print(len(cues), 'cues ->', sys.argv[2])
