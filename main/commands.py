from main.code import main, clear
from main.config import p, config, cmds, app_version, projects_folder
from main.sub_commands import wait, change_editor
from main.dev.logging import log, logging

from time import sleep as time_sleep
from subprocess import Popen as sp_Popen
from os import listdir as os_listdir, getcwd as os_getcwd
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
         if config.cxml.fancy_print == False:
            config.cxml.fancy_print = True
            config.fprint_status = 'Enabled'
            config.fprint = .07
         else:
            config.cxml.fancy_print = False
            config.fprint_status = 'Disabled'
            config.fprint = 0
         config.cxml.data.set('fancy_print',str(config.xml.fancy_print))
         config.cxml.tree.write(config.xml.data_file)
         clear()
         configuration()
      elif i in ['change editor','editor','2',2]:
         change_editor()
      elif i in cmds.menu:
         main()
      else: 
         continue

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

def open_file(file=None):
   if file[4:]:
      print(file[4:])
#      main()
   else:
      while True:
         for file_name in os_listdir(projects_folder):
            print(file_name[:-4])
         print()
         i = input('File: ')
         if i in cmds.menu:
            main()
         elif i == '':
            log(2,'Input invalid - open_file')
         else:
            temp = str(i).lower()+'.txt'
            for file_name in os_listdir(projects_folder):
               print(str(file_name) + ' - ' + temp)
               if str(file_name).lower() == temp:
                  file = (str(os_getcwd())+'\\main\\ascii\\'+str(i)+'.txt')
                  print(str(file_name) + ' - ' + temp)
                  sp_Popen([config.editor, file])
                  main()
            clear()
            print('That file was not found, please try again or type "home" to go back.')
            continue

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
         for file_name in os_listdir('main/ascii'):
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
      time_sleep(3)
      editor = config.editor
      file = (str(os_getcwd())+'\\main\\ascii\\'+str(project_name)+'.txt')
      sp_Popen([editor, file])
      main()