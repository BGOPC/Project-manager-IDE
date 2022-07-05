from cmath import e, pi
import json
import os
import subprocess
import sys
from time import sleep

from rich import print as rp

from frameworks import *
from Init import *
PATH = os.path.dirname(__file__)
SCRIPTS = os.path.join(PATH, 'scripts')

class Rust(object):
    def __init__(self, name, lang):
        rp("[red italic] Use 'quit' to exit the program [/ red  italic]")
        self.name = name
        self.lang = lang.strip()
        rp("[blue italic bold] Rust initialized [/ blue italic bold]")
        if exist(name):
            code = subprocess.run([f"{sudo} cargo", "new", name], capture_output=True)
            mk_old()
        sleep(1.5)
        self.listen()

    def listen(self):
        rp(" [ spring_green2 italic ] 'run' for run the code\n'check' for check the code \n'delete' to delete all of project [/ spring_green2 italic ] ")
        while True:
            cmd = input("Command !#>  ")
            function = getattr(self, cmd, None)
            if function is not None:
                function()
            else:
                rp(f"[bright_red italic] {cmd} does not exist [/ bright_red italic]")
    def quit(self):
        exit(1)

    def run(self):
        os.system(f"cd {str(self.name)} "+"&& cargo run")

    def check(self):
        os.system(f" cd {str(self.name)} && cargo check")
        # subprocess.run([f"cd {self.name}"," && ","cargo", "check"])

    def delete(self):
        os.system(f"cd {self.name} && {sudo} cargo clean")
        os.system(f"cd {self.name}/src"+ f" && {sudo} rm *")
        os.system(f"cd {self.name}"+f" && {sudo} rmdir src"+" && {sudo} rm *")
        rp("[ cyan italic ] Folder Cleared [/ cyan italic ]")
        rp("[ cyan italic ] Deleting log [/ cyan italic ]")
        os.system("{sudo} rm data.txt")
        if sudo != "":
            os.system(f"{sudo} rmdir {self.name}")
        rp("[ cyan italic ] deleted [/ cyan italic ] ")
        if sudo == "":
            rp(" [ bright_red italic ] I can't delete your folder because it's connected to git\ndyou can delete it on your own [/ bright_red italic ]")
        s = input("Do you want a new project? (N/Y)")
        if s == "Y":
            initialize()
        else:
            exit(1)
    def clear(self):
        os.system(clear)



