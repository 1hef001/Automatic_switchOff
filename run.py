import os

def Windows():
    import idleTime as q
    from subprocess import Popen, PIPE
    # import os
    import libDep as l



    while True:
        time = q.get_idle_duration()
        if (time < l.TIME):
            print(time)
        os.system('clear')
        if(int(time)==l.TIME):
            p = Popen(l.FILENAME,shell=True,cwd=l.PATH,stdout=PIPE).stdout
            stdout, stderr = p.communicate()
        else:
            print("Press CTRL+C to stop shutdown")



def Linux():
    # import os
    import libDep as l
    os.system('python3 preReq.pyw')
    os.system('clear')
    os.system('sh '+l.PATH + '/' + l.FILENAME)


import platform
if (platform.system() == 'Windows'):
    Windows()
elif (platform.system() == 'Linux'):
    Linux()
