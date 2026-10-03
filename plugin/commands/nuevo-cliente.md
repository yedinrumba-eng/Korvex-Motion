---
description: Da de alta un cliente o producto nuevo en el estudio (carpeta, perfil, marca) antes de crear su primer video
argument-hint: NOMBRE-DEL-CLIENTE [ruta del proyecto o web de referencia]
---
Cliente nuevo: `$ARGUMENTS`

1. `python _studio/tools/nuevo_producto.py <NOMBRE>` crea `<NOMBRE>/` desde `_PLANTILLA-PRODUCTO` (`perfil.md`, `marca.js`, `logos/`, `assets/`, `videos/`, `entregas/`).
2. Si Yeyow dio una ruta o una web, léela en **solo lectura**: landing, código, docs, marca y FAQ.
3. Llena `perfil.md` sección por sección con datos con fuente:
   - identidad;
   - funciones reales;
   - lo que NO se dice;
   - público;
   - marca;
   - cómo se ve;
   - assets con licencia;
   - fuentes;
   - copy aprobado;
   - categorías prioritarias.

   Llena también `marca.js` (colores, fuentes, logos, tagline, CTA). Lo que no encuentres queda "PENDIENTE — preguntar a Yeyow".
4. Copia logos, fuentes (con su licencia) y assets usables. Nunca fotos personales ni stock sin licencia. Etiqueta lo generado.
5. Haz a Yeyow las preguntas de lo PENDIENTE: ≤4 por ronda, con opciones y la recomendada primero.
6. Si la marca necesita piezas propias (sello, iconos, tipografía), crea `<NOMBRE>/<nombre>-kit.css/js` siguiendo el modelo de las piezas de `_studio/lib/kit.js`. Debe incluir el intro de marca (R1).
7. Agrega el cliente a `PRODUCTOS.md` y a la tabla del `README.md`.
8. Ofrece arrancar el primer video con `/korvex-motion`.
