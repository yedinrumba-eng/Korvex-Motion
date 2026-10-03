"""Pruebas del kit v3 (K.cut, K.nudgeEase, K.fitText, K.posterize) sobre seams-demo.html.
Uso (desde _studio/test/):  python kit_v3_test.py      -> codigo 1 si algo falla."""
import pathlib, random, sys
from playwright.sync_api import sync_playwright

ok = True
def check(name, cond, info=''):
    global ok
    ok &= bool(cond)
    print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f'  ({info})' if info else ''))

STATE = """() => ['#s1', '#s2', '#s3', '#s4', '#p0', '#p1', '#p2', '#stop'].map(s => { const e = document.querySelector(s), c = getComputedStyle(e);
  return [s, c.opacity, c.visibility, c.transform, c.filter].join(' '); }).join('\\n')"""

with sync_playwright() as p:
    b = p.chromium.launch(args=['--force-device-scale-factor=1', '--font-render-hinting=none'])
    def page():
        pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(pathlib.Path('seams-demo.html').resolve().as_uri())
        pg.wait_for_function('() => window.READY === true', timeout=60000)
        return pg
    pg = page()
    seek = lambda t: pg.evaluate('t => { window.seek(t); }', t)

    print('K.nudgeEase')
    r = pg.evaluate("""() => { const N = 20000, v = []; for (let i = 0; i <= N; i++) v.push(K.nudgeEase(i / N));
      let mono = true, jump = 0; for (let i = 1; i <= N; i++) { if (v[i] < v[i - 1]) mono = false; jump = Math.max(jump, v[i] - v[i - 1]); }
      const g = gsap.parseEase('nudge');
      return { mono, jump, k: [0, .2, .38, 1].map(K.nudgeEase), same: [.1, .3, .5, .9].every(x => Math.abs(g(x) - K.nudgeEase(x)) < 1e-12) }; }""")
    check('monotona en [0,1]', r['mono'])
    check('continua (salto maximo entre muestras de 1/20000)', r['jump'] < 2e-4, f"{r['jump']:.2e}")
    check('tramos: f(0)=0, f(.2)=.10, f(.38)=.75, f(1)=1', all(abs(x - y) < 1e-9 for x, y in zip(r['k'], [0, .1, .75, 1])), r['k'])
    check("registrada en GSAP como ease: 'nudge'", r['same'])
    xs = []
    for t in (0.4, 0.4 + 0.6 * 0.2, 0.4 + 0.6 * 0.38, 1.0):
        seek(t); xs.append(pg.evaluate("() => +gsap.getProperty('#p1', 'x')"))
    check('como ease de un tween: x = 0 / 25 / 187.5 / 250', all(abs(x - y) < 0.05 for x, y in zip(xs, [0, 25, 187.5, 250])), [round(x, 2) for x in xs])

    print('K.fitText')
    r = pg.evaluate("""() => { const el = document.querySelector('#hook'), f1 = window.FIT;
      const w1 = K.fitText.measure(el);
      const sp = el.querySelector('.l span'); const old = sp.style.transform; sp.style.transform = 'scale(.5) translateY(140%)';
      const w2 = K.fitText.measure(el); sp.style.transform = old;
      const f2 = K.fitText(el, 940);                    // otra vez: no debe achicar de nuevo
      const big = K.fitText(el, 2000);                  // cabe de sobra: no crece por encima del original
      const tiny = K.fitText(el, 100, { min: 40 });     // no cabe ni con el minimo: avisa y se queda en min
      const back = K.fitText(el, 940);
      return { f1, w1, w2, f2, big, tiny, back, fs: getComputedStyle(el.querySelector('.accent')).fontSize }; }""")
    check('el gancho de 150 px queda <= 940 px', r['f1']['fits'] and r['f1']['width'] <= 940 and r['f1']['size'] < 150, r['f1'])
    check('mide igual con spans transformados (scale/translate)', abs(r['w1'] - r['w2']) < 0.01, f"{r['w1']:.2f} vs {r['w2']:.2f}")
    check('repetirlo da el mismo tamano', r['f2']['size'] == r['f1']['size'], r['f2'])
    check('no agranda por encima del original', r['big']['size'] == 150, r['big'])
    check('respeta min y avisa si no cabe', r['tiny']['size'] == 40 and not r['tiny']['fits'], r['tiny'])
    check('los hijos escalan en la misma proporcion', abs(float(r['fs'][:-2]) - r['back']['size']) < 0.01, r['fs'])

    print('K.posterize')
    r = pg.evaluate('() => [K.posterize(0.3), K.posterize(0.299), K.posterize(1.05), K.posterize(1.05, 4), K.posterize(0)]')
    check('posterize(.3)=.3, (.299)=.2, (1.05)=1, (1.05,4)=1, (0)=0', r == [0.3, 0.2, 1, 1, 0], r)
    a_ = []
    for t in (2.0 / 30, 2.5 / 30): seek(t); a_.append(pg.evaluate("() => document.querySelector('#stop').style.transform"))
    check('la pieza stop-motion no cambia dentro del mismo 1/10 s', a_[0] == a_[1], a_[0])

    print('K.cut: estados y orden de busqueda')
    seek(0); s0 = pg.evaluate(STATE)
    check('cuadro 0: s2, s3 y s4 ocultos', all('hidden' in ln for ln in s0.splitlines()[1:4]) and 'visible' in s0.splitlines()[0])
    TS = [round(x * 0.05, 3) for x in range(0, 129)]
    fwd = {}
    for t in TS: seek(t); fwd[t] = pg.evaluate(STATE)
    rnd = TS[:]; random.Random(7).shuffle(rnd)
    bad = []
    for t in rnd:
        seek(t)
        if pg.evaluate(STATE) != fwd[t]: bad.append(t)
    check('el mismo estado yendo en orden o saltando al azar (129 instantes)', not bad, bad[:6])
    pg2 = page()
    fresh = {}
    for t in (5.9, 3.45, 0.0, 1.81):
        pg2.evaluate('t => { window.seek(t); }', t); fresh[t] = pg2.evaluate(STATE)
    check('el mismo estado en una pagina recien abierta', all(fresh[t] == fwd[round(t, 3)] if round(t, 3) in fwd else True for t in fresh)
          and fresh[0.0] == s0)
    seams = pg.evaluate('window.SEAMS')
    check('window.SEAMS tiene las 3 costuras', [(s['t'], s['axis'], s['out'], s['in']) for s in seams] ==
          [(1.8, 'x', '#s1', '#s2'), (3.4, 'y', '#s2', '#s3'), (5.0, 'z', '#s3', '#s4')], seams)
    check('window.TL expone los labels', pg.evaluate('Object.keys(window.TL.labels).length') == 8)
    b.close()

print('KIT v3', 'PASS' if ok else 'FAIL')
sys.exit(0 if ok else 1)
