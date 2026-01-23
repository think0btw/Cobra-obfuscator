#obfuscator
import marshal ,os

path=""

def GetPATH():
    global path
    UseDropFile = input("Do you want to use drop file ? y for yes : ")
    if (UseDropFile == "y") :
        os.startfile(os.getcwd())
        path = input("Glisse un fichier ici : ").strip('"')
        print(path)
    else :
        path = input("Enter a valid .py PATH : ")

    if path.endswith('.py'):
        return path
    else :
        print("This PATH isn't valid")
        GetPATH()

GetPATH()