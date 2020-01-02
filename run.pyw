from idle_time import IdleMonitor
from subprocess import Popen

name = "terminateFile.bat"

while True:
    monitor = IdleMonitor.get_monitor()
    time=monitor.get_idle_time()
    print(time)
    if(int(time)==30):
        p = Popen(name, cwd=r"C:\Windows\System32")
        stdout, stderr = p.communicate()
    else:
        pass
