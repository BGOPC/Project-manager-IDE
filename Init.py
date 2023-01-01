import os
from sys import platform


sudo = ""
Py = "python"
clear = "cls"
pip = "pip"
copy = "copy"
delall = f"powershell.exe -Command rm *"
if platform in ("linux","linux2","darwin") :
    Py = "python3"
    clear = "clear"
    sudo = "sudo"
    pip = "pip3"
    copy = "cp"
    delall = f"rm -rf ./*"

def initialize():
    if not (os.path.exists("data.txt")):
        print("""Languages name format is like this:
        Python except of py or python or Py or ...,
        Kotlin except of kt or kotlin of Kt or ...
        Java except of Jv or java or ...,
        Rust except of rs or rust or Rs or ...,
        Cpp except of c++ or cpluspls or c plus plus or ...,
        JS for JavaScript or js or ...,
        """)
        name = input("name of project:  ")
        lang = input("Language of project:  ")
        with open("data.txt", "a+") as file:
            file.write(f"""project_name = {name}\nproject_language = {lang}\n now""")
    else:
        if str(open("data.txt").read()) != "":
            file = str(open("data.txt").read()).replace("project_", '').replace('\n', '=').split("=")
            # print(file)
            lang = file[3].strip()
            name = file[1].strip()
        else:
            print("""Languages name format is like this:
        Python except of py or python or Py or ...,
        Java except of Jv or java or ...,
        Rust except of rs or rust or Rs or ...,
        JS for JavaScript or js or ...,
        """)
            name = input("name of project:  ")
            lang = input("Language of project:  ")
            with open("data.txt", "a+") as file:
                file.write(f"""project_name = {name}\nproject_language = {lang}\n now""")
    return name, lang


def exist():
    if not os.path.exists("data.txt"):
        return True
    else:
        return "now" in str(open("data.txt").read())
def mk_old():
    if os.path.exists("data.txt"):
        file = str(open("data.txt").read()).replace("now","old")
        with open("data.txt","w") as f:
            f.write(file)

def Errcheck(lines,lang):
    py = ["ZeroDivisionError","ZeroDivisionError",'UnicodeTranslateError',"UnicodeDecodeError","UnicodeEncodeError",
          "UnicodeError","UnboundLocalError","TypeError","SystemExit","SystemError","TabError","IndentationError",
          "SyntaxError","StopIteration","RuntimeError","ReferenceError","OverflowError","OSError","NotImplementedError",
          "NameError","MemoryError","KeyboardInterrupt","KeyError","IndexError","ImportError","GeneratorExit","FloatingPointError",
          "EOFError","AttributeError","AssertionError","BaseException","Exception","Error"]


    js = ["Error","InternalError","RangeError",
    "ReferenceError","SyntaxError","TypeError",
    "URIError","Warning"]

    java = ["Exception","BaseException","error"]


    langs = {"Python":py,"JS":js,"Java":java}
    NE = langs[str(lang)]
    # print(NE)
    for i in NE:
        if i in str(lines):
            return True
    return False