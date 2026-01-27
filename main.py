import os
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


def ast_obfuscate_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            source = f.read()

        engine = ObfuscationEngine(strings=True, numbers=True, passes=2)
        obfuscated_code = engine.obfuscate(source)

        out_path = path.replace(".py", "_obf.py")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(obfuscated_code)

        print(color(f"[+] Obfuscation finished → {out_path}"))

    except Exception as e:
        print(color(f"[ERROR] {e}"))


def drag_file():
    path = input("Glisse un fichier ici : ").strip().strip('"').strip("'")

    if path.lower().endswith(".py") and os.path.isfile(path):
        print(color(f"[+] File loaded : {path}"))
        ast_obfuscate_file(path)
    else:
        print(color("[-] Not a python file"))


def manualpath():
    path = input("Enter the file path : ").strip().strip('"').strip("'")

    if path.lower().endswith(".py") and os.path.isfile(path):
        print(color(f"[+] File loaded : {path}"))
        ast_obfuscate_file(path)
    else:
        print(color("[-] Not a python file"))


def help_menu():
    print(color("""
    help        : show this help
    drag        : drag and drop a python file (auto obfuscate)
    manualpath  : manually enter a python file path
    clear       : clear the screen
    path        : show current directory
    exit        : exit the program
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
    elif cmd == "exit":
        break
    else:
        print(color("Unknown command. Type help"))
