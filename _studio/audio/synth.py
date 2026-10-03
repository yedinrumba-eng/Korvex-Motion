"""
Motion Studio — sintetizador en numpy (determinista, sin samples externos).
Instrumentos: kick, clap, hats, bajo, pads, plucks, campanas, risers, impactos y SFX de UI.
"""
import numpy as np
from scipy import signal

SR = 48000
RNG = np.random.default_rng(1234)


def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)


NOTE = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7,
        'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11}


def n2m(name):
    """'D3' -> 50"""
    for k in sorted(NOTE, key=len, reverse=True):
        if name.startswith(k):
            return 12 * (int(name[len(k):]) + 1) + NOTE[k]
    raise ValueError(name)


class Track:
    """Buffer estereo al que se le suman eventos."""

    def __init__(self, dur):
        self.n = int(dur * SR)
        self.buf = np.zeros((self.n, 2))

    def add(self, t, x, gain=1.0, pan=0.0):
        i0 = int(round(t * SR))
        if x.ndim == 1:
            l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
            x = np.stack([x * l * 1.414, x * r * 1.414], 1)
        if i0 < 0:
            x = x[-i0:]; i0 = 0
        i1 = min(self.n, i0 + len(x))
        if i1 > i0:
            self.buf[i0:i1] += x[:i1 - i0] * gain


# ---------------------------------------------------------------- utilidades
def tt(dur):
    return np.arange(int(dur * SR)) / SR


def env_adsr(n, a=0.005, d=0.1, s=0.7, r=0.2, hold=None):
    """ADSR en muestras. hold = duracion antes del release (s)."""
    t = np.arange(n) / SR
    hold = hold if hold is not None else n / SR - r
    e = np.where(t < a, t / max(a, 1e-6), 1.0)
    dec = (t >= a) & (t < a + d)
    e = np.where(dec, 1 - (1 - s) * (t - a) / max(d, 1e-6), e)
    e = np.where(t >= a + d, s, e)
    rel = t >= hold
    e = np.where(rel, e * np.clip(1 - (t - hold) / max(r, 1e-6), 0, 1), e)
    return e


def exp_env(n, tau):
    return np.exp(-np.arange(n) / SR / tau)


def lp(x, fc, order=2):
    sos = signal.butter(order, min(fc, SR * 0.45), 'low', fs=SR, output='sos')
    return signal.sosfilt(sos, x, axis=0)


def hp(x, fc, order=2):
    sos = signal.butter(order, fc, 'high', fs=SR, output='sos')
    return signal.sosfilt(sos, x, axis=0)


def bp(x, f1, f2, order=2):
    sos = signal.butter(order, [f1, min(f2, SR * 0.45)], 'band', fs=SR, output='sos')
    return signal.sosfilt(sos, x, axis=0)


def saw_additive(f, dur, bright=1.0, phase=0.0, fc=None):
    """Sierra de banda limitada por suma de armonicos, con 'filtro' espectral opcional (fc)."""
    t = tt(dur)
    y = np.zeros_like(t)
    nmax = int(min(80, (SR * 0.45) / f))
    for k in range(1, nmax + 1):
        a = 1.0 / k
        if fc:
            a *= 1.0 / np.sqrt(1 + (k * f / fc) ** 4)
        y += a * np.sin(2 * np.pi * k * f * t + phase * k)
    return y * 0.6


def sine(f, dur, phase=0.0):
    return np.sin(2 * np.pi * f * tt(dur) + phase)


def noise(dur, seed=None):
    r = np.random.default_rng(seed) if seed is not None else RNG
    return r.standard_normal(int(dur * SR))


