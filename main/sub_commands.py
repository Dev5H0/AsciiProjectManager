from main.code import main
from main.config import config, supported_editors

from os import system as os_system
from time import sleep as time_sleep

def wait_input():
   i = input('Press enter to go back to the main menu.')
   if i == i: 
      main()

def clear():
   _ = os_system(config.clear_command)
   print('----------------------------------')
   print('Type "help" for a list of commands')
   print('----------------------------------')
   print('')

def wait():
   time_sleep(config.fprint)

def change_editor():
   print('Supported Editors: ' + 'Wordpad, Notepad, Notepad++, Visual Studio Code')
   i = input('> ')
   if i in supported_editors.all_editors:
      if i in supported_editors.vsc:
         i = ''
      elif i in supported_editors.npp:
         i = 'Notepad++'
      else:
         pass

