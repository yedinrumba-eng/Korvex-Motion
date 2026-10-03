# PRODUCTOS: organización por cliente

Índice de todos los clientes y productos del estudio. **Cada cliente es una carpeta, y su `perfil.md` es la fuente de verdad.** Lo que no está en su perfil, en su web/código o en palabras de Yeyow, no se dice en un video.

Este archivo se actualiza cada vez que se da de alta un cliente o se entrega un video (lo hace el Editor en el paso 7 de `/korvex-motion`).

---

## Clientes
| Cliente | Carpeta | Qué es | Fuente del proyecto (solo lectura) | Kit de video | Videos entregados | Pendientes |
|---|---|---|---|---|---|---|
| *(tu primer cliente: `/korvex-motion:nuevo-cliente NOMBRE`)* | `NOMBRE/` | | | | | |

### Reglas de cada cliente (resumen; el detalle está en su perfil)
- **<Cliente>:** lo que nunca se dice (precios, nombres de clientes, claims sin fuente), CTA exacto y etiquetas obligatorias ("DATOS DE DEMOSTRACIÓN", "Imágenes conceptuales").

---

## Cómo se organiza un cliente
```
<CLIENTE>/
  perfil.md          la ficha (secciones abajo); cada dato con su fuente
  marca.js           window.MARCA: colores, fuentes, logos, tagline, CTA, firma
  <x>-kit.css/js     (opcional) piezas de marca para video: sello animable, iconos, intro de marca (R1)
  logos/             logos del cliente y de su casa (anota cuál tiene fondo transparente)
  fonts/             fuentes de la marca, con su licencia
  assets/            fotos, capturas, b-roll; fotos recortadas + quads.json
  videos/NN-nombre/  un video por carpeta (01-research … 05-revision, index.html, music.py, qa/)
  entregas/          <cliente>-NN-nombre.mp4 + .jpg (portada) + share-copy.txt (+ variantes)
```

### Secciones del `perfil.md` (la plantilla está en `_PLANTILLA-PRODUCTO/perfil.md`)
1. **Identidad:** qué es en una frase, para quién, qué lo diferencia, casa y firma.
2. **Funciones o servicios reales:** lo que se puede mostrar, con el texto exacto de pantalla si hay UI.
3. **Lo que NO se dice:** precios, clientes, claims sin confirmar, temas legales, datos personales.
4. **Público y categorías:** audiencias por segmento y las categorías de video prioritarias (de `_studio/metodo/categorias.md`).
5. **Marca:** colores, tipografías, logos, tagline, CTA y reglas de diseño. Los valores exactos van en `marca.js`.
6. **Cómo se ve en pantalla:** la UI real que se reproduce (app, web, WhatsApp, panel).
7. **Assets:** inventario con origen y licencia y la etiqueta obligatoria ("Imágenes conceptuales"); lo que NO se usa.
8. **Fuentes del proyecto:** rutas de código, docs, web y redes (solo lectura).
9. **Copy aprobado:** líneas reales que se pueden citar; testimonios tal cual, con su autor; captions aprobados.
10. **Serie de videos:** tabla #, video, categoría, estado y carpeta, y debajo la tabla **Huella** (receta, mecánica, técnica firma, transiciones y gancho de cada video: el registro del look).
11. **Intro de marca y kit:** cómo abre cada video (R1) y qué piezas tiene su kit.
12. **Pendiente — preguntar a Yeyow:** lo que falta confirmar.

### Alta de un cliente nuevo
- **En Claude Code:** `/korvex-motion:nuevo-cliente NOMBRE [ruta o web del proyecto]`.
- **A mano:**
  1. `python _studio/tools/nuevo_producto.py NOMBRE`
  2. Llena `perfil.md` y `marca.js` con datos con fuente.
  3. Pon los logos, las fuentes y los assets.
  4. Si hace falta, crea `<nombre>-kit.css/js` con su intro de marca.
  5. Agrega una fila a la tabla de arriba.

### Convenciones
- **Carpeta:** MAYÚSCULAS con guiones (`PANADERIA-EJEMPLO`).
- **Video:** `NN-nombre-corto` (`04-pan-de-boda`).
- **Entrega:** `<cliente>-NN-nombre.mp4` (`panaderia-04-pan-de-boda.mp4`).
- **Fechas:** dd/mm/aaaa en los documentos y AAAA-MM-DD en el frontmatter.
- **Copy:** español de RD, de tú.