# ---------------------------------------------------------------- reverb / delay
def make_ir(dur=2.4, predelay=0.02, damp=6000, seed=7):
    r = np.random.default_rng(seed)
    n = int(dur * SR)
    t = np.arange(n) / SR
    env = np.exp(-t * 6.9 / dur)
    ir = r.standard_normal((n, 2)) * env[:, None]
    ir = lp(ir, damp, 1)
    ir = np.vstack([np.zeros((int(predelay * SR), 2)), ir])
    ir /= np.sqrt((ir ** 2).sum(0))
    return ir


def reverb(x, ir, wet=0.3):
    y = np.stack([signal.fftconvolve(x[:, c], ir[:, c])[:len(x)] for c in range(2)], 1)
    return x * (1 - wet) + y * wet


def delay(x, secs, fb=0.35, mix=0.3, n=5, pingpong=True):
    y = x.copy()
    d = int(secs * SR)
    for k in range(1, n + 1):
        g = mix * fb ** (k - 1)
        sh = np.zeros_like(x)
        sh[d * k:] = x[:-d * k] if d * k < len(x) else 0
        if pingpong:
            if k % 2:
                sh = sh[:, ::-1]
        y += sh * g
    return y


# ---------------------------------------------------------------- instrumentos
def kick(dur=0.5, f0=150, f1=44, punch=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t / 0.035)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t / 0.28)
    click = bp(noise(dur, 3), 1500, 6000) * np.exp(-t / 0.004) * 0.35 * punch
    return np.tanh((body + click) * 1.6) * 0.9


def clap(dur=0.35, seed=5):
    n = int(dur * SR); t = np.arange(n) / SR
    nz = bp(noise(dur, seed), 900, 5000)
    e = np.zeros(n)
    for k, off in enumerate([0, 0.011, 0.022]):
        i = int(off * SR); e[i:] += np.exp(-(t[:n - i]) / 0.008) * (0.6 if k < 2 else 1)
    e += np.exp(-t / 0.12) * 0.35 * (t > 0.022)
    return nz * e * 0.7


def snare(dur=0.3, seed=9):
    t = tt(dur)
    body = np.sin(2 * np.pi * 190 * t) * np.exp(-t / 0.05) * 0.5
    nz = bp(noise(dur, seed), 1500, 9000) * np.exp(-t / 0.09)
    return (body + nz) * 0.6


def hat(dur=0.06, open_=False, seed=11):
    d = 0.32 if open_ else dur
    t = tt(d)
    nz = hp(noise(d, seed), 7000, 2)
    return nz * np.exp(-t / (0.09 if open_ else 0.018)) * (0.35 if open_ else 0.3)


def shaker(dur=0.08, seed=13):
    t = tt(dur)
    e = np.minimum(1, t / 0.02) * np.exp(-t / 0.03)
    return bp(noise(dur, seed), 4000, 11000) * e * 0.25


def bass_pluck(f, dur=0.22, bright=900):
    n = int(dur * SR)
    a = saw_additive(f, dur, fc=bright * 2.2) * exp_env(n, 0.045)
    b = saw_additive(f, dur, fc=bright * 0.6) * (1 - exp_env(n, 0.045))
    sub = np.sin(2 * np.pi * f * tt(dur)) * 0.8
    y = (a + b * 0.8 + sub) * env_adsr(n, 0.003, 0.08, 0.75, 0.05)
    return np.tanh(y * 1.3) * 0.7


def sub_bass(f, dur):
    n = int(dur * SR)
    return np.sin(2 * np.pi * f * tt(dur)) * env_adsr(n, 0.01, 0.1, 0.9, 0.08) * 0.8


def pad(freqs, dur, fc=1800, a=0.6, r=0.8, detune=0.12, voices=3):
    """Pad de sierras desafinadas, estereo."""
    n = int(dur * SR)
    L = np.zeros(n); R = np.zeros(n)
    for fi, f in enumerate(freqs):
        for v in range(voices):
            cents = (v - (voices - 1) / 2) * detune * 100 / max(1, (voices - 1) / 2) if voices > 1 else 0
            ff = f * 2 ** (cents / 1200)
            y = saw_additive(ff, dur, fc=fc, phase=(fi * 1.3 + v * 2.1))
            pan = (v / max(1, voices - 1)) * 2 - 1
            L += y * (1 - pan) * 0.5; R += y * (1 + pan) * 0.5
    e = env_adsr(n, a, 0.3, 0.85, r)
    out = np.stack([L * e, R * e], 1) / (len(freqs) * voices) * 1.6
    return out


