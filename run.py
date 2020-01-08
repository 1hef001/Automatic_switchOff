import idleTime as q
from subprocess import Popen, PIPE
import os
import winDep as l
import psutil


while True:
    time = q.get_idle_duration()
    if (time < l.TIME):
        print(time)
    os.system('cls')
    if(int(time)==l.TIME):
        for proc in psutil.process_iter():
            proc.kill()
        
        p = Popen(l.FILENAME,shell=True,cwd=l.PATH,stdout=PIPE).stdout
        stdout, stderr = p.communicate()
    else:
        print("Press CTRL+C to stop shutdown")