class Python(object):
    def __init__(self, name, lang):
        rp("[red italic] Use 'quit' to exit the program [/ red italic]")
        self.name = name
        self.lang = lang.strip()
        rp(" [blue italic ] Python initialized  [/blue italic ]")
        if exist(name):
            os.system(f"mkdir {name} && cd {name} && " + f"echo print('Hello, World')  >> {name.strip()}.py ")
            mk_old()
        self.listen()

    def listen(self):
        rp(" [spring_green2 italic ]'run' for run the code\n'check' for check the code \n'delete' to delete all of project\n'ip' to install package [/spring_green2 italic ] ")
        while True:
            cmd = input("Command !#>  ")
            function = getattr(self, cmd, None)
            if function is not None:
                function()
                if cmd != "delete":
                    rp(" [ bold ] ---------------------------\n [/ bold ]")
            else:
                rp(f"[bright_red italic] {cmd} does not exist [/ bright_red italic]")
    def quit(self):
        exit(1)
    def ip(self,ver=None, name=None):
        if not name:
            name = input("name of package:  ")
            ver = input("version of package(latest is default):  ")
        if ver in ("","\n",None):
            os.system(f"{sudo} {pip} install {name}")
        else:os.system(f"{sudo} {pip} install {name}=={ver}")
        # os.system(f"rm 1")

    def run(self):
        rp(" [ bold ] running...\n\n-------------------------- [/ bold ]")
        subprocess.call([Py, f"{self.name}" + "/" + f"{self.name}.py"])

    def check(self):
        pipe = subprocess.Popen(f"{Py} " + f"{self.name}" + "/" + f"{self.name}.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=False)
        got_err = False
        while pipe.poll() is None:
            lines = pipe.stderr.readlines()
            if Errcheck(lines,self.lang):
                if "warn" in lines:
                    rp(" [bold] Got Warning! The Warn is:\n\n--------------------------- [bold] ")
                    print_str = str.join("", lines)
                    print(print_str[:-1])
                    got_err = False
                    break;
                else:
                    rp(" [bold] Got error! The error is:\n\n--------------------------- [bold] ")
                    print_str = str.join("", lines)
                    print(print_str[:-1])
                    got_err = True
                    break;
        if not got_err:
            rp(" [bold] No errors occurred! [bold]")

    def delete(self):
        os.system(f"cd {self.name} && {sudo} rm *")
        os.system(f"{sudo} rmdir {self.name}")
        os.system(f"{sudo} rm data.txt")
        s = input("Do you want a new project? (N/Y)")
        if s.lower() == "y":
            initialize()
        else:
            exit(1)

    def clear(self):
        os.system(clear)



class JS(object):
    def __init__(self, name, lang):
        rp("[red italic] Use 'quit' to exit the program [/ red italic]")
        self.name = name

        self.lang = lang.strip()
        rp(" [blue italic ] Node.JS initialized  [/blue italic ]")
        if exist(self.name):
            code = os.system(f" {sudo} mkdir {self.name} && cd {self.name} && npm init")
            mk_old()
        self.data = json.load(open(f"{self.name}/package.json","r"))
        self.main = self.data["main"]
        self.data["main"] = "src"+self.main
        json.dump(self.data,open(f"{self.name}/package.json","w"))
        if not (os.path.exists(f"{self.name}/src")):
            os.system(f"cd {self.name} && mkdir src && echo console.log('Hello, World') >> src/{self.main}")
        rp(" [italic spring_green1] please add your commands like run or start in package.json or use the 'add' command to add a pkg [/italic spring_green1]")
        self.add(name="run",usage=f"node src/{self.main}")
        sleep(1.5)
        if not self.data.get('pk',False):
            if input("Do You Wanna Install a Package? (Y/N)").lower() == "y":
                self.ip() # install node packages
            self.data["pk"] = True
            json.dump(self.data,open(f"{self.name}/package.json","w"))
        self.listen()



    def listen(self):
        rp(" [spring_green2 italic ] 'run' for run the code\n'check' for check the code \n'delete' to delete all of project\n'ip' to install package and 'add' to add a pkg [/spring_green2 italic ]")
        while True:
            cmd = input("Command !#>  ")
            function = getattr(self, cmd, None)
            if function is not None:
                function()
            else:
                rp(f"[bright_red italic] {cmd} does not exist [/ bright_red italic]")



    def ip(self):
        pkg = input("Your package name or version #>  ").strip()
        version = input("version( default : latest) #>").strip() or None
        if not(version in ("","\n",None)):
            os.system(f"cd {self.name} && {sudo} npm i {pkg}@{version}")
        else:
            os.system(f"cd {self.name} && {sudo} npm i {pkg}")


    def add(self,name=None,usage=None):
        if name == None:
            name = input("name #> ").strip()
        if usage == None:
            usage = input("usage #> ").strip()
        self.data["scripts"][str(name)] = str(usage)
        json.dump(self.data,open(f"{self.name}/package.json","w"))



    def quit(self):
        exit(1)


    def run(self):
        os.system(f"cd {self.name} && npm run")


    def delete(self):
        os.system(f"cd {self.name}/src && {sudo} rm *")
        os.system(f"cd {self.name} && {sudo} rmdir src && {sudo} rm *")
        os.system(f"{sudo} rmdir {self.name}")
        os.system(f"{sudo} rm data.txt")
        s = input("Do you want a new project? (N/Y)")
        if s.lower() == "y":
            initialize()
        else:
            exit(1)

    def check(self):
        pipe = subprocess.Popen(f"cd {self.name} && npm run", stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=False)
        got_err = False
        while pipe.poll() is None:
            lines = pipe.stderr.readlines()
            if Errcheck(lines,self.lang):
                if "warn" in lines:
                    rp(" [bold] Warning error! The error is:\n\n--------------------------- [bold] ")
                    print_str = str.join("", lines)
                    print(print_str[:-1])
                    got_err = False
                    break;
                else:
                    rp(" [bold] Got error! The error is:\n\n--------------------------- [bold] ")
                    rp(" [bold] Warning error! The error is:\n\n--------------------------- [bold] ")
                    print_str = str.join("", lines)
                    print(print_str[:-1])
                    got_err = True
                    break;

        if not got_err:
            rp(" [bold] No errors occurred! [bold]")



class Java(object):
    def __init__(self, name, lang):
        rp("[red italic] Use 'quit' to exit the program [/ red italic]")
        self.name = name
        self.main = "Main"
        self.despath = f"./{self.name}/debug/"
        self.lang = lang.strip()
        if not os.path.exists(self.main):
            self.pkg = True if input("Package or No? (Y/N)").lower() == "y" else False
            with open("data.txt","a+") as f:
                f.write(f"\n{self.pkg}")
        else:
            self.pkg = False if "False" in (open("data.txt").read()) else True
        # print(self.pkg)
        rp(" [blue italic ] Java initialized  [/blue italic ]")
        def content(self):
            ipkg = f"package src;" + "\n\n"  if self.pkg else ""
            file = ipkg + open(f"{SCRIPTS}/langs/Main.java","r").read()
            with open(f"{self.name}/src/Main.java", "w") as java:
                java.write(str(file))
        if exist(self.name):
            os.system(f"mkdir {self.name} && cd {self.name} && mkdir ./src")
            content(self)
            mk_old()
        if not (os.path.exists(f"{self.name}/src")):
            os.system(f"cd {self.name}&& cd {self.name} && mkdir src && cd src && {copy} {SCRIPTS}/langs/Main.java src")
        sleep(1.5)
        self.listen()




    def listen(self):
        rp(" [spring_green2 italic ] 'run' for run the code\n'check' for check the code \n'delete' to delete all of project\nand 'Build' to make an executable file [/spring_green2 italic ]")
        while True:
            cmd = input("Command !#>  ")
            function = getattr(self, cmd, None)
            if function is not None:
                function()
            else:
                rp(f"[bright_red italic] {cmd} does not exist [/ bright_red italic]")
    def run(self):
        if self.pkg:
            print("pkg")
            os.system(f"cd ./{self.name} && javac ./src/{self.main}.java -d out")
            os.system(f"cd ./{self.name}/out && java ./src.{self.main}")
        else:
            os.system(f"cd ./{self.name}/src && java ./{self.main}.java")
    def chmain(self):
        st = True if input("Are You Sure You Wanna Change The Main File Name? (Y/N)").lower() == 'y' else False
        if st:
            self.main = (nm:=input(f"Name Of File !#> ({self.main})")) if nm != self.main else self.main
        print("Done")


    def check(self):
        os.system(f"ls ./{self.name}/src")
        os.system(f"cd ./{self.name} && javac ./src/{self.main}.java")
        run = f"cd {self.name} && java src.{self.main}" if self.pkg else "java src/{self.main}"
        pipe = subprocess.Popen(f"javac ./{self.name}/src/{self.main}.java -d out && cd ./{self.name}/out && {run}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=False)
        got_err = False
        while pipe.poll() is None:
            lines = pipe.stderr.readlines()
            if Errcheck(lines,self.lang):
                if "warn" in lines or "Warning" in lines or "warning" in lines:
                    rp(" [bold] Warning error! The error is:\n\n--------------------------- [bold] ")
                    print_str = str.join("", lines)
                    print(print_str[:-1])
                    got_err = False
                    break;
                else:
                    rp(" [bold] Got error! The error is:\n\n--------------------------- [bold] ")
                    rp(" [bold] Warning error! The error is:\n\n--------------------------- [bold] ")
                    print_str = str.join("", lines)
                    print(print_str[:-1])
                    got_err = True
                    break;

        if not got_err:
            rp(" [bold] No errors occurred! [bold]")
    def delete(self):
        os.system(f"cd {self.name} && "+delall)
        os.system(f"rmdir {self.name}")
        os.system(f"rm data.txt")
        s = input("Do you want a new project? (N/Y)")
        if s.lower() == "y":
            initialize()
        else:
            exit(1)

    def quit(self):
        exit(0)