def stab(freqs, dur=0.35, fc=3500):
    n = int(dur * SR)
    y = sum(saw_additive(f, dur, fc=fc, phase=i) + saw_additive(f * 1.006, dur, fc=fc, phase=i + 1) for i, f in enumerate(freqs))
    y = y / len(freqs) * exp_env(n, 0.12) * env_adsr(n, 0.002, 0.05, 1, 0.05)
    return y


def pluck(f, dur=0.5, bright=4000, decay=0.18):
    n = int(dur * SR)
    a = saw_additive(f, dur, fc=bright) * exp_env(n, 0.03)
    b = saw_additive(f, dur, fc=bright * 0.25)
    y = (a + b * 0.7) * exp_env(n, decay) * env_adsr(n, 0.002, 0.02, 1, 0.03)
    return y * 0.6


def bell(f, dur=1.2, decay=0.45):
    t = tt(dur); n = len(t)
    y = (np.sin(2 * np.pi * f * t) + 0.45 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t / 0.15)
         + 0.25 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t / 0.06))
    return y * exp_env(n, decay) * env_adsr(n, 0.001, 0.01, 1, 0.02) * 0.35


# ---------------------------------------------------------------- acusticos (latino calido / cinematico)
def nylon(f, dur=1.6, bright=0.45, decay=1.1, seed=1):
    """Guitarra de nylon: Karplus-Strong vectorizado por periodo + cuerpo. bright 0..1."""
    n = int(dur * SR); N = max(4, int(round(SR / f - 0.5)))
    r = np.random.default_rng(seed)
    exc = r.uniform(-1, 1, N)
    k = max(1, int(N * (0.55 - 0.5 * bright)))
    exc = np.convolve(exc, np.ones(k) / k, 'same'); exc -= exc.mean()
    exc *= np.sin(np.pi * np.arange(N) / N) ** 0.5          # posicion de pulsado suave
    y = np.zeros(n + N + 1); y[1:N + 1] = exc
    g = np.exp(-N / (SR * decay))
    pos = N + 1
    while pos < len(y):
        end = min(pos + N, len(y))
        y[pos:end] = g * 0.5 * (y[pos - N:end - N] + y[pos - N - 1:end - N - 1])
        pos = end
    y = y[1:]
    fa = SR / (N + 0.5)                                      # afinacion exacta por re-muestreo
    idx = np.arange(n) * (f / fa)
    y = np.interp(idx, np.arange(len(y)), y)
    body = bp(y, 90, 260, 2) * 0.45 + lp(y, 4200, 2)
    body /= (np.abs(body).max() + 1e-9)
    return body * env_adsr(n, 0.003, 0.02, 1, 0.05) * 0.7


def strum(freqs, dur=1.6, down=True, spread=0.018, bright=0.45, decay=1.0, seed=1, vel=1.0):
    """Rasgueo: cuerdas desfasadas `spread` s (abajo = graves primero)."""
    fs = list(freqs) if down else list(freqs)[::-1]
    out = np.zeros(int((dur + spread * len(fs)) * SR))
    for i, f in enumerate(fs):
        x = nylon(f, dur, bright, decay, seed + i) * (vel * (0.85 + 0.15 * (i % 2)))
        i0 = int(i * spread * SR); out[i0:i0 + len(x)] += x
    return out[:int(dur * SR)] / np.sqrt(len(fs))


