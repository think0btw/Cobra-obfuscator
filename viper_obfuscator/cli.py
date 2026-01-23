from colorama import init ,Fore , Style
import marshal , os , base64

os.system("")

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
 use --help for help                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠒⠒⠀⠀⠀⠒⠒⠒⠉⠁⠀⠀⠀  
    """

print(color(ascii_art))

def drag_file():
    path = input("Glisse un fichier ici : ").strip().strip('"').strip("'")

    if path.lower().endswith(".py") and os.path.isfile(path):
        print("Path :", path)
    else:
        print("Not a python file")

while True:
    cmd =input(color("[>]  "))
    if cmd =='drag':
        drag_file()

