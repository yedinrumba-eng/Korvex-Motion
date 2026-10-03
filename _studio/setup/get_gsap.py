"""Baja GSAP 3.15.0 desde npm y deja los archivos en _studio/lib/.

GSAP no viene en este repo: tiene su propia licencia ("Standard No Charge", https://gsap.com/community/standard-license/),
que permite usarlo gratis, también en trabajos comerciales, pero no es open source.
Al correr esto aceptas esa licencia.

Uso (desde la carpeta del repo):
  python _studio/setup/get_gsap.py

Verifica el SHA-256 de cada archivo: con la misma versión, los renders salen idénticos.
"""
import hashlib, io, pathlib, sys, tarfile, urllib.request

VERSION = '3.15.0'
URL = f'https://registry.npmjs.org/gsap/-/gsap-{VERSION}.tgz'
FILES = {
    'gsap.min.js': '92bb9a96476f983d212a2bc4f54c889039c1696dd4461d40a736860938570fbb',
    'CustomBounce.min.js': 'e6c138934bbf4c25a0bfdba616aa6114da2641f86c9ee1fffdbf6b6f57ff0608',
    'CustomEase.min.js': '466e426a5c60c21c94b15a30a3dffacac9bb39ce8f4e07d071d7d4bb1be43390',
    'CustomWiggle.min.js': '606fa03b6e37dbf4d12c3237a1967c3ed9a016bbd1ac600bbe6621673c7935d6',
    'DrawSVGPlugin.min.js': 'beb19529f54c1212f1f5117d027be01afda2f363a4926d32aa979bc11140edc1',
    'EasePack.min.js': '2505b29f402a33a0978836bf9a640f86505b1cc542f91a1fe733d9437ad123c8',
    'Flip.min.js': 'cbe3ca726350f8d230da38a14ce2384e7772e05a45cee6144dd7fe6dde868c2f',
    'MorphSVGPlugin.min.js': '19c891a412240d8521b13330813d9b551ea5b0f707907c365ffecaf1dfa0f5cf',
    'MotionPathPlugin.min.js': 'ace44a07c6c179f5347d9b46a152d468e4c9f272ee0d68bf0354e00d60000693',
    'Physics2DPlugin.min.js': 'f41d23011f0b89a66db8dc79aa32e564e82884276ca00b97326130974f5167b9',
    'PhysicsPropsPlugin.min.js': '446bd441ecc582da76af13c878e71e4927e52bda189569063dda89721312cc08',
    'SplitText.min.js': '419f7027a5f086a12cb7988736d8fdd3a6ed2200229661de25b6628ca7ced344',
    'TextPlugin.min.js': 'a24984fa1a33517b4c54c8b25b0bfd7aaf3df9fa7edba661e3bd496a671a2429',
}
LIB = pathlib.Path(__file__).resolve().parent.parent / 'lib'


def main():
    faltan = [n for n, h in FILES.items() if not (LIB / n).exists() or hashlib.sha256((LIB / n).read_bytes()).hexdigest() != h]
    if not faltan:
        print(f'GSAP {VERSION} ya está en {LIB}')
        return 0
    print(f'Bajando GSAP {VERSION} de npm…')
    data = urllib.request.urlopen(URL, timeout=60).read()
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as tar:
        for n in faltan:
            b = tar.extractfile(f'package/dist/{n}').read()
            if hashlib.sha256(b).hexdigest() != FILES[n]:
                print(f'ERROR: {n} no coincide con el SHA-256 esperado', file=sys.stderr)
                return 1
            (LIB / n).write_bytes(b)
            print('  ok', n)
    print('Listo. Licencia de GSAP: https://gsap.com/community/standard-license/')
    return 0


if __name__ == '__main__':
    sys.exit(main())
