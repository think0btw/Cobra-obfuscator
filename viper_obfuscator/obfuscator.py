#obfuscator
import marshal ,base64 ,os

def obfuscate(PATH):
    with open(PATH,"r",encoding="utf-8") as f:
        source = f.read()
        encode =base64.b64encode(f.encode("utf-8"))
    marshalled_code = marshal.dumps(encode)
    
    
def compilefile(PATH):
    with open(PATH,"r",encoding="utf-8") as f:
        source = f.read()
    code = compile(source,PATH,'exec')
    return code