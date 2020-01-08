import idleTime as q
from subprocess import Popen
import os
# name = 

while True:
    time = q.get_idle_duration()
    if (time < 1800):
        print(time)
    os.system('cls')
    if(int(time)==1800):
        p = Popen("terminateFile.bat", cwd=r"C:\Users\Exam\Desktop\test\Remote_switchOff-master")
        stdout, stderr = p.communicate()
    else:
        print("Press CTRL+C to stop shutdown")
