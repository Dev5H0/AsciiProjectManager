# Imports
from import_manager import os_listdir, os_getcwd, sp_Popen, time_sleep, os_system
from config import cmds, social, config, p, projects_folder, supported_editors, app_version

try: 
   from dev.settings import debug_mode
except:
   debug_mode = False
try: 
   from dev.logging import log
except: 
   logging = False
   def log(x=None, y=None):
      pass

# Commands
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

def command_handler(i='',caller='main'):
   if debug_mode == True:
      if i == 're': # So it's easier for me to restart
         command_handler('restart')
   while True:
      if i == '':
         main()
      for c in i:
         if c in config.invalid_characters:
            clear()
            print('That command contains an invalid character.')
            main('')
      if i in ['restart','relaunch']:
         os_system((os_getcwd() + '\\start.bat'))
         exit()
      elif caller == 'main':
         if i in cmds.stop:
            clear('')
            exit()
         else: 
            clear()
         for x in cmds.start:
            if i == x:
               open_file()
            elif i in cmds.start[:5] or i in cmds.start[:4]:
               if i in cmds.start[:5]:
                  open_file(i[5:])
               else:
                  open_file(i[4:])
         if i in cmds.files:
            for file_name in os_listdir(projects_folder):
               print(file_name[:-4])
               wait()
            main('')
         elif i in ['exe']:
             change_editor()
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

def configuration():
   while True:
      wait()
      print('1. Toggle Fancy Printing - ' + config.fprint_status)
      wait()
      print('2. Change Editor')
      wait()
      print('\n(Type "back" to go to the menu)')
      i = input('> ')
      if i in ['fprint','fancy print','1',1]:
         if config.cxml.fancy_print == False:
            config.cxml.fancy_print = True
            config.fprint_status = 'Enabled'
            config.fprint = .07
         else:
            config.cxml.fancy_print = False
            config.fprint_status = 'Disabled'
            config.fprint = 0
         config.cxml.data.set('fancy_print',str(config.cxml.fancy_print))
         config.cxml.tree.write(config.cxml.data_file)
         clear()
         configuration()
      elif i in ['change editor','editor','2',2]:
         clear()
         change_editor()
      elif i in (cmds.menu or '0'):
         main()
      else: 
         clear()
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
            print('That file was not found, please try again. \n(Type "back" to go to the menu)\n')
            continue

def file_read(file):
   try: 
      file = open(str(projects_folder) + '/' + str(file) + '.txt')
   except FileNotFoundError: 
      print('That was not recognised as a valid command.')
      main('')
   except OSError:
      print('That command contains an invalid character.')
      main('')
   except:
      print('That was not recognized as a valid command.')
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

def change_editor():
   while True:
      print('Supported Editors: ' + 'Wordpad, Notepad, Notepad++, Visual Studio Code')
      i = input('> ')
      i = i.lower()
      settings = config.cxml.tree.find('settings')
      if i in cmds.menu:
         main()
      elif i in supported_editors.win_editors: # It can't enter this for some reason
         new_editor = i
         cur_editor = i.capitalize()
      elif i in supported_editors.vsc:
         new_editor = 'vscode'
         cur_editor = 'Visual Studio Code'
      elif i in supported_editors.npp:
         new_editor = 'notepad++'
         cur_editor = 'Notepad++'
      else:
         clear()
         print('That was not recognised as a valid editor, please try again. ')
         os_system('pause')
         clear()
         continue
#         log(2, 'Couldn\'t set editor - input: ' + str(i))
      try: 
         new = settings.set('editor', new_editor)
         break
      except:
         print('We recieved an error, please try again.')
         os_system('pause')
         clear()
         continue
   config.cxml.tree.write(config.cxml.data_file, new)
   clear()
   print('Set editor to ' + cur_editor)
   wait()
   main('')

# Sub Commands
def clear(p=None):
   os_system(config.clear_command)
   if p == None:
      print('----------------------------------')
      print('Type "help" for a list of commands')
      print('----------------------------------')
      print('')

def wait():
   time_sleep(config.fprint)

#-
os_system('title ASCII Project Manager' + ' - ' + str(app_version))
main()
