import os
import subprocess
from Init import *
from time import sleep
import sys
# from frameworks import *

class Language:
    def __init__(self, name, lang):
        self.name = name
        self.lang = lang

    def Run(self):
        lc = getattr(self, f"execute_{self.lang}")
        lc()

    def execute_Rust(self):
        Rust(self.name, self.lang)

    def execute_Python(self):
        Python(self.name, self.lang)


class Rust(Language):
    def __init__(self, name, lang):
        super().__init__(name, lang)
        print("Rust initialized")
        if exist(name):
            code = subprocess.run(["cargo", "new", name], capture_output=True)
            print(code)
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

    def run(self):
        os.system(f"cd {str(self.name)} "+"&& cargo run")

    def check(self):
        subprocess.run(["cargo", "check"])

    def delete(self):
        os.system(f"cd {self.name}" + " && del *")
        os.system(f"rmdir {self.name}")


class Python(Language):
    def __init__(self, name, lang):
        super().__init__(name, lang)
        print("Python initialized")
        if exist(name):
            os.system(f"mkdir {name} && cd {name} && " + f"echo print('Hello, World')  >> {name.strip()}.py ُُ")
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

    def run(self):
        print("running...\n\n--------------------------")
        subprocess.call(["python", f"{self.name}" + "/" + f"{self.name}.py"])

    def check(self):
        pipe = subprocess.Popen("python " + f"{self.name}" + "/" + f"{self.name}.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=False)
        got_err = False
        while pipe.poll() is None:
            lines = pipe.stderr.readlines()
            if lines != "":
                print("Got error! The error is:\n\n---------------------------")
                print_str = str.join("", lines)
                print(print_str[:-1])
                got_err = True
                break
        if not got_err:
            print("No errors occurred!")

    def delete(self):
        os.system(f"cd {self.name}" + " && del *")
        os.system(f"rmdir {self.name}")
        os.system("del log.txt")
