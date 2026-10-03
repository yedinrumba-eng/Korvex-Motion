# Componentes de terceros

| Componente | Dónde | Licencia | Notas |
|---|---|---|---|
| **GSAP 3.15.0** (núcleo + SplitText, DrawSVG, MorphSVG, MotionPath, CustomEase, Flip, Physics2D, etc.) | **No incluido.** `python _studio/setup/get_gsap.py` lo baja de npm a `_studio/lib/` y verifica el SHA-256 | GSAP Standard "No Charge" License (GreenSock / Webflow), https://gsap.com/community/standard-license/ | Gratis, también para uso comercial, pero no es open source. Entre otras cosas, no permite usar GSAP para crear herramientas que compitan con Webflow como constructor visual de animaciones. Al bajarlo aceptas su licencia. |
| **SFX de Kenney** (casino, impact, interface, keyboard, ui) | `_studio/sfx/` | CC0 1.0 (dominio público), https://kenney.nl | Ver `_studio/sfx/LICENSE-Kenney-CC0.txt`. |
| **Inter**, **JetBrains Mono**, **Michroma** (archivos woff2 de Fontsource) | `_studio/fonts/` | SIL Open Font License 1.1 | El texto de cada licencia está junto a las fuentes (`OFL-*.txt`). |
| **lottie-web** (reproductor SVG) | `_studio/lib/lottie_svg.min.js` | MIT (Bodymovin / Airbnb) | `_studio/lib/LICENSE-lottie.txt`. |
| **Motion** (motion.dev) | `_studio/lib/motion.js` | MIT (Motion B.V.) | `_studio/lib/LICENSE-motion.txt`. |
| **/brag** (latent-spaces/brag): referencias de tonos, audio y pasos | `_studio/refs/brag/` | MIT | `_studio/refs/brag/LICENSE-brag-MIT.txt`. |

**Ideas tomadas, no código:** el método reescribe ideas de HyperFrames (Apache-2.0), gsap-skills, emilkowalski/skills, lottiefiles/motion-design-skill, iart-ai/motion-skills (MIT) y otros. La lista completa, con su licencia, está en `_studio/metodo/00-RESUMEN.md` y en la sección "Fuentes" de cada `rol-*.md`.

**Referencias del radar:** `_studio/refs/tendencias.md` resume y cita artículos y prompts públicos con URL y fecha, sin copiar su contenido. Los prompts del repo yihui-dev/awesome-opus5-5-videos (MIT) son de sus autores y se usan como idea.
