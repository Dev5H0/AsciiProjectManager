def import_error(i, import_type=None):
   if import_type == 'module' or 'm':
      import_type = '(from) module'
   elif import_type == ' (from) file' or 'f':
      import_type = 'file'
   else:
      import_type = ''
   print('\033[91m'+'Error importing ' + import_type + ' - '+ i + '\nPlease join our Discord for support: "https://discord.gg/THE5XUF6Rc' + '\033[0m')

try:
   from os import listdir as os_listdir
except:
   import_error('os.listdor','m')

try:
   from os import getcwd as os_getcwd
except:
   import_error('os.getcwd','m')

try:
   from os import system as os_system
except:
   import_error('os.system','m')

try:
   from time import sleep as time_sleep
except:
   import_error('time.sleep','m')

try:
   from subprocess import Popen as sp_Popen
except:
   import_error('subprocess.Popen','m')
