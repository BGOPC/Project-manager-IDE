from frameworks import *
from langs import *

class Manage:
    def __init__(self,name,lang):
        self.name = name
        self.lang = lang.strip()
    def Run(self):
        lc = getattr(self, f"execute_{self.lang}")
        lc()

    def execute_Rust(self):
        Rust(self.name, self.lang)

    def execute_Python(self):
        Python(self.name, self.lang)
    def execute_JS(self):
        JS(self.name, self.lang)
    def execute_Java(self):
        Java(self.name, self.lang)