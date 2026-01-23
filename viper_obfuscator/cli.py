#cli script
import marshal , os , base64

os.system("")

def purple(text):
    result = ""
    r, g, b = 100, 0, 255
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
⠀⠀⠀⠀⠀⠀⠀⠑⢲⠢⣄⣀⣓⢵⡌⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡈⠀⣸⠄⢸⡭⡷⣌⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⢃⢰⡛⠈⢆⣿⡂⢡⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢘⢮⡿⣡⣜⡼⣳⣽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⡟⠈⠠⢡⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⢡⢏⡀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⠁⣀⢀⡏⠈⢻⡂⣤⣐⣉⣀⣀⣀⠏⠢⠀⠀⠀
⢠⠒⠉⡡⠂⠈⢹⢉⡚⣺⡗⠂⣉⠡⠄⠒⠒⠀⠢⢖⠒⠰⢀⠀⠀
⡇⠀⠀⠳⡊⠐⢺⠄⣐⣋⣗⠉⠀⠀⠀⢀⣀⣀⡀⠀⡇⠀⠀⠱⡀
⠑⢄⠀⠀⠀⠀⠀⢣⠀⠈⢛⠣⢤⡖⠊⠉⠀⠀⣀⠠⠂⠀⠀⢰⠁
⠀⠀⠉⠒⠠⠤⠤⠖⠓⢄⡀⠁⠀⠀⠈⠉⠁⠀⠀⠀⠀⢀⡴⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠒⠒⠀⠀⠀⠒⠒⠒⠉⠁⠀⠀⠀      
               
               
    """

print(purple(ascii_art))

enter = input(purple("Enter the text to convert to base64: "))
encode =base64.b64encode(enter.encode("utf-8"))
print(f"Encoded text: {encode.decode('utf-8')}")
marshalled_code = marshal.dumps(encode)
with open("encoded_script.py", "w") as file:
    file.write("import base64, marshal\n")
    file.write("data = ")
    file.write(repr(marshalled_code))
    file.write("\n")
    file.write("decoded_data = marshal.loads(data)\n")
    file.write("original_text = base64.b64decode(decoded_data).decode('utf-8')\n")
    file.write("print('Decoded text:', original_text)\n")
print("Encoded script saved to 'encoded_script.py'")
