# Imports
import sys
from time import sleep as wait
from os import listdir, name, system, getcwd
from subprocess import run
from sys import exit, version
from time import sleep

# File Imports
try: 
   from dev.logging import log
except ImportError: 
   from main.dev.logging import log
except: 
   def log(a=None,b=None,c=None):
      pass

# Configuration
app_version = "v1.0.0"
projects_folder = 'main/ascii'
projects_folder_alt = str(getcwd())+'\\main\\ascii\\'

# Functions
def change_editor():
   print('Supported Editors: '+'Notepad, Wordpad, Visual Studio (Code), Notepad++')
   i = input('> ')
   command_handler(i,'change_editor')

def command_handler(i='',caller='main'):
   while True:
      if i == '':
         return
      elif caller == 'main':
         if i in cmds.stop:
            clear()
            exit()
         else: clear()
         if i in cmds.start:
            open_file()
         if i in cmds.files:
            for file_name in listdir(projects_folder):
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
         else: file_read(i)
      elif caller == 'change_editor':
         pass
      else: log(2,('Caller "' + str(caller) + '" was not found. Please contact "5H0#5782" on Discord or create a report on Github.'))
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
   _ = system(config.clear_command)
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
         command_handler(i,'main')
      else: clear()

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
         for file_name in listdir('main/ascii'):
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
      try: open((str(projects_folder) + '/' + str(project_name) + '.txt'),'x')
      except FileExistsError: 
         naming = True
         continue
      sleep(1)
      log(0,(str(getcwd())+'\\ascii\\'+str(project_name)+'.txt'))
      run([config.editor,(projects_folder_alt+str(project_name)+'.txt')])
      main()

def open_file():
   print('This command is currently not working, sorry for the inconvenience')
   main('')
   for file_name in listdir(projects_folder):
      print(file_name[:-4])
   while True:
      i = input('> ')
      if i == '':
         continue
      for file_name in listdir(projects_folder):
         if i.lower == file_name.lower:
            run([config.editor,(projects_folder_alt+str(i)+'.txt')])
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

def configuration(caller=None):
   wait()
   print('1. Toggle Fancy Printing - ' + config.fprint_status)
   wait()
   print('2. Change Editor (WiP)')
   wait()
   if caller == 'config':
      main('')
   else:
      print('')
   while True:
      i = input('> ')
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
         configuration('config')
      elif i in cmds.menu:
         main()
      else: 
         continue

class cmds:
   cmd_list = ['?','help','info','cmd','cmds','command','commands'] # Lists commands
   settings = ['settings','config','configuration','configurations']
   menu = ['back','main','menu','main menu']
   files = ['!','dir','directory','files','projects'] # Lists the project directory
   create = ['create','new'] # Create a new file
   start = ['start','open','execute'] # Opens in editor
   stop = ['stop','exit','quit','leave'] # Quits the application


class xml_config:
   import xml.etree.ElementTree as xml
   data_file = './main/settings.xml'
   tree = xml.parse(data_file)
   data = tree.find('settings')
   editor = data.get('editor')+'.exe'
   fancy_print = bool(data.get('fancy_print'))

class config:
   if name == 'nt':
      clear_command = 'cls'
      invalid_chars = ['\\','/','<','>',':','"','|','?','*']
      invalid_names = ['CON','PRN','AUX','NUL','COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','LPT1','LPT2','LPT3','LPT4','LPT5','LPT6','LPT7','LPT8','LPT9']
   elif name == 'posix':
      clear_command = 'clear'
      invalid_chars = ':'
      invalid_names = []

   editor = xml_config.editor

   if xml_config.fancy_print == True:
      fprint_status = 'Enabled'
      fprint = .07
   else: 
      fprint_status = 'Disabled'
      fprint = 0

def wait():
   sleep(config.fprint)

#-
p = lambda t: print(t,end='',)
system('title '+('ASCII Project Manager' + ' - ' + str(app_version)))
clear()
main()
