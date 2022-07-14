#!/usr/bin/python3

import os
from color import *
import Logo

def Forensics():
    os.system("clear")
    Logo.logo_18()

    lists = ('binwalk','bulk_extractor','capstone','chntpw','cuckoo','dc3dd','ddrescue','dff','distorm3',
    'dumpzilla','extundelete','foremost','galleta','guymager','iphonebackupanalyzer','p0f','pdf-parser',
    'pdfid','pdgmail','peepdf','regripper','volatility','xplico')
    
    list_tool(lists)
    
    print(G('    101. Back to Main Menu'))
    print(R("    102. exit"))

    menu = int(input(G("[") + R("DracOS") + G("]select>")))

    if menu in range(len(lists)):
        menu -= 1
        # Call function
        tool_forensic(lists[menu])
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
    os.system('clear')
    Forensics()

#Function
#tool forensic
def tool_forensic(a):
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
            print(R(f"Not Installing {a}"))
    input()
    # back()
    # end tool forensic