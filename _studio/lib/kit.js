/* ==========================================================================
   Korvin Motion Kit — utilidades deterministas + componentes
   Todo lo animado sale de window.seek(t): sin requestAnimationFrame, sin Date.
   ========================================================================== */
(function () {
  const K = (window.K = {});
  gsap.registerPlugin(...[window.DrawSVGPlugin, window.MorphSVGPlugin, window.CustomEase, window.MotionPathPlugin, window.SplitText,
    window.Physics2DPlugin, window.PhysicsPropsPlugin, window.TextPlugin, window.CustomWiggle, window.CustomBounce, window.Flip].filter(Boolean));
  gsap.ticker.sleep(); // el reloj interno no corre: solo seek()

  // ---------- matematica ----------
  K.clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  K.lerp = (a, b, p) => a + (b - a) * p;
  K.prog = (t, t0, t1) => K.clamp((t - t0) / (t1 - t0));
  K.ease = {
    out3: p => 1 - Math.pow(1 - p, 3), out5: p => 1 - Math.pow(1 - p, 5), in3: p => p * p * p,
    io3: p => (p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2),
    outExpo: p => (p >= 1 ? 1 : 1 - Math.pow(2, -10 * p)),
    outBack: (p, c = 1.7) => 1 + (c + 1) * Math.pow(p - 1, 3) + c * Math.pow(p - 1, 2),
  };
  K.spring = (t, w = 12, z = 0.45) => {            // 0 -> 1; z<1 rebota, z=1 critico, z>1 sobreamortiguado
    if (t <= 0) return 0;
    if (z < 1) { const wd = w * Math.sqrt(1 - z * z);
      return 1 - Math.exp(-z * w * t) * (Math.cos(wd * t) + (z * w / wd) * Math.sin(wd * t)); }
    if (z === 1) return 1 - Math.exp(-w * t) * (1 + w * t);
    const s = w * Math.sqrt(z * z - 1), r1 = -z * w + s, r2 = -z * w - s;
    return 1 - (r2 * Math.exp(r1 * t) - r1 * Math.exp(r2 * t)) / (r2 - r1);
  };
  K.rng = seed => () => { seed |= 0; seed = (seed + 0x6d2b79f5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };

  // ---------- homografia: rectangulo (w,h) -> cuadrilatero -> matrix3d ----------
  function solve(A, b) { const n = b.length;
    for (let i = 0; i < n; i++) { let m = i; for (let r = i + 1; r < n; r++) if (Math.abs(A[r][i]) > Math.abs(A[m][i])) m = r;
      [A[i], A[m]] = [A[m], A[i]]; [b[i], b[m]] = [b[m], b[i]];
      for (let r = i + 1; r < n; r++) { const f = A[r][i] / A[i][i]; for (let c = i; c < n; c++) A[r][c] -= f * A[i][c]; b[r] -= f * b[i]; } }
    const x = new Array(n); for (let i = n - 1; i >= 0; i--) { let s = b[i]; for (let c = i + 1; c < n; c++) s -= A[i][c] * x[c]; x[i] = s / A[i][i]; } return x; }
  K.matrix3d = (w, h, q) => {
    const src = [[0, 0], [w, 0], [w, h], [0, h]], A = [], b = [];
    for (let i = 0; i < 4; i++) { const [x, y] = src[i], [u, v] = q[i];
      A.push([x, y, 1, 0, 0, 0, -u * x, -u * y]); b.push(u); A.push([0, 0, 0, x, y, 1, -v * x, -v * y]); b.push(v); }
    const [a, bb, c, d, e, f, g, hh] = solve(A, b);
    return `matrix3d(${[a, d, 0, g, bb, e, 0, hh, 0, 0, 1, 0, c, f, 0, 1].map(n => n.toFixed(8)).join(',')})`;
  };
  K.lerpQuad = (q1, q2, p) => q1.map((pt, i) => [K.lerp(pt[0], q2[i][0], p), K.lerp(pt[1], q2[i][1], p)]);

  // ---------- DOM ----------
  K.h = (html) => { const d = document.createElement('div'); d.innerHTML = html.trim(); return d.firstElementChild; };
  K.$ = (s, r = document) => r.querySelector(s);
  K.$$ = (s, r = document) => [...r.querySelectorAll(s)];

  // ---------- Iconos (trazo, 24x24) ----------
  const I = (d, sw = 2.2) => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round">${d}</svg>`;
  K.icon = {
    bolt: I('<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>'),
    cal: I('<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/><path d="m9 15 2 2 4-4"/>'),
    bell: I('<path d="M6 8a6 6 0 0 1 12 0c0 7 3 8 3 8H3s3-1 3-8"/><path d="M10 20a2 2 0 0 0 4 0"/>'),
    mic: I('<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>'),
    bag: I('<path d="M5 8h14l-1 13H6z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>'),
    user: I('<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>'),
    userplus: I('<circle cx="10" cy="8" r="4"/><path d="M2 21a8 8 0 0 1 16 0M19 8v6M16 11h6"/>'),
    ticket: I('<path d="M3 8a2 2 0 0 0 0 4v4a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-4a2 2 0 0 1 0-4V6a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2z"/><path d="M9 4v16" stroke-dasharray="2 3"/>'),
    handoff: I('<circle cx="7" cy="7" r="3"/><circle cx="17" cy="7" r="3"/><path d="M2 20a5 5 0 0 1 10 0M12 20a5 5 0 0 1 10 0"/>'),
    clock: I('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
    check: I('<path d="m5 12 5 5 9-10"/>', 2.8),
    card: I('<rect x="2" y="5" width="20" height="14" rx="3"/><path d="M2 10h20M6 15h4"/>'),
    link: I('<path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/>'),
    search: I('<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>'),
    brain: I('<path d="M9 3a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 3 3h1V3z"/><path d="M15 3a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-3 3h-1V3z"/>'),
    doc: I('<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h6"/>'),
    shield: I('<path d="M12 2 4 5v6c0 5 3.5 9 8 11 4.5-2 8-6 8-11V5z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>'),
    chart: I('<path d="M3 21h18"/><rect x="5" y="11" width="3" height="7"/><rect x="11" y="7" width="3" height="11"/><rect x="17" y="3" width="3" height="15"/>'),
    chat: I('<path d="M4 5h16v11H9l-5 4z"/>'),
    home: I('<path d="m3 11 9-8 9 8v10H3z"/>'),
    bank: I('<path d="m3 9 9-6 9 6M5 9v9M9 9v9M15 9v9M19 9v9M3 21h18"/>'),
    scissors: I('<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4 8.1 15.9M14.5 14.5 20 20M8.1 8.1 12 12"/>'),
    car: I('<path d="M5 17h14M3 17v-5l2-5h14l2 5v5"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/><path d="M3 12h18"/>'),
    key: I('<circle cx="8" cy="15" r="4"/><path d="m11 12 9-9M17 6l3 3"/>'),
    food: I('<path d="M4 3v8a3 3 0 0 0 6 0V3M7 3v18M17 3c-2 0-3 3-3 7h3v11"/>'),
    brief: I('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>'),
    truck: I('<path d="M2 6h12v10H2zM14 10h4l3 3v3h-7"/><circle cx="6" cy="17" r="2"/><circle cx="17" cy="17" r="2"/>'),
    spark: I('<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>'),
    moon: I('<path d="M21 13A9 9 0 1 1 11 3a7 7 0 0 0 10 10z"/>'),
    wa: `<svg viewBox="0 0 32 32"><path fill="#25d366" d="M16 3C9 3 3.3 8.6 3.3 15.6c0 2.5.7 4.8 2 6.8L3.5 29l6.8-1.8c1.9 1 4 1.6 5.7 1.6 7 0 12.7-5.7 12.7-12.7C28.7 8.6 23 3 16 3z"/><path fill="#fff" d="M11.6 9.6c-.3-.6-.6-.6-.9-.6h-.8c-.3 0-.7.1-1 .5-.4.4-1.3 1.3-1.3 3.1s1.3 3.6 1.5 3.9c.2.2 2.6 4.1 6.4 5.6 3.1 1.2 3.8 1 4.5.9.7-.1 2.2-.9 2.5-1.8.3-.9.3-1.6.2-1.8-.1-.2-.3-.2-.7-.4l-2.4-1.2c-.3-.1-.6-.2-.8.2l-1.1 1.4c-.2.2-.4.3-.8.1-.4-.2-1.6-.6-3-1.9-1.1-1-1.9-2.2-2.1-2.6-.2-.4 0-.6.2-.8l.6-.7c.2-.2.2-.4.4-.7.1-.3 0-.5 0-.7l-1.1-2.5z"/></svg>`,
  };

  // ---------- Marca Korvin (burbuja-K) ----------
  K.markPaths = {
    blue: 'M0,23 Q0,0 23,0 L158,0 Q163,0 160,4 L110,66 L66,67 L66,150 L110,150 L162,212 Q165,217 159,217 L112,217 L66,269 Q60,273 58,266 L58,217 L23,217 Q0,217 0,194 Z',
    gray: 'M118,109 L205,3 Q208,0 212,0 L303,0 Q326,0 326,23 L326,194 Q326,217 303,217 L269,217 L269,266 Q268,273 262,268 Z',
  };
  let gid = 0;
  K.mark = (w = 120, id = '') => { const g = 'kg' + (++gid);
    return `<svg ${id ? `id="${id}"` : ''} class="kmark" width="${w}" height="${(w * 271) / 326}" viewBox="0 0 326 271" style="overflow:visible">
      <defs><linearGradient id="${g}b" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4f66ff"/><stop offset="1" stop-color="#2238d6"/></linearGradient>
      <linearGradient id="${g}s" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c6ccda"/><stop offset="1" stop-color="#7f889c"/></linearGradient></defs>
      <path class="kb" fill="url(#${g}b)" d="${K.markPaths.blue}"/><path class="kg" fill="url(#${g}s)" d="${K.markPaths.gray}"/></svg>`; };

  K.lockup = (scale = 1) => `<div class="lockup" style="display:flex;align-items:center;gap:${36 * scale}px">
     ${K.mark(210 * scale)}
     <div style="display:flex;flex-direction:column;gap:${14 * scale}px">
       <div class="wordmark lk-word" style="font-size:${92 * scale}px;line-height:1;color:#fff">KORVIN</div>
       <div class="wordmark lk-sub" style="font-size:${27 * scale}px;line-height:1;color:var(--kx-400);letter-spacing:.62em">AI ASSISTANT</div>
     </div></div>`;

  // ---------- Grano de pelicula determinista ----------
  K.grain = (stage) => {
    const c = document.createElement('canvas'); c.id = 'grain'; c.width = 580; c.height = 1000; stage.appendChild(c);
    const ctx = c.getContext('2d'); const tiles = []; const r = K.rng(7);
    for (let k = 0; k < 8; k++) { const img = ctx.createImageData(290, 500);
      for (let i = 0; i < img.data.length; i += 4) { const v = r() * 255; img.data[i] = img.data[i + 1] = img.data[i + 2] = v; img.data[i + 3] = 255; }
      tiles.push(img); }
    c.style.width = '1160px'; c.style.height = '2000px';
    return t => { const k = Math.floor(t * 24) % 8; for (let y = 0; y < 2; y++) for (let x = 0; x < 2; x++) ctx.putImageData(tiles[(k + x + y * 2) % 8], x * 290, y * 500); };
  };

  // ---------- WhatsApp: telefono con chat programable ----------
  const TICK = `<svg class="tick" viewBox="0 0 18 11"><path d="M1 6l3 3 6-7M7 9l1 1 8-9" fill="none" stroke="#53bdeb" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
  K.waPhone = (opts = {}) => {
    const H = opts.h || 820, time = opts.clock || '11:47';
    const holder = K.h(`<div class="wa-holder abs" style="left:0;top:0;width:780px;height:${H * 2}px;transform-origin:0 0"></div>`);
    const el = K.h(`<div class="wa" style="height:${H}px">
      <div class="wa-status"><span>${time}</span><span class="ico">
        <svg width="18" height="12" viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx="1" fill="#fff"/><rect x="5" y="5" width="3" height="7" rx="1" fill="#fff"/><rect x="10" y="2" width="3" height="10" rx="1" fill="#fff"/><rect x="15" y="0" width="3" height="12" rx="1" fill="#fff" opacity=".4"/></svg>
        <svg width="16" height="12" viewBox="0 0 16 12"><path d="M8 11.5 1 4.5a10 10 0 0 1 14 0z" fill="#fff"/></svg>
        <svg width="26" height="12" viewBox="0 0 26 12"><rect x=".5" y=".5" width="22" height="11" rx="3" fill="none" stroke="#fff" opacity=".5"/><rect x="2" y="2" width="15" height="8" rx="2" fill="#fff"/><rect x="23.5" y="4" width="2" height="4" rx="1" fill="#fff" opacity=".5"/></svg></span></div>
      <div class="wa-head">
        <svg class="back" viewBox="0 0 24 24" fill="none" stroke="#e9edef" stroke-width="2.4" stroke-linecap="round"><path d="M15 5l-7 7 7 7"/></svg>
        <div class="wa-av">${opts.avatar || K.mark(26)}</div>
        <div><div class="wa-name">${opts.name || 'Korvin'}</div><div class="wa-sub"><span class="online">${opts.status || 'en línea'}</span><span class="typing" style="opacity:0">escribiendo…</span></div></div>
        <div class="acts"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#e9edef" stroke-width="2"><rect x="2" y="6" width="14" height="12" rx="2"/><path d="m16 10 6-3v10l-6-3"/></svg>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#e9edef" stroke-width="2"><path d="M5 3h4l2 5-3 2a11 11 0 0 0 6 6l2-3 5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2"/></svg></div>
      </div>
      <div class="wa-body"><div class="wa-list"></div></div>
      <div class="wa-input"><div class="pill"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#8696a0" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"/></svg>Mensaje</div>
        <div class="mic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg></div></div>
    </div>`);
    holder.appendChild(el);
    const list = el.querySelector('.wa-list');
    const rows = [];
    const api = { holder, el, H, rows };
    api.add = (m) => {
      let inner = '';
      if (m.type === 'day') inner = `<div class="wa-day">${m.text}</div>`;
      else if (m.type === 'typing') inner = `<div class="bub in"><div class="typing-b"><i></i><i></i><i></i></div></div>`;
      else if (m.type === 'voice') { const r = K.rng(m.seed || 3); let bars = '';
        for (let i = 0; i < 34; i++) bars += `<i style="height:${6 + Math.round(22 * Math.pow(Math.sin(i * .5 + 1) * .5 + .5, .8) * (0.45 + 0.55 * r()))}px"></i>`;
        inner = `<div class="bub ${m.side}"><div class="voice"><div class="play"><svg width="22" height="22" viewBox="0 0 24 24"><path d="M7 4v16l13-8z" fill="#e9edef"/></svg></div>
          <div class="wave">${bars}</div></div><div class="meta" style="margin-top:0"><span class="dur">${m.dur || '0:07'}</span>&nbsp;${m.time || ''}${m.side === 'out' ? TICK : ''}</div></div>`; }
      else {
        const btns = (m.buttons || []).map(b => `<div class="wa-btn">${b}<div class="rip"></div></div>`).join('');
        const cards = m.cards ? `<div class="card-row">${m.cards.map(c => `<div class="pcard"><div class="img" style="background:${c.bg}">${c.icon || ''}</div><div class="t">${c.t}</div><div class="p">${c.p}</div></div>`).join('')}</div>` : '';
        inner = `<div style="display:flex;flex-direction:column;max-width:82%;${m.side === 'out' ? 'align-items:flex-end' : ''}">
          <div class="bub ${m.side} ${btns ? 'hasbtn' : ''}" style="max-width:100%">${m.text}<span class="meta">${m.time || ''}${m.side === 'out' ? TICK : ''}</span></div>
          ${btns ? `<div class="wa-btns" style="align-self:stretch">${btns}</div>` : ''}${cards}</div>`;
      }
      const row = K.h(`<div class="wa-row ${m.side || 'center'}"><div class="wa-row-in">${inner}</div></div>`);
      list.appendChild(row);
      const rec = { m, row, inner: row.firstElementChild, bub: row.querySelector('.bub,.wa-day') };
      rows.push(rec); return rec;
    };
    // Mide alturas naturales y deja cada fila colapsada (height 0) hasta su momento
    api.measure = () => { rows.forEach(r => { r.hNat = r.row.offsetHeight; r.row.style.height = '0px'; }); };
    // Programa la aparicion de una fila en el timeline
    api.show = (tl, rec, t, dur = 0.34) => {
      tl.to(rec.row, { height: rec.hNat, duration: dur * 0.9, ease: 'power3.out' }, t);
      const origin = rec.m.side === 'out' ? '100% 100%' : rec.m.side === 'in' ? '0% 100%' : '50% 50%';
      tl.fromTo(rec.inner, { scale: 0.78, opacity: 0, y: 14, transformOrigin: origin },
        { scale: 1, opacity: 1, y: 0, duration: dur, ease: 'back.out(2.2)' }, t + 0.02);
    };
    api.hide = (tl, rec, t, dur = 0.2) => {
      tl.to(rec.row, { height: 0, duration: dur, ease: 'power2.in' }, t);
      tl.to(rec.inner, { opacity: 0, scale: 0.9, duration: dur * 0.8 }, t);
    };
    api.typingHeader = (tl, t0, t1) => {
      const on = el.querySelector('.online'), ty = el.querySelector('.typing');
      tl.to(on, { opacity: 0, duration: 0.12 }, t0).to(ty, { opacity: 1, duration: 0.12 }, t0)
        .to(ty, { opacity: 0, duration: 0.12 }, t1).to(on, { opacity: 1, duration: 0.12 }, t1);
    };
    // puntos del "escribiendo" (funcion de t)
    api.animTyping = (t) => rows.forEach(r => { if (r.m.type !== 'typing') return;
      r.row.querySelectorAll('.typing-b i').forEach((d, i) => { const s = Math.sin((t * 7.5 - i * 0.9));
        d.style.transform = `translateY(${-Math.max(0, s) * 5}px)`; d.style.opacity = 0.45 + 0.55 * Math.max(0, s); }); });
    // toque en un boton (ripple + dedo)
    api.tap = (tl, rec, idx, t) => {
      const b = rec.row.querySelectorAll('.wa-btn')[idx]; const rip = b.querySelector('.rip');
      tl.fromTo(rip, { scale: 0, opacity: 0.9 }, { scale: 1.3, opacity: 0, duration: 0.45, ease: 'power2.out' }, t);
      tl.to(b, { backgroundColor: '#2a3942', duration: 0.08 }, t).to(b, { backgroundColor: '#202c33', duration: 0.3 }, t + 0.25);
    };
    return api;
  };

  // ---------- Audio-reactivo (window.AUDIO_RMS / AUDIO_LOW de synth.export_rms) ----------
  // Devuelve {rms, low} en 0..1 para el instante t. Sin archivo de audio, devuelve ceros.
  K.audio = t => {
    const R = window.AUDIO_RMS, L = window.AUDIO_LOW, fps = window.AUDIO_FPS || 30;
    if (!R) return { rms: 0, low: 0 };
    const f = t * fps, i = Math.max(0, Math.min(R.length - 2, Math.floor(f))), k = f - i;
    return { rms: R[i] * (1 - k) + R[i + 1] * k, low: L[i] * (1 - k) + L[i + 1] * k };
  };

  // ---------- Marca del producto (window.MARCA de <producto>/marca.js) ----------
  // Cada video carga SU marca; kit expone K.brand y vuelca los colores a variables CSS
  // (--brand-primario, --brand-fondo, etc.) para no mezclar productos.
  K.brand = window.MARCA || null;
  K.applyBrand = () => {
    const M = window.MARCA; if (!M || !M.colores) return;
    const r = document.documentElement.style;
    Object.entries(M.colores).forEach(([k, v]) => r.setProperty('--brand-' + k, v));
  };
  K.applyBrand();


  // =====================================================================================
  // MOVIMIENTO PRO (v2, 02/10/2026) — todo es f(t): sin estado entre cuadros
  // Ideas tomadas de awesome-opus5-5-videos / HyperFrames / onetake (reimplementadas aqui).
  // =====================================================================================

  // Math.random con semilla: llamalo ANTES de crear objetos de librerias que usan random al construir
  // (mojs rand(), CustomWiggle 'random'). Sin esto cada worker del render veria otra cosa.
  K.seedRandom = (seed = 1) => { const r = K.rng(seed); Math.random = r; return r; };

  // Springs encadenadas: un valor que cambia de objetivo varias veces = suma de un spring por cambio.
  // keys: [{t:0, v:0}, {t:1.2, v:300}, {t:2.0, v:120}]  (el primero es el valor inicial)
  K.springs = (t, keys, w = 14, z = 0.62) => {
    let v = keys[0].v;
    for (let i = 1; i < keys.length; i++) v += (keys[i].v - keys[i - 1].v) * K.spring(t - keys[i].t, keys[i].w || w, keys[i].z || z);
    return v;
  };

  // Bordes elasticos (indicador de tabs, knob, subrayado): el borde que va adelante es rapido, el de atras lento.
  // keys: [{t, l, r}]  -> {l, r}
  K.edges = (t, keys, fast = { w: 22, z: 0.75 }, slow = { w: 11, z: 0.8 }) => {
    let l = keys[0].l, r = keys[0].r;
    for (let i = 1; i < keys.length; i++) {
      const k = keys[i], p = keys[i - 1], right = (k.l + k.r) > (p.l + p.r);
      const fl = right ? slow : fast, fr = right ? fast : slow;
      l += (k.l - p.l) * K.spring(t - k.t, fl.w, fl.z);
      r += (k.r - p.r) * K.spring(t - k.t, fr.w, fr.z);
    }
    return { l, r };
  };

  // Zoom en espacio logaritmico (se lee a una sola velocidad): s0 -> s1
  K.zoomLog = (t, t0, t1, s0, s1, ease = K.ease.io3) => s0 * Math.pow(s1 / s0, ease(K.prog(t, t0, t1)));

  // Texto que se escribe: devuelve el substring visible
  K.typeOn = (t, t0, text, cps = 22) => text.slice(0, Math.max(0, Math.min(text.length, Math.floor((t - t0) * cps + 1e-6))));

  // Scramble con semilla: los caracteres se resuelven de izquierda a derecha; los pendientes cambian 20 veces/s
  K.scramble = (t, t0, dur, text, seed = 7, chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%&*+') => {
    const p = K.prog(t, t0, t0 + dur); if (p >= 1) return text; if (t < t0) return '';
    const solved = Math.floor(p * text.length), tick = Math.floor(t * 20);
    let out = text.slice(0, solved);
    for (let i = solved; i < text.length; i++) {
      if (text[i] === ' ') { out += ' '; continue; }
      const h = K.rng(seed * 7919 + i * 104729 + tick * 1299709)();
      out += chars[Math.floor(h * chars.length)];
    }
    return out;
  };

  // Posicion de un elemento relativa al stage (para match cuts / shared element). Cacheada.
  const _mc = new Map();
  K.measure = (el, stage = document.getElementById('stage')) => {
    if (_mc.has(el)) return _mc.get(el);
    const a = el.getBoundingClientRect(), b = stage.getBoundingClientRect();
    const r = { x: a.left - b.left, y: a.top - b.top, w: a.width, h: a.height, cx: a.left - b.left + a.width / 2, cy: a.top - b.top + a.height / 2 };
    _mc.set(el, r); return r;
  };

  // Iris / flood: un circulo que cubre TODO (sobre-escala mas alla de las esquinas). Devuelve el radio para clip-path.
  K.coverRadius = (x, y, W = 1080, H = 1920) => 1.08 * Math.max(Math.hypot(x, y), Math.hypot(W - x, y), Math.hypot(x, H - y), Math.hypot(W - x, H - y));
  // Abre (o cierra) una capa con clip-path circular desde (x,y). Usa duraciones ~0.3–0.6 s.
  K.iris = (tl, el, t, { x = 540, y = 960, dur = 0.5, open = true, ease = 'power3.inOut' } = {}) => {
    const R = K.coverRadius(x, y), a = `circle(0px at ${x}px ${y}px)`, b = `circle(${R}px at ${x}px ${y}px)`;
    tl.fromTo(el, { clipPath: open ? a : b }, { clipPath: open ? b : a, duration: dur, ease, immediateRender: false }, t);
  };
  // Flood: una forma de color inunda el cuadro y se contrae revelando la escena siguiente (dur total ~0.6 s)
  K.flood = (tl, el, t, { x = 540, y = 960, x2 = 540, y2 = 960, dur = 0.6 } = {}) => {
    const R = K.coverRadius(x, y), R2 = K.coverRadius(x2, y2);
    tl.set(el, { opacity: 1, clipPath: `circle(0px at ${x}px ${y}px)` }, t)
      .to(el, { clipPath: `circle(${R}px at ${x}px ${y}px)`, duration: dur * 0.5, ease: 'power3.in' }, t)
      .set(el, { clipPath: `circle(${R2}px at ${x2}px ${y2}px)` }, t + dur * 0.5)
      .to(el, { clipPath: `circle(0px at ${x2}px ${y2}px)`, duration: dur * 0.5, ease: 'power3.out' }, t + dur * 0.5)
      .set(el, { opacity: 0 }, t + dur);
  };

  // Morph de contenedor (tarjeta -> boton -> pill...). Regla: el contenido entra DESPUES de que arranca el morph
  // y sale ANTES del siguiente. props: {width, height, borderRadius, backgroundColor, x, y}
  K.morph = (tl, el, t, props, dur = 0.55, ease = 'expo.inOut') => tl.to(el, { ...props, duration: dur, ease }, t);

  // Cursor: va de punto en punto con arco natural, hace click (presiona + onda) y arrastra.
  // path: [{t, x, y, click?:true, down?:true, up?:true}]; devuelve {el, update(t)}. Llamar update(t) en el porCuadro.
  K.cursor = (stage, path, { size = 64, color = '#111', ring = 'rgba(17,17,17,.25)', z = 900 } = {}) => {
    const el = K.h(`<div style="position:absolute;left:0;top:0;width:${size}px;height:${size}px;z-index:${z};pointer-events:none;transform-origin:8% 6%">
      <div class="cur-ring" style="position:absolute;left:${-size * 0.35}px;top:${-size * 0.35}px;width:${size * 0.7}px;height:${size * 0.7}px;border-radius:50%;border:3px solid ${ring};opacity:0"></div>
      <svg viewBox="0 0 24 24" width="${size}" height="${size}"><path d="M3 2l7.2 19 2.6-7.6L20.6 11z" fill="${color}" stroke="#fff" stroke-width="1.4" stroke-linejoin="round"/></svg></div>`);
    stage.appendChild(el); const rg = el.querySelector('.cur-ring');
    const pos = t => {
      if (t <= path[0].t) return { x: path[0].x, y: path[0].y };
      for (let i = 1; i < path.length; i++) {
        const a = path[i - 1], b = path[i];
        if (t <= b.t) {
          const p = K.ease.io3(K.prog(t, a.t, b.t)), arc = Math.sin(p * Math.PI) * Math.min(60, Math.hypot(b.x - a.x, b.y - a.y) * 0.12);
          const nx = -(b.y - a.y), ny = b.x - a.x, nl = Math.hypot(nx, ny) || 1;
          return { x: K.lerp(a.x, b.x, p) + nx / nl * arc, y: K.lerp(a.y, b.y, p) + ny / nl * arc };
        }
      }
      const l = path[path.length - 1]; return { x: l.x, y: l.y };
    };
    const update = t => {
      const { x, y } = pos(t); let s = 1, ro = 0, rs = 0.4;
      path.forEach(k => {
        if (k.click) { const d = t - k.t; if (d >= 0 && d < 0.18) s = Math.min(s, 1 - 0.18 * Math.sin(Math.PI * d / 0.18));
          if (d >= 0 && d < 0.45) { ro = 0.9 * (1 - d / 0.45); rs = 0.4 + 1.4 * K.ease.out3(d / 0.45); } }
      });
      const down = path.some((k, i) => k.down && t >= k.t && !path.slice(i + 1).some(u => u.up && t >= u.t));
      if (down) s = 0.86;
      el.style.transform = `translate(${x}px,${y}px) scale(${s})`;
      rg.style.opacity = ro; rg.style.transform = `scale(${rs})`;
    };
    return { el, update, pos };
  };

  // Filtros SVG: vidrio liquido (desplazamiento + borde cromatico) y goo (blur + umbral alfa).
  // Inyecta <svg><defs> una vez; usar con style="filter:url(#id)".
  K.filters = () => {
    if (document.getElementById('k-filters')) return;
    document.body.appendChild(K.h(`<svg id="k-filters" width="0" height="0" style="position:absolute">
      <filter id="k-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="12" result="b"/>
        <feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -10" result="g"/><feComposite in="SourceGraphic" in2="g" operator="atop"/></filter>
      <filter id="k-glass" x="-10%" y="-10%" width="120%" height="120%">
        <feTurbulence type="fractalNoise" baseFrequency="0.008 0.012" numOctaves="2" seed="7" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="18" xChannelSelector="R" yChannelSelector="G" result="d1"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="24" xChannelSelector="R" yChannelSelector="G" result="d2"/>
        <feColorMatrix in="d1" type="matrix" values="1 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 1 0" result="r"/>
        <feColorMatrix in="d2" type="matrix" values="0 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 1 0" result="gb"/>
        <feBlend in="r" in2="gb" mode="screen"/></filter>
    </svg>`));
  };

  // Lottie posicionable (lottie_svg.min.js): data = JSON en linea (fetch falla en file://)
  K.lottie = (container, data) => {
    const anim = window.lottie.loadAnimation({ container, renderer: 'svg', loop: false, autoplay: false, animationData: data });
    const fr = data.fr || 30, last = (data.op || 1) - 1;
    return { anim, draw: (tl0) => anim.goToAndStop(Math.max(0, Math.min(last, tl0 * fr)), true) };
  };

  // Correr un video completo OFF segundos (por ejemplo, para meterle un intro de marca adelante).
  // Mueve tweens, labels, cues y costuras (window.SEAMS); en el porCuadro usa t - OFF.
  K.shift = (tl, OFF, CUES) => { tl.shiftChildren(OFF, true); (CUES || []).forEach(c => { c.t = +(c.t + OFF).toFixed(4); });
    (window.SEAMS || []).forEach(s => { s.t = +(s.t + OFF).toFixed(4); }); };


  // =====================================================================================
  // COSTURAS Y TIEMPO (v3, 03/10/2026) — K.cut, K.nudgeEase, K.fitText, K.posterize
  // Del metodo (rol-editor: Costuras, Numeros de entrada/salida, Composicion). Todo f(t).
  // =====================================================================================

  // Costura con la ley del vector: A sale y B entra por el MISMO eje y en la MISMA direccion, cortando a mitad de vuelo.
  //   K.cut(tl, A, B, t, { axis: 'x'|'y'|'z', dir: -1|1, dist, outDur: .28, inDur: .34, blur: 10, text: true })
  //   x/y: A acelera (power4.in) en [t-outDur, t] hacia dir*dist; B frena (power4.out) en [t, t+inDur] desde -dir*dist.
  //        dist por defecto: 130 px en x, 230 px en y (≈12 % del cuadro). dir -1 = izquierda / arriba.
  //   z:   dir -1 = A se encoge a 0,8 y B llega grande (1,25 -> 1); dir +1 = A crece a 1,25 y B llega chica (0,75 -> 1).
  //   Opacidad: A llega a 0 en t (en t-0,05 si text: sin doble exposicion legible); B arranca en 0,35.
  //   Blur: pico `blur` px en la mitad rapida (0 = sin filtro; superficies 18–20).
  //   A y B: elemento, lista o selector. Su posicion de reposo es x/y = 0 (o `rest`, `restOut`, `restIn`) y scale 1.
  //   B queda oculto (autoAlpha 0) desde el cuadro 0, salvo que ya haya salido en otra costura o `hide0: false`.
  //   Registra la costura en window.SEAMS para tools/seams.py.
  //   force3D: false -> sin translate3d a mitad del tween (con translate3d, una escala puede variar 1 nivel entre renders).
  let _cutN = 0;
  const _cutOut = new Set();
  const _cutEls = x => {
    if (typeof x === 'string') return [K.$$(x), x];
    const els = x instanceof Element ? [x] : [...x];
    els.forEach(e => { if (!e.id) e.id = 'k-cut-' + (++_cutN); });
    return [els, els.map(e => '#' + CSS.escape(e.id)).join(',')];
  };
  K.cut = (tl, outEl, inEl, t, o = {}) => {
    const axis = o.axis || 'x', dir = o.dir < 0 ? -1 : o.dir > 0 ? 1 : -1, z = axis === 'z', p = axis === 'y' ? 'y' : 'x';
    const dist = o.dist ?? (axis === 'y' ? 230 : 130), outDur = o.outDur ?? 0.28, inDur = o.inDur ?? 0.34;
    const blur = o.blur ?? 10, text = o.text ?? true;
    const rA = o.restOut ?? o.rest ?? 0, rB = o.restIn ?? o.rest ?? 0;
    const [A, selA] = _cutEls(outEl), [B, selB] = _cutEls(inEl);
    const f = v => (blur > 0 ? { filter: `blur(${v}px)` } : {});
    const t0 = t - outDur, tOff = text ? t - 0.05 : t;
    // A sale: acelera y se va
    tl.fromTo(A, { ...(z ? { scale: 1 } : { [p]: rA }), ...f(0) },
      { ...(z ? { scale: dir < 0 ? 0.8 : 1.25 } : { [p]: rA + dir * dist }), ...f(blur), duration: outDur, ease: 'power4.in', force3D: false, immediateRender: false }, t0);
    tl.fromTo(A, { autoAlpha: 1 }, { autoAlpha: 0, duration: Math.max(0.04, tOff - t0), ease: 'power2.in', immediateRender: false }, t0);
    // B entra: llega rapido y se asienta
    tl.fromTo(B, { ...(z ? { scale: dir < 0 ? 1.25 : 0.75 } : { [p]: rB - dir * dist }), ...f(blur) },
      { ...(z ? { scale: 1 } : { [p]: rB }), ...f(0), duration: inDur, ease: 'power4.out', force3D: false, immediateRender: false }, t);
    tl.fromTo(B, { autoAlpha: 0.35 }, { autoAlpha: 1, duration: inDur * 0.7, ease: 'power2.out', immediateRender: false }, t);
    if (blur > 0) tl.set(B, { filter: 'none' }, t + inDur);
    // estado del cuadro 0: B oculto hasta su costura. '+=0' no mueve nada: deja el transform escrito por GSAP
    // (identidad) desde el cuadro 0, igual al que GSAP repone al volver atras -> mismo estado en cualquier orden de seek.
    gsap.set([...A, ...B], z ? { scale: '+=0' } : { [p]: '+=0' });
    if (o.hide0 !== false && !B.some(e => _cutOut.has(e))) gsap.set(B, { autoAlpha: 0 });
    A.forEach(e => _cutOut.add(e));
    (window.SEAMS = window.SEAMS || []).push({ t: +t.toFixed(4), out: selA, in: selB, axis, dir, outDur, inDur, text });
    return tl;
  };

  // Reacomodo (nudge): 3 tramos — power3.in 10 % del camino en el 20 % del tiempo, lineal 65 % en el 18 % siguiente,
  // power4.out 25 % en el 62 % final. Continua y monotona. Uso: ease: K.nudgeEase  (o ease: 'nudge').
  const _p3in = gsap.parseEase('power3.in'), _p4out = gsap.parseEase('power4.out');
  K.nudgeEase = p => (p <= 0 ? 0 : p >= 1 ? 1
    : p < 0.2 ? 0.1 * _p3in(p / 0.2)
    : p < 0.38 ? 0.1 + 0.65 * (p - 0.2) / 0.18
    : 0.75 + 0.25 * _p4out((p - 0.38) / 0.62));
  if (gsap.registerEase) gsap.registerEase('nudge', K.nudgeEase);

  // Ancho real del texto (cajas de los nodos de texto + img/svg/canvas en linea), SIN transforms:
  // quita un momento los transform del elemento, de sus hijos (spans con yPercent/scale) y de sus ancestros (camara).
  const _inkW = el => {
    const nodes = [...el.querySelectorAll('*')];
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) nodes.push(e);
    const props = ['transform', 'scale', 'rotate'];
    const saved = nodes.map(e => props.map(k => [e.style.getPropertyValue(k), e.style.getPropertyPriority(k)]));
    nodes.forEach(e => props.forEach(k => e.style.setProperty(k, 'none', 'important')));
    let l = Infinity, r = -Infinity;
    const rg = document.createRange(), tw = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    while (tw.nextNode()) {
      if (!tw.currentNode.textContent.trim()) continue;
      rg.selectNodeContents(tw.currentNode);
      for (const q of rg.getClientRects()) if (q.width > 0) { l = Math.min(l, q.left); r = Math.max(r, q.right); }
    }
    el.querySelectorAll('img,svg,canvas,video').forEach(e => {
      if (e.tagName.toLowerCase() === 'svg' && e.parentElement.closest('svg')) return;
      const q = e.getBoundingClientRect(); if (q.width > 0) { l = Math.min(l, q.left); r = Math.max(r, q.right); }
    });
    const w = r > l ? r - l : el.scrollWidth;
    nodes.forEach((e, i) => props.forEach((k, j) => { const [v, pr] = saved[i][j];
      if (v) e.style.setProperty(k, v, pr); else e.style.removeProperty(k); }));
    return w;
  };

  // Ajusta el font-size para que el texto mida <= maxW (ganchos largos: K.fitText('#q1', 940)).
  // Escala el elemento y sus hijos en la misma proporcion; nunca pasa del tamano original (o de `max`) ni baja de `min`.
  // Llamar DESPUES de document.fonts.ready y antes de SplitText/medidas. Repetirlo no lo achica de nuevo.
  // Devuelve { size, scale, width, fits }.
  const _fit0 = new WeakMap();
  K.fitText = (el, maxW, { min = 24, max } = {}) => {
    el = typeof el === 'string' ? K.$(el) : el;
    const again = _fit0.has(el);
    if (!again) _fit0.set(el, [el, ...el.querySelectorAll('*')].map(n => [n, parseFloat(getComputedStyle(n).fontSize), n.style.fontSize]));
    const orig = _fit0.get(el), base = orig[0][1], kMin = Math.min(1, min / base);
    const apply = k => orig.forEach(([n, fs, inl]) => { n.style.fontSize = k === 1 ? inl : (fs * k).toFixed(2) + 'px'; });
    let k = (max ?? base) / base;
    if (k !== 1 || again) apply(k);                                 // en una segunda llamada parte del tamano original
    let w = _inkW(el);
    for (let i = 0; i < 10 && w > maxW && k > kMin + 1e-6; i++) {   // proporcional; si cambia el corte de linea, repite
      k = Math.max(kMin, k * (maxW / w) * (i ? 0.995 : 1));
      apply(k); w = _inkW(el);
    }
    const fits = w <= maxW + 0.5;
    if (!fits) console.warn(`K.fitText: no cabe en ${maxW}px ni con ${min}px (mide ${w.toFixed(1)}px)`);
    return { size: +(base * k).toFixed(2), scale: +k.toFixed(4), width: +w.toFixed(1), fits };
  };
  K.fitText.measure = _inkW;

  // Stop-motion: congela el tiempo a `fps` cuadros por segundo (10 = cartoon). Uso: algo(K.posterize(t)).
  K.posterize = (t, fps = 10) => Math.floor(t * fps + 1e-6) / fps;

  // ---------- Timeline maestro ----------
  // K.install pone window.seek(t), window.TL (para tools/golden.py: lee TL.labels) y READY.
  K.timeline = () => gsap.timeline({ paused: true, defaults: { ease: 'power3.out' } });
  K.install = (tl, extra) => {
    window.seek = t => { tl.seek(t, false); extra && extra(t); };
    window.TL = tl;
    window.READY = true;
  };
})();
