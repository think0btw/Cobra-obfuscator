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
 use help for help                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠒⠒⠀⠀⠀⠒⠒⠒⠉⠁⠀⠀⠀  """

print(color(ascii_art))


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def drag_file():
    path = input("Glisse un fichier ici : ").strip().strip('"').strip("'")

    if path.lower().endswith(".py") and os.path.isfile(path):
        print("Path :", path)
    else:
        print("Not a python file")
    return

def mlanualpath():
    path = input("Enter the file path : ")
    if path.lower().endswith(".py") and os.path.isfile(path):
        print("Path :", path)
    else:
        print("Not a python file")
    return

def help():
    print(color("""
    help : show this help
    drag : drag and drop a python file
    clear : clear the screen
    path : show the current path
    manualpath : manually enter a file path
    exit : exit the program
    """))


while True:
    cmd =input(color("[>]  "))
    if cmd =='drag':
        drag_file()
    if cmd =='help':
        help()
    if cmd =='clear':
        clear()
    if cmd =='path':
        print(os.getcwd())
    if cmd =='manualpath':
        mlanualpath()
    if cmd =='exit':
        break









def inutile ():
    enter = input(purple("Enter the text to convert to base64: "))
    encode =base64.b64encode(enter.encode("utf-8"))
    print(purple(f"Encoded text: {encode.decode('utf-8')}"))
    marshalled_code = marshal.dumps(encode)
    with open("encoded_script.py", "w") as file:
        file.write("import base64, marshal\n")
        file.write("data = ")
        file.write(repr(marshalled_code))
        file.write("\n")
        file.write("decoded_data = marshal.loads(data)\n")
        file.write("original_text = base64.b64decode(decoded_data).decode('utf-8')\n")
        file.write("print('Decoded text:', original_text)\n")
    print(purple("Encoded script saved to 'encoded_script.py'"))
    init(autoreset=True)
    print(Style.RESET_ALL)

