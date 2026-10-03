"""Chroma key de fotos con pantalla verde + deteccion de las 4 esquinas de la pantalla.
Uso: python key.py <carpeta_origen> <carpeta_salida> foto1 foto2 ...   (nombres sin .png)
Salida: <nombre>_keyed.png (RGBA, pantalla transparente) y quads.json (esquinas TL,TR,BR,BL en px)."""
import cv2, numpy as np, json, sys, os
SRC = sys.argv[1].rstrip('/\\') + os.sep
OUT = sys.argv[2].rstrip('/\\') + os.sep
quads = json.load(open(OUT + 'quads.json')) if os.path.exists(OUT + 'quads.json') else {}
for name in sys.argv[3:]:
    im = cv2.imread(SRC + name + '.png').astype(np.float32)
    b, g, r = im[..., 0], im[..., 1], im[..., 2]
    # "verdosidad": cuanto domina el verde sobre el mayor de rojo/azul
    gd = g - np.maximum(r, b)
    alpha = 1 - np.clip((gd - 25) / 60, 0, 1)            # 0 = pantalla, 1 = foto
    # despill: el verde que rebota en los bordes se baja al max(r,b)
    g2 = np.where(gd > 0, np.maximum(r, b), g)   # despill: el verde no pasa del max(rojo, azul)
    out = np.dstack([b, g2, r, alpha * 255]).clip(0, 255).astype(np.uint8)
    cv2.imwrite(OUT + name + '_keyed.png', out)

    # --- esquinas: contorno del area verde mas grande
    mask = (gd > 60).astype(np.uint8) * 255
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cnts, key=cv2.contourArea)
    hull = cv2.convexHull(c)
    peri = cv2.arcLength(hull, True)
    for eps in np.linspace(0.005, 0.1, 200):
        ap = cv2.approxPolyDP(hull, eps * peri, True)
        if len(ap) == 4:
            break
    pts = ap.reshape(-1, 2).astype(float)
    # Refinar: ajustar una recta a los puntos del casco cerca de cada lado (ignora esquinas redondeadas)
    P = c.reshape(-1, 2).astype(float)
    lines = []
    for i in range(4):
        p0, p1 = pts[i], pts[(i + 1) % 4]
        d = p1 - p0; L = np.linalg.norm(d); u = d / L; nrm = np.array([-u[1], u[0]])
        rel = P - p0; along = rel @ u; perp = np.abs(rel @ nrm)
        sel = P[(along > 0.2 * L) & (along < 0.8 * L) & (perp < 25)]
        vx, vy, x0, y0 = cv2.fitLine(sel.astype(np.float32), cv2.DIST_HUBER, 0, 0.01, 0.01).ravel()
        lines.append((np.array([x0, y0]), np.array([vx, vy])))
    corners = []
    for i in range(4):
        (a0, ad), (b0, bd) = lines[i - 1], lines[i]
        A = np.array([ad, -bd]).T; s = np.linalg.solve(A, b0 - a0)
        corners.append((a0 + s[0] * ad).tolist())
    # ordenar TL, TR, BR, BL
    cs = np.array(corners); cen = cs.mean(0)
    ang = np.arctan2(cs[:, 1] - cen[1], cs[:, 0] - cen[0])
    cs = cs[np.argsort(ang)]            # empieza en el angulo mas negativo = arriba-izq aprox
    # rotar para que el primero sea el de menor x+y
    k = int(np.argmin(cs.sum(1))); cs = np.roll(cs, -k, 0)
    quads[name] = {'size': [im.shape[1], im.shape[0]], 'quad': cs.round(1).tolist()}
    dbg = cv2.imread(SRC + name + '.png')
    cv2.polylines(dbg, [cs.astype(np.int32)], True, (0, 0, 255), 4)
    cv2.imwrite(OUT + 'dbg_' + name + '.jpg', cv2.resize(dbg, (400, 712)))
    print(name, quads[name])
json.dump(quads, open(OUT + 'quads.json', 'w'), indent=1)
