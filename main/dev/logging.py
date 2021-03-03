# Imports
from json import load as json_load

try: 
   from termcolor import cprint #optional - pip install termcolor
except ImportError: 
   pass

try: 
   from settings import *
except ImportError: 
   from dev.settings import *
except ImportError: 
   from code.dev.settings import *
except ImportError: 
   from main.dev.settings import *
except:
   logging = False
   debug_mode = False

# Functions
def disable():
   logging = False
   debug_mode = False
   return logging, debug_mode

def log(log_type,text=None):
   if logging == True:
      if text == '' or None:
         return
      else:
         while logging == True:
            if log_type in log_type_info:
               log_title = 'INFO'
               log_color = colors.info
            elif log_type in log_type_warn:
               log_title = 'WARN'
               log_color = colors.warn
            elif log_type in log_type_error:
               log_title = 'ERROR'
               log_color = colors.error
            elif log_type in log_type_console:
               log_title = 'APP'
               log_color = colors.app
            elif log_type in log_type_dev:
               if debug_mode == True:
                  log_title = 'DEV'
                  log_color = colors.dev
               else: 
                  return
            else:
               try:
                  print(str(colors.dev) + '[DEV]: Logging Error ' + ' - ' + str(text))
               except: 
                  disable()
            try: 
               print(str(log_color)+'['+str(log_title)+']: ' + str(text) + '\033[0m')
            except: 
               disable()
            return
         return
   else:
      if debug_mode == True:
         print('[DEV]: Logging is disabled')

class colors:
   error = '\033[91m'
   warn = '\033[93m'
   info = '\033[37m'
   app = '\033[34m'
   dev = '\033[35m'

# log(-1,'-1')
# log(0,'0')
# log(1,'1')
# log(2,'2')
# log(3,'3')
