#obfuscator
import marshal ,base64 ,os

def obfuscate(PATH):
    with open(PATH,"r",encoding="utf-8") as f:
        source = f.read()
    

def cimpilefiles(PATH):
    with open(PATH,"r",encoding="utf-8") as f:
        source = f.read()
    code = compile(source,PATH,'exec')
    return code