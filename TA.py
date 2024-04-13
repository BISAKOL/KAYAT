import os, sys 
os.system("git pull")
try:
_import_("TA").Spy() 
except Exception as e: 
exit(str(e))
