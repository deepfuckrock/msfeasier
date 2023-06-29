import Installer
import program

try:
    import colorama
except ImportError:
    print('colorama is not installed, installing it with other neccessary modules')
    Installer.install()
from colorama import Fore, Style
try:
    import requests
except ImportError:
    print('requests is not installed, installing it with other necessary repositories')
    Installer.install()
import os
import time
import pip

def CLC():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def quickchech():
    print('checking (0%)\r')
    check=os.system('which msfconsole > /dev/null')
    print("checking (75%)\r")
    if check==256:
        print("running installer")
        program.uno()
    return

CLC()

print(Fore.LIGHTCYAN_EX + 'Welcome!' + Style.RESET_ALL)
time.sleep(2)

##quickchech()

try:
    request = requests.get("https://www.google.com", timeout=5)
except (requests.ConnectionError, requests.Timeout):
    print("Checking connection: " +Fore.RED+"DISCONNECTED")
    print('CLOSING PROGRAM :('  + Style.RESET_ALL)
    time.sleep(1)
    exit()
else:
    print("Checking connection: " +Fore.GREEN+ "CONNECTED")
    print('STARTING PROGRAM :)'  + Style.RESET_ALL)
    time.sleep(1)

print("\n\t1) Installer\t\t2) payload(win)\n\t3) payload(andr)\t4) Activate listener\n\t5) Clean executables")
print()

todo=input('Put here the wanted option (1,2...): ')
while True:
        todoc=todo in ['1','2','3','4','5','6']
        if todoc==False:
            print(Fore.RED + 'select a valid number' + Style.RESET_ALL)
            quit()
        else:
            break

if todo=='1':
    program.uno()
if todo=='2':
    quickchech()
    program.dos()
if todo=='3':
    quickchech()
    program.tres()
if todo=='4':
    quickchech()
    program.cuatro()
if todo=='5':
    quickchech()
    program.cinco()
if todo=='6':
    os.system('sudo rm -r __pycache__')
    print('cache erased')
