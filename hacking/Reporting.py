import os
from color import*
import Logo

def Report():
    os.system("clear")
    Logo.logo_21()

    lists = ('casefile','cherrytree','cutycapt','dos2unix','dradis','magic-tree','metagoofil','nipper-ng','pipal','rdpy')
    
    list_tool(lists)
    print(G('   101. back'))
    print(R('   102. exit'))
    
    menu = int(input(G("[")+R("DracOS")+G("]select> ")))
    if menu in  range(len(lists)):
        menu -= 1
        # Call Function
        reporting_tools(list[menu])
    elif menu == 101:
        os.system('python3 /usr/bin/DracOS_VENOMIZER/venomizer.py')
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

#Function
#CaseFile
def reporting_tools(a):
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
        back()
    # end CaseFile


def back():
    Report()