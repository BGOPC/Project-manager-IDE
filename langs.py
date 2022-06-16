import os
import subprocess
from Init import *
from time import sleep
import sys
from frameworks import *
class Rust(object):
    def __init__(self, name, lang):
        self.name = name
        self.lang = lang.strip()
        print("Rust initialized")
        if exist(name):
            code = subprocess.run([f"{sudo} cargo", "new", name], capture_output=True)
            # print(code)
            mk_old()
        sleep(1.5)
        self.listen()

    def listen(self):
        print("run for run the code\ncheck for check the code \ndelete to delete all of project")
        while True:
            cmd = input("Command !#>  ")
            function = getattr(self, cmd, None)
            if function is not None:
                function()
            else:
                print("Command is not exist")
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
        print("Folder Cleared")
        print("Deleting log")
        os.system("{sudo} rm log.txt")
        if sudo != "":
            os.system(f"{sudo} rmdir {self.name}")
        print("deleted")
        if sudo == "":
            print("I can't delete your folder because it's connected to git\ndyou can delete it on your own")
        s = input("Do you want a new project? (N/Y)")
        if s == "Y":
            initialize()
        else:
            exit(1)
    def clear(self):
        os.system(clear)



class Python(object):
    def __init__(self, name, lang):
        self.name = name
        self.lang = lang.strip()
        print("Python initialized")
        if exist(name):
            os.system(f"mkdir {name} && cd {name} && " + f"echo print('Hello, World')  >> {name.strip()}.py ")
            mk_old()
        self.listen()

    def listen(self):
        print("run for run the code\ncheck for check the code \ndelete to delete all of project")
        while True:
            cmd = input("Command !#>  ")
            function = getattr(self, cmd, None)
            if function is not None:
                function()
                if cmd != "delete":
                    print("---------------------------\n")
            else:
                print(f"{cmd} doesn't not exist")
    def quit(self):
        exit(1)

    def run(self):
        print("running...\n\n--------------------------")
        subprocess.call([Py, f"{self.name}" + "/" + f"{self.name}.py"])

    def check(self):
        pipe = subprocess.Popen(f"{Py} " + f"{self.name}" + "/" + f"{self.name}.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=False)
        got_err = False
        while pipe.poll() is None:
            lines = pipe.stderr.readlines()
            if Errcheck(lines,self.lang):
                print("Got error! The error is:\n\n---------------------------")
                print_str = str.join("", lines)
                print(print_str[:-1])
                got_err = True
                break;
        if not got_err:
            print("No errors occurred!")

    def delete(self):
        os.system(f"cd {self.name}" + " && {sudo} rm *")
        os.system(f"{sudo} rmdir {self.name}")
        os.system("{sudo} rm log.txt")
        s = input("Do you want a new project? (N/Y)")
        if s.lower() == "y":
            initialize()
        else:
            exit(1)

    def clear(self):
        os.system(clear)



class JS(object):
    def __init__(self, name, lang):
        self.name = name
        self.lang = lang.strip()
        print("node initialized")
        if exist(name):
            code = os.system(f" {sudo} mkdir {name} && cd {name} && npm init")
            # print(code)
            mk_old()
        print("please add your commands like run or start in package.json or use the 'add' command to add a pkg")
        sleep(1.5)
        self.ip() # install node packages
        self.listen()
    def listen(self):
        print("run for run the code\ncheck for check the code \ndelete to delete all of project")
        while True:
            cmd = input("Command !#>  ")
            function = getattr(self, cmd, None)
            if function is not None:
                function()
            else:
                print("Command is not exist")
    def ip(self):
        pkg = input("Your package name or version #>  ").strip()
        version = input("version( default : latest) #>").strip() or None
        if not(version == "" or version == "\n"):
            os.system(f"cd {self.name} && {sudo} npm i {pkg}@{version}")
        else:
            os.system(f"cd {self.name} && {sudo} npm i {pkg}")
    def add(self,name=None,usage=None):
        if name == None:
            name = input("name #> ").strip()
        if usage == None:
            usage = input("usage #> ").strip()
        import json
        with open(f"{self.name}/packages.json", "w+") as f:
            data = json.load(f)
        #TODO: write a code to add a script to package.json
    def quit(self):
        exit(1)
    def run(self):
        pass
        #TODO: write a code to run a node module
