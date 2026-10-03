# Korvex Motion - instalacion y verificacion en Windows
# Uso (PowerShell, desde la carpeta del repo):
#   powershell -ExecutionPolicy Bypass -File "_studio\setup\instalar-windows.ps1"
# Instala lo que falte (Python, ffmpeg, paquetes, Chromium de Playwright) y prueba el estudio.
# Nota: escrito para Windows 10/11 con winget. No se pudo probar desde la nube: si algo falla, copia el error en el chat.

$ErrorActionPreference = "Continue"
function Ok($m)   { Write-Host "  OK  $m" -ForegroundColor Green }
function Warn($m) { Write-Host "  !!  $m" -ForegroundColor Yellow }
function Have($c) { return [bool](Get-Command $c -ErrorAction SilentlyContinue) }

Write-Host "`n== Korvex Motion: requisitos ==" -ForegroundColor Cyan

# 1) Python 3.11+
if (-not (Have "python")) {
  Warn "Python no esta en el PATH. Instalando Python 3.12 con winget..."
  winget install -e --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements
  Warn "Cierra y vuelve a abrir PowerShell y corre este script otra vez."
  exit 1
}
$pv = (python -c "import sys;print('%d.%d'%sys.version_info[:2])")
if ([version]$pv -lt [version]"3.11") { Warn "Python $pv es viejo: instala 3.11+ (winget install Python.Python.3.12)"; exit 1 }
Ok "Python $pv"

# 2) ffmpeg
if (-not (Have "ffmpeg")) {
  Warn "ffmpeg no esta. Instalando con winget (Gyan.FFmpeg)..."
  winget install -e --id Gyan.FFmpeg --accept-package-agreements --accept-source-agreements
  Warn "Cierra y vuelve a abrir PowerShell para que ffmpeg entre al PATH, y corre este script otra vez."
  exit 1
}
Ok ("ffmpeg " + ((ffmpeg -version | Select-Object -First 1) -split ' ')[2])

# 3) Paquetes de Python + Chromium de Playwright
python -m pip install --upgrade pip | Out-Null
python -m pip install playwright numpy opencv-python scipy
python -m playwright install chromium
Ok "paquetes y Chromium de Playwright"

# 3b) GSAP (no viene en el repo: licencia propia de GSAP, gratis tambien para uso comercial)
$root0 = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
python (Join-Path $root0 "_studio\setup\get_gsap.py")
if ($LASTEXITCODE -eq 0) { Ok "GSAP en _studio\lib" } else { Warn "no se pudo bajar GSAP (mira el error arriba)" }

# 4) Node / Claude Code (opcional)
if (Have "node") { Ok ("node " + (node --version)) } else { Warn "Node no esta (solo hace falta para instalar Claude Code: winget install OpenJS.NodeJS.LTS)" }
if (Have "claude") { Ok "Claude Code instalado" } else { Warn "Claude Code no esta: npm install -g @anthropic-ai/claude-code" }

# 5) Prueba del estudio: un cuadro del demo del kit y el candado de puertas
Write-Host "`n== Prueba ==" -ForegroundColor Cyan
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Push-Location (Join-Path $root "_studio\test")
python ..\render.py --html kit-motion.html --frame 40 --png prueba-f40.png --w 1080 --h 1920 --sub 4
if (Test-Path "prueba-f40.png") { Ok "render de prueba: _studio\test\prueba-f40.png" } else { Warn "el render de prueba fallo (mira el error arriba)" }
Pop-Location
$j = '{"tool_name":"Write","tool_input":{"file_path":"X/videos/01-a/index.html"}}'
$j | python (Join-Path $root "_studio\tools\gate_check.py")
if ($LASTEXITCODE -eq 0) { Ok "gate_check.py responde (python funciona para el hook del plugin)" } else { Warn "gate_check.py devolvio $LASTEXITCODE" }

Write-Host "`nListo. Siguiente: abre Claude Code en esta carpeta y corre:" -ForegroundColor Cyan
Write-Host '  /plugin marketplace add yedinrumba-eng/korvex-motion'
Write-Host '  /plugin install korvex-motion@korvex'
