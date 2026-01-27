#obfuscator
import base64 ,os

def obfuscate(PATH):
    with open(PATH, "r", encoding="utf-8") as f:
        source = f.read()

    # base64
    encoded = base64.b64encode(source.encode("utf-8"))

    # xor
    key = b"\x13\x37\x42\x20\x54"
    xor = bytearray()

    for i in range(len(encoded)):
        xor.append(encoded[i] ^ key[i % len(key)])

    return xor

def compilefile(PATH):
    with open(PATH, "r", encoding="utf-8") as f:
        source = f.read()
    code = compile(source,PATH,'exec')
    return code