def epiano(f, dur=1.6, vel=0.8, decay=1.5):
    """Piano electrico (FM tipo Rhodes): calido, con 'ladrido' corto de la pua."""
    t = tt(dur); n = len(t)
    I = (0.8 + 1.6 * vel) * np.exp(-t / 0.3)
    y = np.sin(2 * np.pi * f * t + I * np.sin(2 * np.pi * f * t))
    y += 0.18 * vel * np.sin(2 * np.pi * f * 7.0 * t + 0.5 * np.sin(2 * np.pi * f * t)) * np.exp(-t / 0.04)
    y *= 1 + 0.06 * np.sin(2 * np.pi * 4.6 * t)            # tremolo leve
    return y * exp_env(n, decay) * env_adsr(n, 0.002, 0.05, 1, 0.12) * 0.28


def epiano_chord(freqs, dur=1.6, vel=0.7, decay=1.5, spread=0.012):
    out = np.zeros(int((dur + spread * len(freqs)) * SR))
    for i, f in enumerate(freqs):
        x = epiano(f, dur, vel * (0.9 + 0.1 * ((i + 1) % 2)), decay)
        i0 = int(i * spread * SR); out[i0:i0 + len(x)] += x
    return out[:int(dur * SR)] / np.sqrt(len(freqs))


def upright(f, dur=0.6, decay=0.45, seed=5):
    """Contrabajo pizzicato: fundamental redonda + golpe de dedo."""
    t = tt(dur); n = len(t)
    y = np.sin(2 * np.pi * f * t) + 0.45 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.12) \
        + 0.15 * np.sin(6 * np.pi * f * t) * np.exp(-t / 0.05)
    thump = lp(noise(dur, seed), 350, 2) * np.exp(-t / 0.018) * 0.35
    return (y * exp_env(n, decay) + thump) * env_adsr(n, 0.006, 0.05, 1, 0.06) * 0.55


def conga(f=210, dur=0.4, slap=False, seed=3):
    """Conga / tumbadora: tono con caida de pitch + parche (slap = seco y brillante)."""
    t = tt(dur); fr = f * (1 + 0.22 * np.exp(-t / 0.018))
    y = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / (0.05 if slap else 0.17))
    y += bp(noise(dur, seed), 900, 6000, 2) * np.exp(-t / (0.028 if slap else 0.012)) * (0.7 if slap else 0.22)
    return y * 0.55


def guira(dur=0.11, seed=21, ridges=95.0):
    """Guira dominicana: raspado metalico corto."""
    t = tt(dur)
    x = bp(noise(dur, seed), 3500, 12000, 2)
    am = 0.5 + 0.5 * (np.sin(2 * np.pi * ridges * t) > 0)
    env = np.minimum(1, t / 0.012) * np.exp(-t / (dur * 0.45))
    return x * am * env * 0.35


def rim(seed=4):
    t = tt(0.08)
    y = np.sin(2 * np.pi * 1750 * t) * np.exp(-t / 0.007) + bp(noise(0.08, seed), 2000, 7000, 2) * np.exp(-t / 0.005) * 0.6
    return y * 0.45


def taiko(f=62, dur=1.4, v=1.0, seed=2):
    """Tambor grande cinematografico."""
    t = tt(dur); fr = f * (1 + 0.7 * np.exp(-t / 0.025))
    y = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.4)
    y += lp(noise(dur, seed), 1400, 2) * np.exp(-t / 0.035) * 0.55
    y += bp(noise(dur, seed + 1), 150, 600, 2) * np.exp(-t / 0.18) * 0.35
    return y * v * 0.8


