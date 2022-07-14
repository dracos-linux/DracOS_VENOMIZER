#! /usr/share/bin/python3
#! -*- coding: utf-8 -*-
#! PasswordAttack.py
import os
from color import *
import Logo


def PassAtck():
    os.system("clear")
    Logo.logo_15()

    lists = ('brutespray', 'brup', 'cewl', 'chntpw', 'cisco-auditing-tool', 'cmospwd', 'creddump',
     'crowbar', 'crunch', 'findmyhash', 'gpp-decrypt', 'hash-identifier', 'hashcat', 'hexorbase', 
     'thc-hydra', 'john the ripper', 'johnny', 'keimpx', 'maltego teeth', 'maskprocessor', 'multiforcer', 
     'ncrack', 'oclgausscrack', 'ophcrack', 'pack', 'patator', 'phrasendrescher', 'polenum', 'rainbowcrack', 
     'rcracki-mt', 'rsmangler', 'seclists', 'sqldict', 'statsprocessor', 'thc-pptp-bruter', 'truecrack', 
     'webscarab', 'wordlists', 'zaproxy')
    
    list_tool(lists)
    print(G("    101. Back to Main Menu"))
    print(R("    102. exit"))

    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu in range(len(lists)):
        menu -= 1
        # Call function
        passwordATK_tool(lists[menu])
    elif menu == 101:
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # //usr/bin/
    elif menu == 102:
        exit()
    else:
        print(R('Wrong Input!'))
        input()
    back()


def list_tool(a):
    num = 0
    for x in range(len(a)):
        num += 1
        if os.path.isfile(f'/usr/bin/{a[x]}'):
            print(G(f'[{num}] {a[x]}'))
        else:
            print(R(f'[{num}] {a[x]}'))


def back():
    PassAtck()
#Funciton
# passwordATK_tool
def passwordATK_tool(a):
    if os.path.isfile(f"/usr/bin/{a}"):
        os.system("clear")
        print(B("Tools Available"))
        input()
        back()
    else:
        os.system(
            f'xterm -T "☣ INSTALL {a} ☣" -geometry 100x30 -e "sudo apt install {a}"'
        )
        os.system("clear")
        if os.path.isfile(f"/usr/bin/{a}"):
            print(B(f"{a} Already Installed"))
        else:
            print(R(f"{a} Not Installed"))
    input()
    # back()
        # end passwordATK_tool

