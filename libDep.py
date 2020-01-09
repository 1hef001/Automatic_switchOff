import os
import platform

if(platform.system() == 'Windows'):
    FILENAME = 'terminateFile.bat'
elif(platform.system() == 'Linux'):
    FILENAME = 'idle.sh'
TIME = 900
PATH = os.getcwd()
# print(platform.system())