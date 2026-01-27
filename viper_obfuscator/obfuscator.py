import base64
import subprocess
import os

def obfuscate(PATH):
    with open(PATH, "r", encoding="utf-8") as f:
        source = f.read()

    encoded = base64.b64encode(source.encode("utf-8"))

    key = b"\x13\x37\x42\x20\x54"
    xor = bytearray(encoded[i] ^ key[i % len(key)] for i in range(len(encoded)))
    return xor


def compilefile(PATH):
    if not os.path.isfile(PATH):
        print("File not found")
        return

    if not PATH.endswith(".py"):
        print("Not a python file")
        return

    try:
        subprocess.run(
            ["python3", "-m", "nuitka", "--onefile", PATH],
            check=True
        )
        print("[+] Compilation finished")
    except subprocess.CalledProcessError:
        print("Compilation failed")
