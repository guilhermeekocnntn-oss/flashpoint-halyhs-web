from pathlib import Path
import zlib

root = Path(__file__).resolve().parents[1]
source = root / "game" / "halYHS.swf"
output = root / "tmp" / "halYHS-pt-loader.swf"

raw = source.read_bytes()
if raw[:3] != b"CWS":
    raise SystemExit(f"Formato inesperado: {raw[:3]!r}")

body = zlib.decompress(raw[8:])
old = b"intro.swf"
new = b"intrp.swf"
count = body.count(old)
if count != 1:
    raise SystemExit(f"Esperava 1 referencia a {old!r}, encontrei {count}")

patched = body.replace(old, new)
rebuilt = raw[:8] + zlib.compress(patched, 9)

if zlib.decompress(rebuilt[8:]) != patched:
    raise SystemExit("Falha na verificacao da recompresao")

output.write_bytes(rebuilt)
print(f"Criado: {output}")
print(f"Referencia antiga: {patched.count(old)}")
print(f"Referencia nova: {patched.count(new)}")
print(f"Tamanho declarado: {int.from_bytes(raw[4:8], 'little')}")
print(f"Tamanho descomprimido: {len(patched) + 8}")
