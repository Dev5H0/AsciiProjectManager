# Imports
from json import load as json_load

try: 
   from termcolor import cprint #optional - pip install termcolor
except ImportError: 
   pass

try: 
   from main.dev.settings import *
except ImportError:
   from dev.settings import *
except ImportError: 
   from settings import *
except ImportError: 
   from code.dev.settings import *
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
               log_type = 'info'
               log_title = 'INFO'
               log_color = 'white'
            elif log_type in log_type_warn:
               log_type = 'warn'
               log_title = 'WARN'
               log_color = 'yellow'
            elif log_type in log_type_error:
               log_type = 'error'
               log_title = 'ERROR'
               log_color = 'red'
            elif log_type in log_type_console:
               log_type = 'console'
               log_title = 'APP'
               log_color = 'blue'
            elif log_type in log_type_debug:
               if debug_mode == True:
                  log_type = 'debug'
                  log_title = 'DEBUG'
                  log_color = 'magenta'
            else:
               try: 
                  cprint('-'+'\n'+'[DEV]: Logging Error. ' + '\n' + 'Log Type: ' + str(log_type) + '\n', 'red')
               except SyntaxError or NameError:
                  print('[DEV]: Logging Error ' + '\n' + 'Log Type: ' + str(log_type) + '\n' + 'Text: ' + str(text))
               except: 
                  disable()
            try: 
               cprint(('['+log_title+']: ')+str(text),log_color)
            except SyntaxError or NameError:
               print('['+log_title+']: ')+str(text)
            except: 
               disable()
            return
         return
