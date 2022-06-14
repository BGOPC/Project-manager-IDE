from Init import *
from langs import *
from base import Manage
name, lang = initialize()
language = Manage(name, lang)
language.Run()
