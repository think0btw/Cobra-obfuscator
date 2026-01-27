#obfuscator
import base64 ,os

def obfuscate(PATH):
    with open(PATH,"r",encoding="utf-8") as f:
        source = f.read()
        #base64
        encode =base64.b64encode(f.encode("utf-8"))
        #xor
        key = b"\x13\x37\x42\x20\x54"
        xor = bytearray()
        for i in range(len(encode)):
            xor.append(encode[i] ^ key[i % len(key)])
    
def compilefile(PATH):
    with open(PATH,"r",encoding="utf-8") as f:
        source = f.read()
    code = compile(source,PATH,'exec')
    return code