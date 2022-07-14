import os
from color import*
import Logo

def WebApp():
    os.system('clear')
    # Logo
    Logo.logo_16()

    lists = ('apache-users','arachni','bbqsql','blindelephant','burpsuite','cutycapt','davtest','deblaze',
    'dirb','dirbuster','fimap','funkload','gobuster','grabber','hurl','jboss-autopwn','joomscan','jsql',
    'maltego-teeth','nikto','padbuster','paros','parsero','plecost','powerfuzzer','proxystrike','recon-ng',
    'skipfish','sqlmap','sqlninja','sqlsus','ua-tester','uniscan','w3af','webscarab','webshag','webslayer',
    'websploit','wfuzz','whatweb','wpscan','xsser')
    
    list_tool(lists)
    
    print(G("    101. back"))
    print(R("    102. exit"))

    menu = int(input(G("[") + R("DracOS") + G("]select>")))
    if menu in range(len(lists)):
        menu -= 1
        # Call function
        webApp_tool(lists[menu])
    elif menu == 101:
        os.system(f"python3 /usr/bin/DracOS_VENOMIZER/venomizer.py")  # /usr/bin/
    elif menu == 102:
        exit()
    else:
        print(R('Wrong Input!'))
        input()
    back()

# check install
def list_tool(a):
    num = 0
    for x in range(len(a)):
        num += 1
        if os.path.isfile(f'/usr/bin/{a[x]}'):
            print(G(f'[{num}] {a[x]}'))
        else:
            print(R(f'[{num}] {a[x]}'))

#Function
def webApp_tool(a):
    if os.path.isfile(f'/usr/bin/{a}'):
        os.system('clear')
        print(B('tools Available'))

    else:
        os.system(
            f'xterm -T "☣ INSTALL {a} ☣" -geometry 100x30 -e "sudo apt install {a}"'
        )
        os.system('clear')
        if os.path.isfile(f'/usr/bin/{a}'):
            print(B(f'{a} already installed'))
        else:
            print(B(f'{a} users not installed'))
    input()
    back()



def back():
    os.system('clear')
    WebApp()