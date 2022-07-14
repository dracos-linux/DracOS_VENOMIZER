
import os
from color import *
import Logo


def Sniffing():
    os.system("clear")
    Logo.logo_13()
    
    lists = ('bettercap','brup','dnschef','fiked','hamster-sidejack','hexinject','iaxflood','inviteflood','ismtp',
    'isr-evilgrade','mitmproxy','ohrwurm','protos-sip','rebind','responder','rtpbreak','rtpinsertsound','sctpscan',
    'siparmyknife','sipp','sipvicious','sniffjoke','sslsplit','thc-ipv6','voiphopper','webscarab','wifi-honey','wireshark',
    'xspy','yersinia','zaproxy')
    list_tool(lists)
    print(G("    101. back"))
    print(R("    102. exit"))
    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu in range(len(lists)):
        # Call function
        sniffing_tool(lists[menu])
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
    Sniffing()


#function
#sniffing tool
def sniffing_tool(a):
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
    input()
    # end sniffing tool
