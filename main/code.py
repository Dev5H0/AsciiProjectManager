# Imports
import subprocess as sp
from sys import exit
import time
import os

# File Imports
try: 
   from dev.logging import log
except ImportError: 
   from main.dev.logging import log, logging
except: 
   def log(a=None,b=None,c=None):
      pass

# Configuration
app_version = "v1.0.0"
projects_folder = 'main/ascii'
projects_folder_alt = str(os.getcwd())+'\\main\\ascii\\'

# Functions
def change_editor():
   print('Supported Editors: ' + 'Wordpad, Notepad, Notepad++, Visual Studio Code')
   i = input('> ')
   if i in config.supported_editors.all_editors:
      if i in config.supported_editors.vsc:
         i = ''
      elif i in config.supported_editors.npp:
         i = 'Notepad++'
      else:
         pass

def command_handler(i='',caller='main'):
   while True:
      if i == '':
         main()
      elif caller == 'main':
         if i in cmds.stop:
            clear()
            exit()
         else: 
            clear()
         if i in cmds.start:
            open_file()
         elif i in cmds.start[:5]:
            open_file(i[5:])
         elif i in cmds.start[:4]:
            open_file(i[5:])
         if i in cmds.files:
            for file_name in os.listdir(projects_folder):
               print(file_name[:-4])
               wait()
            main('')
         # elif i in ['exe']:
         #    change_editor()
         elif i in cmds.cmd_list:
            read_text('help')
            main('')
         elif i in cmds.create:
            new_project()
         elif i == 'credits':
            read_text('credits')
            main('')
         elif i[:5] == 'print':
            file_read(i[6:])
         elif i in cmds.menu:
            main()
         elif i in cmds.settings:
            configuration()
         elif i == 'discord':
            print('Discord Server: ' + social.discord)
            main('')
         else: 
            file_read(i)
      else: 
         log(2,('Caller "' + str(caller) + '" was not found. Please join our Discord for support.'))
      main()

def read_text(file=None):
   if file == None:
      return
   else: 
      try:
         for line in open('main/dev/texts/'+file+'.txt'):
            p(line)
            wait()
         main('')
      except FileNotFoundError:
         main()

def wait_input():
   i = input('Press enter to go back to the main menu.')
   if i == i: 
      main()

def clear():
   _ = os.system(config.clear_command)
   print('----------------------------------')
   print('Type "help" for a list of commands')
   print('----------------------------------')
   print('')

def main(c=None):
   if c == None:
      clear()
   else:
      print('')
   while True:
      i = input('> ')
      if i != '' or ' ':
         i = i.lower()
         command_handler(i,'main')
      else: 
         clear()

def new_project():
   naming = True
   while True:
      while naming:
         clear()
         print('Leave project name empty to cancel')
         project_name = input('Project Name: ')
         if project_name == '':
            main()
         temp_project_name = str(project_name).lower()+'.txt'
         for file_name in os.listdir('main/ascii'):
            if str(file_name).lower() == temp_project_name:
               print('That project name already exists, please try again')
               continue
         for invalid_name in config.invalid_names:
            if str(file_name).upper() == invalid_name:
               print('That project name cannot be used on this operating system, please try again')
               continue
         if project_name in config.invalid_chars:
            print('That project name includes an invalid character, please try again')
            continue
         naming = False
      try: 
         open((str(projects_folder) + '/' + str(project_name) + '.txt'),'x')
      except FileExistsError: 
         continue
      time.sleep(1)
      log(0,(str(os.getcwd())+'\\ascii\\'+str(project_name)+'.txt'))
      editor = config.editor
      file = (str(os.getcwd())+'\\main\\ascii\\'+str(project_name)+'.txt')
      sp.Popen([editor, file])
      main()