def strings(freqs, dur, a=0.8, r=1.2, fc=2200, seed=0):
    """Colchon de cuerdas: sierras desafinadas con vibrato lento y ataque largo."""
    t = tt(dur); n = len(t); out = np.zeros(n)
    rr = np.random.default_rng(seed)
    for f in freqs:
        for d in (-0.09, 0.0, 0.1):
            vib = 1 + 0.0035 * np.sin(2 * np.pi * (4.8 + rr.uniform(-.4, .4)) * t + rr.uniform(0, 6))
            ph = 2 * np.pi * np.cumsum(f * 2 ** (d / 12) * vib) / SR
            nh = int(min(30, SR * 0.45 / f)); y = np.zeros(n)
            for k in range(1, nh + 1):
                y += np.sin(k * ph) / k / np.sqrt(1 + (k * f / fc) ** 4)
            out += y
    return out / (len(freqs) * 3) * env_adsr(n, a, 0.2, 0.9, r) * 0.5


def sfx_sizzle(dur=3.0, seed=7, density=170):
    """Chisporroteo de sarten: siseo fluctuante + crepitaciones (mono)."""
    r = np.random.default_rng(seed); n = int(dur * SR)
    mod = lp(np.abs(noise(dur, seed + 1)), 9, 2); mod = 0.45 + 0.55 * mod / (mod.max() + 1e-9)
    hiss = bp(noise(dur, seed), 2500, 12000, 2) * mod
    pops = np.zeros(n)
    for i in r.integers(0, n - 600, r.poisson(density * dur)):
        L = int(r.integers(30, 260)); a = r.uniform(0.15, 1.0) ** 2
        pops[i:i + L] += a * np.exp(-np.arange(L) / (L / 5)) * r.choice([-1, 1]) * r.standard_normal(L)
    pops = hp(pops, 1200, 2)
    y = hiss * 0.1 + pops * 0.5
    return y * np.minimum(1, np.arange(n) / SR / 0.05)


# ---------------------------------------------------------------- SFX
def sfx_pop(v=1.0):
    t = tt(0.12)
    f = 700 + 700 * (1 - np.exp(-t / 0.02))
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.035)
    y += bp(noise(0.12, 21), 2000, 6000) * np.exp(-t / 0.004) * 0.3
    return y * 0.45 * v


def sfx_send(v=1.0):
    t = tt(0.1)
    f = 1500 + 900 * (t / 0.1)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.022)
    return y * 0.3 * v


def sfx_tick(p=0, v=1.0):
    t = tt(0.05)
    f = 1800 * 2 ** (p / 12 * 2)
    y = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.012) + bp(noise(0.05, 31 + p), 3000, 9000) * np.exp(-t / 0.003) * 0.4
    return y * 0.35 * v


def sfx_tap(v=1.0):
    t = tt(0.06)
    y = np.sin(2 * np.pi * 520 * t) * np.exp(-t / 0.015) + bp(noise(0.06, 41), 1000, 5000) * np.exp(-t / 0.004) * 0.6
    return y * 0.45 * v


def sfx_whoosh(dur=0.45, v=1.0, seed=51):
    n = int(dur * SR); t = np.arange(n) / SR
    x = noise(dur, seed)
    out = np.zeros(n)
    # barrido de banda por bloques
    blocks = 24
    for b in range(blocks):
        i0, i1 = b * n // blocks, (b + 1) * n // blocks
        p = b / (blocks - 1)
        fc = 300 * (12 ** p)
        seg = bp(x[max(0, i0 - 2000):i1], fc * 0.6, fc * 1.8)[-(i1 - i0):]
        out[i0:i1] = seg
    e = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 1.5
    y = out * e
    pan = np.linspace(-0.7, 0.7, n)
    return np.stack([y * (1 - pan) * .7, y * (1 + pan) * .7], 1) * 0.9 * v


