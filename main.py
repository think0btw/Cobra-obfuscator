import os
import base64
from viper_obfuscator.ast import ObfuscationEngine
from viper_obfuscator import obfuscator

def color(text):
    result = ""
    r, g, b = 225, 11, 18
    up = True

    for line in text.splitlines():
        for char in line:
            if up:
                g += 3
                if g >= 180:
                    up = False
            else:
                g -= 2
                if g <= 40:
                    up = True

            result += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
        result += "\n"

    return result


ascii_art = r"""
                                         ⠀⠀⠀⠀⠀⠀⠀⡖⠎⣻⡊⠑⢦⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
               ___      _                ⠀⠀⠀⠀⠀⠀⠀⠑⢲⠢⣄⣀⣓⢵⡌⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀
              / __\___ | |__  _ __ __ _  ⠀⠀⠀⠀⠀⠀⠀⠀⡈⠀⣸⠄⢸⡭⡷⣌⡄⠀⠀⠀⠀⠀⠀⠀⠀
             / /  / _ \| '_ \| '__/ _` | ⠀⠀⠀⠀⠀⠀⠀⢠⢃⢰⡛⠈⢆⣿⡂⢡⠃⠀⠀⠀⠀⠀⠀⠀⠀
            / /__| (_) | |_) | | | (_| | ⠀⠀⠀⠀⠀⠀⠀⢘⢮⡿⣡⣜⡼⣳⣽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
            \____/\___/|_.__/|_|  \__,_| ⠀⠀⠀⠀⠀⠀⠀⠈⡟⠈⠠⢡⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                         ⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⢡⢏⡀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀
            By :                         ⠀⠀⠀⠀⠀⠀⢰⠁⣀⢀⡏⠈⢻⡂⣤⣐⣉⣀⣀⣀⠏⠢⠀⠀⠀
            ~ think0btw                  ⢠⠒⠉⡡⠂⠈⢹⢉⡚⣺⡗⠂⣉⠡⠄⠒⠒⠀⠢⢖⠒⠰⢀⠀⠀
            ~ Nat11-n1                   ⡇⠀⠀⠳⡊⠐⢺⠄⣐⣋⣗⠉⠀⠀⠀⢀⣀⣀⡀⠀⡇⠀⠀⠱⡀
                                         ⠑⢄⠀⠀⠀⠀⠀⢣⠀⠈⢛⠣⢤⡖⠊⠉⠀⠀⣀⠠⠂⠀⠀⢰⠁
                                         ⠀⠀⠉⠒⠠⠤⠤⠖⠓⢄⡀⠁⠀⠀⠈⠉⠁⠀⠀⠀⠀⢀⡴⠃⠀
 use help for help                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠒⠒⠀⠀⠀⠒⠒⠒⠉⠁⠀⠀⠀
"""

print(color(ascii_art))


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def write_loader(out_path, data):
    key = b"\x13\x37\x42\x20\x54"
    loader = f'''
import base64
data = {list(data)}
key = {list(key)}
decoded = bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))
code = base64.b64decode(decoded)
exec(code)
'''
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(loader)


def full_obfuscate(path):
    with open(path, "r", encoding="utf-8") as f:
        source = f.read()

    engine = ObfuscationEngine(strings=True, numbers=True, passes=2)
    ast_code = engine.obfuscate(source)

    tmp = path.replace(".py", "_tmp.py")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ast_code)

    xor_bytes = obfuscator.obfuscate(tmp)
    os.remove(tmp)

    out = path.replace(".py", "_packed.py")
    write_loader(out, xor_bytes)

    print(color(f"[+] {out}"))


def drag_file():
    path = input("Glisse un fichier ici : ").strip().strip('"').strip("'")
    if path.lower().endswith(".py") and os.path.isfile(path):
        full_obfuscate(path)
    else:
        print(color("Not a python file"))


def manualpath():
    path = input("Enter the file path : ").strip().strip('"').strip("'")
    if path.lower().endswith(".py") and os.path.isfile(path):
        full_obfuscate(path)
    else:
        print(color("Not a python file"))


def help_menu():
    print(color("""
help
drag
manualpath
clear
path
exit
"""))


while True:
    cmd = input(color("[>] ")).strip().lower()
    if cmd == "drag":
        drag_file()
    elif cmd == "manualpath":
        manualpath()
    elif cmd == "help":
        help_menu()
    elif cmd == "clear":
        clear()
    elif cmd == "path":
        print(os.getcwd())
    elif cmd == "compile":
        pathtocompile = input("Enter the file path to compile: ")
        obfuscator.compilefile(pathtocompile)
    elif cmd == "exit":
        break
    else:
        print(color("Unknown command"))
