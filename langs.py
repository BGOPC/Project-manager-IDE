import json
import os
import subprocess
import sys
from time import sleep

from rich import print as rp

from frameworks import *
from Init import *


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
        rp(" [ bright_green italic ] 'run' for run the code\n'check' for check the code \n'delete' to delete all of project [/ bright_green italic ] ")
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
        os.system(f"cd {self.name}/src"+ " && {sudo} rm *")
        os.system(f"cd {self.name}"+f" && {sudo} rmdir src"+" && {sudo} rm *")
        rp("[ cyan italic ] Folder Cleared [/ cyan italic ]")
        rp("[ cyan italic ] Deleting log [/ cyan italic ]")
        os.system("{sudo} rm log.txt")
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
        rp(" [bright_green italic ]'run' for run the code\n'check' for check the code \n'delete' to delete all of project\n'ip' to install package [/bright_green italic ] ")
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
        os.system(f"{sudo} rm log.txt")
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
        rp(" [ blue italic ] Node.JS initialized  [/ blue italic ]")
        if exist(self.name):
            code = os.system(f" {sudo} mkdir {self.name} && cd {self.name} && npm init")
            mk_old()
        self.data = json.load(open(f"{self.name}/package.json","r"))
        self.main = self.data["main"]
        self.data["main"] = "src"+self.main
        json.dump(self.data,open(f"{self.name}/package.json","w"))
        os.system(f"cd {self.name} && mkdir src && echo console.log('Hello, World') >> src/{self.main}")
        rp(" [] please add your commands like run or start in package.json or use the 'add' command to add a pkg")
        self.add(name="run",usage=f"node src/{self.main}")
        sleep(1.5)
        if input("Do You Wanna Install a Package? (Y/N)").lower() == "y":
            self.ip() # install node packages
        self.listen()



    def listen(self):
        rp(" [ bright_green italic ] 'run' for run the code\n'check' for check the code \n'delete' to delete all of project\n'ip' to install package and 'add' to add a pkg [/ bright_green italic ]")
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
        os.system(f"{sudo} rm log.txt")
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