def sfx_riser(dur=1.0, v=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    x = noise(dur, 61)
    out = np.zeros(n); blocks = 30
    for b in range(blocks):
        i0, i1 = b * n // blocks, (b + 1) * n // blocks
        fc = 400 * (20 ** (b / (blocks - 1)))
        out[i0:i1] = bp(x[max(0, i0 - 2000):i1], fc * 0.7, fc * 1.5)[-(i1 - i0):]
    f = 180 * 2 ** (2.5 * t / dur)
    tone = saw_additive(1, 0.001)  # placeholder
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.25
    e = (t / dur) ** 2.2
    return (out * 0.8 + tone) * e * 0.6 * v


def sfx_boom(v=1.0, dur=2.2):
    t = tt(dur); n = len(t)
    f = 32 + 60 * np.exp(-t / 0.08)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.7)
    nz = lp(noise(dur, 71), 1800) * np.exp(-t / 0.18) * 0.7
    crack = bp(noise(dur, 72), 2000, 9000) * np.exp(-t / 0.02) * 0.4
    return np.tanh((sub * 1.2 + nz + crack) * 1.4) * 0.9 * v


def sfx_shimmer(dur=1.8, seed=81):
    r = np.random.default_rng(seed)
    out = np.zeros((int((dur + 1.5) * SR), 2))
    notes = [n2m(x) for x in ['D6', 'A5', 'F6', 'E6', 'A6', 'C7', 'D7']]
    k = 0
    tpos = 0.0
    while tpos < dur:
        m = notes[k % len(notes)]; k += 1
        b = bell(midi(m), 1.2, 0.35) * (0.25 + 0.2 * r.random()) * (tpos / dur + 0.2)
        pan = r.uniform(-0.8, 0.8)
        i = int(tpos * SR)
        out[i:i + len(b), 0] += b * (1 - pan) * .7
        out[i:i + len(b), 1] += b * (1 + pan) * .7
        tpos += 0.09 + 0.05 * r.random()
    return out


def sfx_sweep(dur=1.0):
    t = tt(dur); n = len(t)
    x = bp(noise(dur, 91), 3500, 11000)
    e = np.sin(np.pi * t / dur) ** 2
    y = x * e * 0.25
    pan = np.linspace(-0.8, 0.8, n)
    return np.stack([y * (1 - pan), y * (1 + pan)], 1)


def sfx_chime():
    a = bell(midi(n2m('A5')), 1.2, 0.4); b = bell(midi(n2m('E6')), 1.4, 0.5)
    out = np.zeros(len(b) + int(0.12 * SR)); out[:len(a)] += a; out[int(.12 * SR):] += b
    return out * 0.9


# ---------------------------------------------------------------- master
def master(mix, target_peak_db=-1.0, drive=1.25):
    mix = hp(mix, 28, 2)
    mix = np.tanh(mix * drive) / np.tanh(drive)
    pk = np.abs(mix).max()
    mix = mix / pk * 10 ** (target_peak_db / 20)
    return mix


def write_wav(path, x):
    import wave
    pcm = (np.clip(x, -1, 1) * 32767).astype(np.int16)
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())


def duck_curve(n, kick_times, depth=0.55, rel=0.16):
    g = np.ones(n)
    t = np.arange(n) / SR
    for kt in kick_times:
        i0 = int(kt * SR); i1 = min(n, i0 + int(rel * 3 * SR))
        if i0 >= n:
            continue
        tau = t[i0:i1] - kt
        g[i0:i1] = np.minimum(g[i0:i1], 1 - depth * np.exp(-tau / rel) * np.minimum(1, tau / 0.004 + 0.2))
    return g


# ---------------------------------------------------------------- samples (Kenney CC0, en assets/sfx)
_SAMPLE_CACHE = {}


def load_sample(path, gain=1.0):
    """Decodifica cualquier audio (ogg/wav/mp3) con ffmpeg a float estereo 48 kHz."""
    import subprocess
    if path not in _SAMPLE_CACHE:
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'],
                             capture_output=True, check=True).stdout
        _SAMPLE_CACHE[path] = np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)
    return _SAMPLE_CACHE[path] * gain


