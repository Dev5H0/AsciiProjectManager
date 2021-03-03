# Imports
from import_manager import os_system
from config import app_version
from commands import main
try: 
   from main.dev.logging import log, logging
except:
   logging = False
   def log(x=None, y=None):
      pass

#-
os_system('title '+('ASCII Project Manager' + ' - ' + str(app_version)))
main()
