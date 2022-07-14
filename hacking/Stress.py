#!/usr/bin/python3
#! -*- coding: utf-8 -*-
#! Stress.py
import os, sys
from color import *
import Logo

def checkroot():
    if os.geteuid() != 0:
        print(c("[-]", 'red')+c(" You must be root to run this script", 'red'))
        sys.exit()

def Stress():
    checkroot()
    os.system("clear")
    Logo.logo_14()

    lists = ('dhcpig','funkload','iaxflood','inundator','inviteflood','ipv6toolkit','mdk3','reaver','rtpflood','slowhttptest','t50','termineter','thc-ipv6','thc-ssl-dos')
    
    list_tool(lists)
    print(G("    101. back"))
    print(R("    102. exit"))
    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu in  range(len(lists)):
        menu -= 1
        # Call function
        stress_tool(lists[menu+1])
    elif menu == 101:
        os.system("python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # //usr/bin/
    elif menu == 102:
        exit()
    else:
        print(R('Wrong Input!'))
    input()
    back()

def list_tool(a):
    num = -1
    for x in range(len(a)):
        num += 1
        if os.path.isfile(f'/usr/bin/{a[x]}'):
            print(G(f'[{num}] {a[x]}'))
        else:
            print(R(f'[{num}] {a[x]}'))

#Funciton
# stress tool
def stress_tool(a):
    if os.path.isfile(f"/usr/bin/{a}"):
        os.system("clear")
        print(B("Tools Available"))
    else:
        os.system(
            f'xterm -T "☣ INSTALL {a} ☣" -geometry 100x30 -e "sudo apt install {a}"'
        )
        os.system("clear")
        if os.path.isfile(f"/usr/bin/{a}"):
            print(B(f"{a} Already Installed"))
        else:
            print(R(f"{a} Not Installed"))
    # input()
    # back()
    # end stress tool

def back():
    Stress()

if __name__=='__main__':
    Stress()