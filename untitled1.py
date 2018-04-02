import glob
import os
import datetime

files = glob.glob("*")
files.sort(key=os.path.getmtime)
os.stat('file.txt').st_mtime
if os.path.getmtime==datetime.datetime.now().strftime ("%YY %mM %dd") :
    print("\n".join(files))