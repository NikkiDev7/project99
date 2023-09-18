import os
import shutil
import time

filepath = input("Put the path of the file you want to remove:")
time1 = int(input("Put the time of the files you want to keep:"))

def removefiles():
    if os.path.exists(filepath):
        days=time.time()-(30*24*60*60)
        files = os.walk(filepath)
        ctime = os.stat(files).st_ctime
        if ctime > days:
            if os.path.isfile(filepath):
                os.remove(filepath)
            else:
                shutil.rmtree(filepath)
    else:
        print("Path Not Found")

removefiles()
