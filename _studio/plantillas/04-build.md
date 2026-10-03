---
cliente: {{CLIENTE}}
video: {{VIDEO}}
version_guion: 1
vuelta: 1                      # vueltas con el Juez (máx. 2)
estado: construyendo        # construyendo | listo-para-juez | cambios-juez | listo-para-yeyow | aprobado | entregado
qa:             # salida de qa.py
juez:                 # APROBADO | CAMBIOS | RECHAZADO
maquina_render:    # ej.: "PC Yeyow (Windows)"
---

## 1. Escenas construidas (del beat sheet)
| # · nombre | t guion | t real | Estado | Nota |
|---|---|---|---|---|

## 1b. Costuras
| t | Sale (eje, signo, id) | Entra (eje, signo, id) | Técnica |
|---|---|---|---|

## 2. Desviaciones del guion
| Beat | Qué cambió | Por qué | ¿Vuelve al Guionista? |
|---|---|---|---|

## 3. Comandos para reproducir
```bash
…
```

## 4. QA (qa/report.json)
- Duración … s · 1080×1920 · … MB · quietos … % · cortes … · CV … · pops … · … LUFS / … dBTP · texto fuera de zona: …
- WARN justificados: …
- Hojas: qa/contacto.png · qa/transiciones.png · qa/stills-beats.png · qa/stills-trans.png

## 5. Línea de verdad (verificada en el video)
- Real: … · EJEMPLO: … · Etiquetas presentes en t=…

## 6. Veredicto del Juez (lo escribe el Juez)
### Vuelta 1 — dd/mm
| # | Sev | t | Criterio | Problema | Evidencia (conf.) | Sugerencia |
|---|---|---|---|---|---|---|
Veredicto: … · Lo que se arregló: … · Lo que se dejó y por qué: …

## 7. Pendientes / para Yeyow (PUERTA 4)
- Timestamps que vale la pena mirar: …
- Preguntas abiertas: …

## 8. Entrega (tras 05-revision.md APROBADO)
- master.mp4 (… s, … MB) → entregas/…mp4 + .jpg (poster t=…) + share-copy.txt · perfil § Serie actualizado dd/mm
