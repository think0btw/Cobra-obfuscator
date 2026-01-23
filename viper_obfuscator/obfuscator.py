#obfuscator
import marshal , platform , os

path=""

def GetPATH():
    global path
    path = input("Enter a valid .py PATH :")
    if path.endswith('.py'):
        return path
    else :
        print("This PATH isn't valid")
        GetPATH()