#!/usr/bin/python3
# -*- coding: utf-8 -*-
# venomizer.py

# import packages hacking
import hacking
from color import *
from termcolor import colored as c
import sys
import Logo
import os.path
import os
from sys import exit



# if os.path.isfile('sudo /usr/local/lib/python3.7/dist-packages/termcolor.py'):
#     print()
# else:
#     os.system('xterm -T " INSTALL TERMCOLOR " -geometry 100x30 -e "sudo pip install termcolor -y"')
# cek root
def checkroot():
    if os.geteuid() != 0:
        print(c("[-]", 'red')+c(" You must be root to run this script", 'red'))
        sys.exit()
# cek apakah file git sudah ada!
# jika sudah ada maka kita lewati
if os.path.isfile('/usr/bin/git'):
    print()
else:
    # jika belum install dulu
    os.system(
        'xterm -T "☣ INSTALL GIT ☣" -geometry 100x30 -e "sudo apt-get install git -y"')

#
# logo


def LOGO():
    os.system("clear")
    print(c("        -os:", 'red'))
    print("            "+c("-os/`", 'red'))
    print("            "+c("  :s", 'red')+c("y+-`", 'red'))
    print("            "+c("   `/y", 'red')+c("yyy+.", 'red'))
    print("            "+c("     `+y", 'red')+c("yyyo-", 'red'))
    print("            "+c("       `/y", 'red')+c("yyys:", 'red'))
    print(c("`:osssoo", 'red')+c("oo++-", 'red'),
          c("        +y", 'red')+c("yyyyy/`", 'red'))
    print(c("   ./yyyy", 'red')+c("yyo ", 'red'),
          c("        yo`", 'red')+c(":syyyy+.", 'red'))
    print(c("      -oyy", 'red')+c("y+ ", 'red') +
          c("        +-   :y", 'red')+c("yyyyo-", 'red'))
    print(c("        `:s", 'red')+c("y:", 'red') +
          c("        `.    `/y", 'red')+c("yyyys:", 'red'))
    print(c("           .", 'red')+c("/o')+/.`", 'red') +
          c("           .oyy", 'red')+c("so+oo:`", 'red'))
    print(c("              :+oo+//::::///:-.`", 'red')+c("     `.`", 'red'))
    print(c('=================================================================', 'green'))
    print("__      _______ __   __  _____  ___  ___ _____ ___________ _____   ")
    print("\ \    / / ____|  \  | |/ ___ \|   \/   |_   _|___  |  ___| __   \ ")
    print(" \ \  / /| |__ |   \ | | |   | | |\  /| | | |    / /| |__ | |__) / ")
    print("  \ \/ / |  __|| |\ \| | |   | | | \/ | | | |   / / |  __||  _  /  ")
    print("   \  /  | |___| | \   | |___| | |    | |_| |_ / /__| |___| | \ \  ")
    print("    \/   |_____|_|  \__|\_____/|_|    |_|_____/_____|_____|_|  \_\ ")
    print(c("Version : 1.2.7     Codename : Mr. Robot", "blue"))
    print(c('[(c) 2022 |', 'red'), c(
        'dracos-linux.org | https://github.com/dracos-linux', 'red')+c(']', 'red'))


# menu
global DracOS
DracOS = c('[', 'green')+c('DracOS', 'red')+c(']> ', 'green')


def menu():
    checkroot()

    # call logo
    os.system('clear')
    LOGO()
    # print(c('[PERHATIAN UNTUK PERTAMA KALI LAKUKAN SETUP!!!] klik Y', 'green'))
    print(c('1.  Information Gathering', 'green'))
    print(c('2.  Vulnerability Analysis', 'green'))
    print(c('3.  Wireless Attacks', 'green'))
    print(c('4.  Web Applications', 'green'))
    print(c('5.  Exploitation Tools', 'green'))
    print(c('6.  Stress Testing', 'green'))
    print(c('7.  Forensics Tools', 'green'))
    print(c('8.  Sniffing & Spoofing', 'green'))
    print(c('9.  Password Attacks', 'green'))
    print(c('10. Maintaining Access', 'green'))
    print(c('11. Reverse Engineering', 'green'))
    print(c('12. Reporting Tools', 'green'))
    print(c('13. Hardware Hacking', 'green'))
    print(c('0.  Update Repository', 'green'))
    print(c('99. Update tools Venomizer', 'green'))
    print(c('00. exit'))
    
    menu = input(DracOS)
    if menu == '0':
        var = input('sudo apt update(y/n)? ')
        if var == 'y':
            os.system('sudo apt update')
            back()
        else:
            back()
    elif menu == '99':
        os.system(
            f'xterm -T "☣ INSTALL Update Tools Venomizer ☣" -geometry 100x30 -e "cd /usr/bin/DracOS_VENOMIZER/ && sudo git pull"'
        )
        print(B("Tools Updating"))
        print(R("[ DONE ]"))
        print(G("Restart, please click Enter..."))
        input()
        os.system("vnm")
    elif menu == '1':
        hacking.InfoGat()
    elif menu == '2':
        hacking.VulnAs()
    elif menu == '3':
        hacking.WireAttack()
    elif menu == '4':
        hacking.WebApp()
    elif menu == '5':
        hacking.Exploit()
    elif menu == '6':
        hacking.Stress()
    elif menu == '7':
        hacking.Forensics()
    elif menu == '8':
        hacking.Sniffing()
    elif menu == '9':
        hacking.PassAtck()
    elif menu == '10':
        hacking.MaintiningF()
    elif menu == '11':
        hacking.Reverse()
    elif menu == '12':
        hacking.Report()
    elif menu == '13':
        hacking.Hardware()
    elif menu == '00':
        print(R("Thanks for using venomizer "))
        os.system('exit')
        sys.exit()
        exit()
    elif menu == 'clear':
        os.system('clear')
    else:
        print(c('Wrong Input!', 'red'))
        input()
    back()
# x-terminal-emulator

def back():
    menu()

# while menu():    
#     menu()
        
if __name__ == '__main__':
    menu()
