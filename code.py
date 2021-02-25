# Imports
import sys
from time import sleep as wait
from os import listdir, name, system, getcwd
from subprocess import run
from sys import exit
from time import sleep

# File Imports
try: from dev.logging import log
except ImportError: 
   def log(a,b=None):
      pass

# Configuration
projects_folder = 'ascii/'

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
         if i in ['exe']:
            change_editor()
         elif i in cmds.files:
            for file_name in listdir('ascii'):
               print(file_name[:-4])
            print('')
         elif i in cmds.cmd_list:
            print('credits | Creator\'s social media')
            print('dir | Gives you a list of files')
            print('print | Prints contents of file')
            print('new | Create and open new file in editor')
            print('exit | Closes the window')

            print('')
            print('DISABLED')
            print('open | Open file in editor')
            print('')
            return
         elif i in cmds.create:
            new_project()
         elif i == 'credits':
            print('')
            print('Discord: 5H0#5782')
            print('Github: Dev5H0')
            print('Reddit: BoredCatGod')
            print('')
            return
         elif i == open:
            pass
         elif i[:5] == 'print':
            file_read(i[6:])
         else: 
            print('That was not detected as a valid command, please try again')
      elif caller == 'change_editor':
         pass
      else: log(2,('Caller "' + str(caller) + '" was not found. Please contact "5H0#5782" on Discord or create a report on Github.'))
      main()

def clear():
   _ = system(config.clear_command)
   print('Type "help" for a list of commands')

def main():
   # clear()
   while True:
      i = input('> ')
      if i != '' or ' ':
         command_handler(i,'main')
      else: clear()

def new_project():
   naming = True
   while naming:
      print('Leave project name empty to cancel')
      project_name = input('Project Name: ')
      if project_name == '':
         main()
      temp_project_name = str(project_name).lower()+'.txt'
      for file_name in listdir('ascii'):
         if str(file_name).lower() == temp_project_name:
            print('That project name already exists, please try again')
            continue
      for invalid_name in config.invalid_names:
         if str(file_name).upper() == invalid_name:
            print('That name cannot be used on this operating system, please try again')
            continue
      if project_name in config.invalid_chars:
         print('That name most likely includes an invalid character , please try again')
         continue
      naming = False
   open(('ascii/'+str(project_name)+'.txt'),'x')
   sleep(1)
   log(0,(str(getcwd())+'\\ascii\\'+str(project_name)+'.txt'))
   run([config.editor,(str(getcwd())+'\\ascii\\'+str(project_name)+'.txt')])

def file_read(file):
   try: testFile = open("ascii/"+str(file)+".txt")
   except FileNotFoundError: 
      print('That was not recognised as a valid command!')
      return
   lines = testFile.readlines()
   print('')
   for line in lines:
      p(line)
      wait()
   print('')
   print('')
   print('')
   return

class cmds:
   cmd_list = ['?','help','info','cmd','cmds','command','commands']
   files = ['!','dir','directory','files','projects']
   stop = ['stop','exit','quit','leave']
   create = ['create','new']


class xml_config:
   from xml.etree.ElementTree import ElementTree as xml
   tree = xml.parse(xml,'./settings.xml')
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
      fprint = '.02'
   else: 
      fprint = '0'
def wait():
   sleep(config.fprint)

#-
p = lambda t: print(t,end='',)
system('title '+'ASCII Printer - Made by 5H0')
main()
