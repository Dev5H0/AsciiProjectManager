# Imports
from import_manager import os_getcwd

# Variables
p = lambda t: print(t,end='',)

app_version = "v1.0.0"
projects_folder = 'main/ascii'
projects_folder_alt = str(os_getcwd())+'\\main\\ascii\\'

# Functions
class cmds:
   cmd_list = ['?','help','info','cmd','cmds','command','commands'] # Lists commands
   settings = ['settings','config','configuration','configurations']
   menu = ['back','main','menu','main menu','home']
   files = ['!','dir','directory','files','projects'] # Lists the project directory
   create = ['create','new'] # Create a new file
   start = ['start','open'] # Opens in editor
   stop = ['stop','exit','quit','leave'] # Quits the application


class config:
   from os import name as os_name
   class cxml:
      import xml.etree.ElementTree as xml
      data_file = './main/settings.xml'
      tree = xml.parse(data_file)
      data = tree.find('settings')
      editor = data.get('editor')+'.exe'
      fancy_print = bool(data.get('fancy_print'))

   if os_name == 'nt':
      clear_command = 'cls'
      invalid_chars = ['\\','/','<','>',':','"','|','?','*']
      invalid_names = ['CON','PRN','AUX','NUL','COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','LPT1','LPT2','LPT3','LPT4','LPT5','LPT6','LPT7','LPT8','LPT9']
   elif os_name == 'posix':
      clear_command = 'clear'
      invalid_chars = ':'
      invalid_names = ['']


   editor = cxml.editor

   if cxml.fancy_print == True:
      fprint_status = 'Enabled'
      fprint = .07
   else: 
      fprint_status = 'Disabled'
      fprint = 0

class supported_editors:
   windows_editors = ['wordpad','notepad'],
   npp = ['notepad++','notepad plus plus','n++','npp']
   vsc = ['vsc','vscode','vs code','visual studio code']
   all_editors = [windows_editors, npp, vsc]

class social:
   discord = 'https://discord.gg/THE5XUF6Rc'

