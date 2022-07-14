#!/usr/bin/python3
import os
from color import *
import Logo

#
def checkroot():
    if os.geteuid() != 0:
        print(c("[-]", 'red')+c(" You must be root to run this script", 'red'))
        sys.exit()

def InfoGat():
    checkroot()
    os.system("clear")
    Logo.logo_10()

    lists = ('nmap','amap','whatweb','sublist3r','arp-scan','automater','braa','casefile','cisco-torch',
    'dmitry','dnsenum','dnsmap','dnsrecon','dnstracer','dnswalk','python-faraday','fierce','firewalk',
    'fragroute','fragrouter','ghost-phisher','goofile','hping3','inspy','intrace','ismtp','maltego-teeth',
    'masscan','metagoofil','miranda','nikto','ntop','recon-ng','smbmap','smtp-user-enum','snmp-check','sslcaudit','sslsplit')

    list_tool(lists)
    
    print(G('    101. back'))
    print(R("    102. exit"))

    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu in range(len(lists)):
        menu -=1
        # Call function
        info_gathering(lists[menu+1])
    elif menu == 101:
        os.system(f"/usr/bin/DracOS_VENOMIZER/venomizer.py")  # /usr/bin/
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


def info_gathering(a):
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
            print(R(f"Error Installing {a}"))
    input()
        # end info_gathering

# fungsi untuk memanggil lagi InfoGat
# supaya program tidak keluar
def back():
    os.system('clear')
    InfoGat()

if __name__ == '__main__':
    InfoGat()