def import_error(import_type=None):
   if import_type == None:
      import_type = ''
   if import_type == 'module' or 'm':
      import_type = ' from module'
   elif import_type == 'file' or 'f':
      import_type = ' from file'

   if logging == True:
      log(3, 'Couldn\'t import' + import_type + '. \nPlease join our Discord for support: "https://discord.gg/THE5XUF6Rc')
   print('Couldn\'t import' + import_type + '. \nPlease join our Discord for support: "https://discord.gg/THE5XUF6Rc')

# Imports
try: from sys import exit
except:
   import_error('m')
try: 
   import os
except:
   import_error('m')

# File Imports
try: 
   from main.dev.logging import log, logging
except:
   logging = False
   def log(x=None, y=None):
      pass

try: 
   from main.config import cmds, clear, wait, social
except:
   import_error('f')

try:
   from main.commands import open_file, read_text, new_project, file_read, configuration, app_version, projects_folder
except:
   import_error('f')

# Functions
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
         for x in cmds.start:
            if i == x:
               open_file()
            elif i in cmds.start[:5] or i in cmds.start[:4]:
               if i in cmds.start[:5]:
                  open_file(i[5:])
               else:
                  open_file(i[4:])
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

#-
os.system('title '+('ASCII Project Manager' + ' - ' + str(app_version)))
main()
