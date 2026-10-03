---
description: Muestra en qué puerta va cada video del flujo korvex-motion (o de un cliente)
argument-hint: [CLIENTE]
---
Muestra el estado del flujo korvex-motion para: `$ARGUMENTS` (si está vacío, todos los clientes de `PRODUCTOS.md`).

Para cada `<CLIENTE>/videos/NN-*/` que tenga `02-brief.md`, lee el frontmatter de 01–05 y arma una tabla con estas columnas:
- video;
- categoría;
- 01 research (estado);
- PUERTA 1 (`aprobado` del brief);
- PUERTA 2 (`aprobado` del guion);
- build/juez (`04-build.md` estado/juez/qa);
- PUERTA 4 (`veredicto_yeyow`);
- entregado (si existe `entregas/<cliente>-NN-*.mp4`).

Los videos viejos (solo `plan.md`) van aparte, como "entregados (flujo anterior)". Termina diciendo cuál es el siguiente paso de cada video abierto.