# ---------------------------------------------------------------- audio-reactivo
def export_rms(mix, fps, path_js, dur=None):
    """Escribe window.AUDIO_RMS / window.AUDIO_LOW (0..1 por cuadro) para que el video 'respire' con la musica.
    El index.html lo carga con <script src="audio-rms.js"></script> (fetch no funciona en file://)."""
    m = mix.mean(1) if mix.ndim == 2 else mix
    low = lp(m, 150, 2)
    n = int((dur or len(m) / SR) * fps)
    hop = SR / fps

    def env(x):
        out = []
        for f in range(n):
            a, b = int(max(0, (f - 0.5) * hop)), int(min(len(x), (f + 1.5) * hop))
            out.append(float(np.sqrt((x[a:b] ** 2).mean())) if b > a else 0.0)
        out = np.array(out)
        out = out / (np.percentile(out, 98) + 1e-9)
        return np.clip(out, 0, 1).round(3).tolist()
    open(path_js, 'w').write(f'window.AUDIO_FPS={fps};window.AUDIO_RMS={env(m)};window.AUDIO_LOW={env(low)};')


# ---------------------------------------------------------------- loudness (ITU-R BS.1770 / EBU R128)
def _kweight(x):
    """Filtro K (dos etapas) a 48 kHz."""
    b1, a1 = [1.53512485958697, -2.69169618940638, 1.19839281085285], [1.0, -1.69065929318241, 0.73248077421585]
    b2, a2 = [1.0, -2.0, 1.0], [1.0, -1.99004745483398, 0.99007225036621]
    return signal.lfilter(b2, a2, signal.lfilter(b1, a1, x, axis=0), axis=0)


def lufs(x):
    """Loudness integrado (LUFS) con compuertas absoluta (-70) y relativa (-10 LU)."""
    x = x if x.ndim == 2 else x[:, None]
    y = _kweight(x)
    blk, hop = int(0.4 * SR), int(0.1 * SR)
    if len(y) < blk:
        return -70.0
    ms = np.array([(y[i:i + blk] ** 2).mean(0).sum() for i in range(0, len(y) - blk + 1, hop)])
    lk = -0.691 + 10 * np.log10(ms + 1e-12)
    g = ms[lk > -70]
    if not len(g):
        return -70.0
    rel = -0.691 + 10 * np.log10(g.mean()) - 10
    g2 = ms[(lk > -70) & (lk > rel)]
    return float(-0.691 + 10 * np.log10(g2.mean() + 1e-12))


def true_peak_db(x, os=4):
    up = signal.resample_poly(x, os, 1, axis=0)
    return float(20 * np.log10(np.abs(up).max() + 1e-12))


def limiter(x, ceil_db=-1.0, release=0.08, look=0.005):
    """Limitador con anticipacion: nunca pasa de ceil_db (muestra); el true peak se revisa afuera."""
    from scipy.ndimage import maximum_filter1d
    thr = 10 ** (ceil_db / 20)
    pk = maximum_filter1d(np.abs(x).max(1) if x.ndim == 2 else np.abs(x), size=max(1, int(look * SR)) * 2 + 1)
    g = np.minimum(1.0, thr / (pk + 1e-12))
    a = np.exp(-1.0 / (release * SR))
    gs = 1 - signal.lfilter([1 - a], [1, -a], 1 - g)          # suaviza la recuperacion
    gs = np.minimum(gs, g)
    return x * (gs[:, None] if x.ndim == 2 else gs)


def master_lufs(mix, target=-14.0, tp=-1.0, drive=1.15):
    """Master para redes: -14 LUFS integrados y true peak <= -1 dBTP (lo que IG/TikTok normalizan)."""
    mix = hp(mix, 28, 2)
    mix = np.tanh(mix * drive) / np.tanh(drive)
    for _ in range(3):
        mix = mix * 10 ** ((target - lufs(mix)) / 20)
        mix = limiter(mix, tp - 0.3)
        if true_peak_db(mix) <= tp + 0.05 and abs(lufs(mix) - target) < 0.5:
            break
    return mix
