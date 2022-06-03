import os


def initialize():
    if not (os.path.exists("log.txt")):
        print("""Languages name format is like this:
        Python except of py or python or Py or ...,
        Kotlin except of kt or kotlin of Kt or ...
        Java except of Jv or java or ...,
        Rust except of rs or rust or Rs or ...,
        Cpp except of c++ or cpluspls or c plus plus or ...,
        """)
        name = input("name of project:  ")
        lang = input("Language of project:  ")
        with open("log.txt", "a+") as file:
            file.write(f"""project_name = {name}\nproject_language = {lang} \n now""")
    else:
        if str(open("log.txt").read()) != "":
            file = str(open("log.txt").read()).replace("project_", '').replace('\n', '=').split("=")
            # print(file)
            lang = file[3].strip()
            name = file[1].strip()
        else:
            print("""Languages name format is like this:
        Python except of py or python or Py or ...,
        Kotlin except of kt or kotlin of Kt or ...
        Java except of Jv or java or ...,
        Rust except of rs or rust or Rs or ...,
        Cpp except of c++ or cpluspls or c plus plus or ...,
        """)
            name = input("name of project:  ")
            lang = input("Language of project:  ")
            with open("log.txt", "a+") as file:
                file.write(f"""project_name = {name}\nproject_language = {lang}\n now""")
    return name, lang


def exist(name):
    if not os.path.exists("log.txt"):
        return True
    else:
        return "now" in str(open("log.txt").read())
def mk_old():
    if os.path.exists("log.txt"):
        file = str(open("log.txt").read()).replace("now","old")
        with open("log.txt","w") as f:
            f.write(file)