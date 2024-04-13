import os, sys 
os.system("git pull")
try:
_import_("KAYAT").Spy() 
except Exception as e: 
exit(str(e))