def open_file(file=None):
   if file == '' or None:
      main()
   else:
      while True:
         for file_name in os.listdir(projects_folder):
            print(file_name[:-4])
         print()
         i = input('File: ')
         if i in cmds.menu:
            main()
         elif i == '':
            log(2,'Input invalid - open_file')
         else:
            temp = str(i).lower()+'.txt'
            for file_name in os.listdir(projects_folder):
               print(str(file_name) + ' - ' + temp)
               if str(file_name).lower() == temp:
                  file = (str(os.getcwd())+'\\main\\ascii\\'+str(i)+'.txt')
                  print(str(file_name) + ' - ' + temp)
                  sp.Popen([config.editor, file])
                  main()
   #         clear()
            print('That file was not found, please try again or type "home" to go back.')
            continue

def openfile():
   print('This command is currently not working, sorry for the inconvenience')
   main('')
   for file_name in os.listdir(projects_folder):
      print(file_name[:-4])
   while True:
      i = input('> ')
      if i == '':
         continue
      for file_name in os.listdir(projects_folder):
         if i.lower == file_name.lower:
            sp.run([config.editor,(projects_folder_alt+str(i)+'.txt')])
            break
      print('That was not detected as a valid file')

def file_read(file):
   try: file = open(str(projects_folder) + '/' + str(file) + '.txt')
   except FileNotFoundError: 
      print('That was not recognised as a valid command!')
      main('')
   lines = file.readlines()
   print('')
   for line in lines:
      p(line)
      wait()
   print('')
   print('')
   print('')
   main('')

def configuration():
   wait()
   print('1. Toggle Fancy Printing - ' + config.fprint_status)
   wait()
   print('2. Change Editor (WiP)')
   wait()
   print('3. Logging')
   while True:
      print('\n(Type "back" to go to the menu)')
      i = input('> ')
      if i in ['3',3]:
         if logging == False:
            logging = True
         elif logging == True:
            logging = False
         else: 
            continue
         return logging
      if i in ['fprint','fancy print','1',1]:
         if xml_config.fancy_print == False:
            xml_config.fancy_print = True
            config.fprint_status = 'Enabled'
            config.fprint = .07
         else:
            xml_config.fancy_print = False
            config.fprint_status = 'Disabled'
            config.fprint = 0
         xml_config.data.set('fancy_print',str(xml_config.fancy_print))
         xml_config.tree.write(xml_config.data_file)
         clear()
         configuration()
      elif i in ['change editor','editor','2',2]:
         change_editor()
      elif i in cmds.menu:
         main()
      else: 
         continue

class cmds:
   cmd_list = ['?','help','info','cmd','cmds','command','commands'] # Lists commands
   settings = ['settings','config','configuration','configurations']
   menu = ['back','main','menu','main menu','home']
   files = ['!','dir','directory','files','projects'] # Lists the project directory
   create = ['create','new'] # Create a new file
   start = ['start','open'] # Opens in editor
   stop = ['stop','exit','quit','leave'] # Quits the application


class xml_config:
   import xml.etree.ElementTree as xml
   data_file = './main/settings.xml'
   tree = xml.parse(data_file)
   data = tree.find('settings')
   editor = data.get('editor')+'.exe'
   fancy_print = bool(data.get('fancy_print'))

class config:
   if os.name == 'nt':
      clear_command = 'cls'
      invalid_chars = ['\\','/','<','>',':','"','|','?','*']
      invalid_names = ['CON','PRN','AUX','NUL','COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','LPT1','LPT2','LPT3','LPT4','LPT5','LPT6','LPT7','LPT8','LPT9']
   elif os.name == 'posix':
      clear_command = 'clear'
      invalid_chars = ':'
      invalid_names = ['']

   

   class supported_editors:
      windows_editors = ['wordpad','notepad'],
      npp = ['notepad++','notepad plus plus','n++','npp']
      vsc = ['vsc','vscode','vs code','visual studio code']
      all_editors = [windows_editors, npp, vsc]

   editor = xml_config.editor

   if xml_config.fancy_print == True:
      fprint_status = 'Enabled'
      fprint = .07
   else: 
      fprint_status = 'Disabled'
      fprint = 0

class social:
   discord = 'https://discord.gg/THE5XUF6Rc'

def wait():
   time.sleep(config.fprint)

#-
p = lambda t: print(t,end='',)
os.system('title '+('ASCII Project Manager' + ' - ' + str(app_version)))
main()
