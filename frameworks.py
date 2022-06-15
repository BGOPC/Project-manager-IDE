import os
import subprocess
from Init import *
from time import sleep
import sys
import langs

class frameworks:
    def __init__(self,name,lang,fw):
        self.name = name
        self.lang = lang.strip()
        self.fw = fw.strip()
        print("Frameworks initialized")
        self.build()
    def build(self):
        func = getattr(self,f"{self.lang}_build",None)
        if func: func()
    def Python_build(self):
        py = PyFW(self.name,self.fw)
        py.build_fw()
class PyFW(frameworks):
    def __init__(self,name,fw):
        self.name = name
        self.fw = fw.strip()
    def build_fw(self):
        os.system(f"cd {self.name} && python3 -m venv {self.name}")
        os.system(f"cd {self.name} && '{self.name}/bin/activate'")
        os.system(f"cd {self.name} && pip install {self.fw}")

