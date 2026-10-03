"""Pista de prueba: 3 s de silencio con un beep de 1 kHz que arranca EXACTAMENTE en 1.000 s."""
import numpy as np, wave
SR, DUR, T0 = 48000, 3.0, 1.0
n = int(SR * DUR); x = np.zeros(n)
L = int(0.12 * SR); i0 = int(round(T0 * SR))
tt = np.arange(L) / SR
env = np.minimum(1, tt / 0.002) * np.exp(-tt / 0.045)   # ataque de 2 ms, caida rapida
x[i0:i0 + L] = 0.8 * np.sin(2 * np.pi * 1000 * tt) * env
pcm = (np.clip(x, -1, 1) * 32767).astype(np.int16)
st = np.stack([pcm, pcm], 1).ravel()
with wave.open('beep.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())
print('beep.wav ok — onset en', i0 / SR, 's')
