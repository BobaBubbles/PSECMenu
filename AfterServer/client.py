import socket
import pickle
import datetime
end = 0

def getnewsocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cartlist = []
currentday = datetime.datetime.now()

clientsocket = getnewsocket()
clientsocket.connect(('localhost', 8089))

gui = clientsocket.recv(255)
npmenu = clientsocket.recv(4096)
menu = (pickle.loads(npmenu))
nptodmenu = clientsocket.recv(4096)
todmenu = (pickle.loads(nptodmenu))

clientsocket.close()

def printmenu():
    print(f'-----------------------------------------')            
    print('             ', currentday.strftime("%A"), "'s", " menu", sep = '')
    print(f'-----------------------------------------')            
    for i in range(0, len(todmenu), 1):
        print((i + 1), '. ', todmenu[i]['Item'].ljust(25), '$' + todmenu[i]['Pricing'].ljust(25), sep = '')
    print(f'-----------------------------------------') 

def runmenu():
    while True:
        printmenu()
        print(f'\nWhat would you like today?\n')
        try:
            dishselected = input('Enter the dish number to add it to your cart\nEnter x to quit to main menu\n\n>> ')
            if dishselected.isnumeric() == True:
                dishselected = int(dishselected)
            elif dishselected.lower() == 'x':
                break
            else:
                print(f'---------------------------------------------------')
                print(f'{"Please enter a valid input": ^51}')
                print(f'---------------------------------------------------')
                continue
        except ValueError:
            print(f'---------------------------------------------------')
            print(f'{"Please enter a valid input": ^51}')
            print(f'---------------------------------------------------')
            continue
        if (dishselected > len(todmenu) or dishselected < 1):
            print(f'---------------------------------------------------')
            print(f'{"Please enter a valid number": ^51}')
            print(f'---------------------------------------------------')
            continue
        else:
            cartlist.append(todmenu[dishselected-1],)
            print(f'---------------------------------------------------')
            print(todmenu[dishselected-1]['Item'], 'has been added to your cart')
            print(f'---------------------------------------------------')            
            continue

# Search function
def runsearch():
    while True:
        searchlist=[]
        try:
            print(f'-----------------------------------------------------------------------')
            search = input(f'What would you like to search for? Enter x to go back to the main menu\n-----------------------------------------------------------------------\n>> ')
            if search.isnumeric() == True:
                print(f'--------------------------')
                print(f'{"Enter a valid name": ^26}')
                print(f'--------------------------')
            elif search.lower() == 'x':
                break
            else:
                for i in todmenu:
                    if search.lower() in (i['Item']).lower():
                        searchlist.append(i)
                if len(searchlist) == 0:
                    print(f'---------------------------------------------')
                    print(f'{"Nothing in the menu matched your search term.": ^45}')
                    print(f'---------------------------------------------')

                    continue
                else:
                    print('')
                    for j in range(0, len(searchlist), 1):
                        print((j+1), '. ', searchlist[j]['Item'].ljust(25), '$' + searchlist[j]['Pricing'].ljust(25), sep = '')
                    while True:
                        try:
                            addtocart = input('\nEnter item number to add it to the cart or x to search again\n-----------------------------------------------------------------------\n>> ')
                            if addtocart.isnumeric() == True:
                                addtocart = int(addtocart)
                            elif addtocart.lower() == 'x':
                                break
                            else:
                                print(f'--------------------------')
                                print(f'{"Please enter a valid input": ^26}')
                                print(f'--------------------------')
                                continue
                        except ValueError:
                            print(f'--------------------------')
                            print(f'{"Please enter a valid number": ^26}')
                            print(f'--------------------------')
                            continue
                        if (addtocart > len(searchlist) or addtocart < 1):
                            print(f'---------------------------')
                            print(f'{"Please enter a valid number": ^26}')
                            print(f'---------------------------')
                            continue
                        else:
                            cartlist.append(searchlist[addtocart - 1])
                            print(f'{searchlist[addtocart - 1]["Item"]} has been added to your cart!')
                            continue
        except ValueError:
            print(f'---------------------------')
            print(f'{"Enter a valid input": ^26}')
            print(f'---------------------------')
            continue

# Cart function 
def runcart():
    while True:
        total = 0
        if len(cartlist) == 0:
            print(f'\n=================================================================')
            print(f'{"Your cart is empty, please add something to your cart at the menu": ^65}')
            print(f'=================================================================\n')
            break
        else:
            print(f'=============================================')
            for i in range(0, len(cartlist), 1):
                print((i+1), '. ', cartlist[i]['Item'].ljust(25),'$' + cartlist[i]['Pricing'].ljust(25), sep = '')
                total += float(cartlist[i]['Pricing'])
            print(f'=============================================')
            print(f'Your current total price is ${total:.2f}')
            print(f'=============================================')

            try:
                editcart = input(f'Enter item number to remove from cart or x to go back\n>> ')
                if editcart.isnumeric() == True:
                    editcart = int(editcart)
                elif editcart.lower() == 'x':
                    break
                else:
                    print(f'==========================')
                    print(f'{"Enter a valid input": ^26}')
                    print(f'==========================')
                    continue
            except ValueError:
                print(f'==========================')
                print(f'{"Enter a valid input": ^26}')
                print(f'==========================')
                continue
            if (editcart > len(cartlist) or editcart < 1):
                print(f'==========================')
                print(f'{"Please enter a valid number": ^26}')
                print(f'==========================')
                continue
            else:
                del cartlist[editcart - 1]
                continue
        
# Checkout function
def checkout():
    total = 0
    if len(cartlist) == 0:
        print(f'\n ____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ ____')
        print(f'|                                                                     |')
        print(f'| Please add something into your cart before checking out. Thank you! |')
        print(f'|_____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ ___|\n')
    else:
        print(f'=============================================')
        for i in range(0, len(cartlist), 1):
            print((i+1), '. ', cartlist[i]['Item'].ljust(25), '$' + cartlist[i]['Pricing'].ljust(25), sep = '')
            total += float(cartlist[i]['Pricing'])
        print(f'=============================================')
        print(f'Your current total bill is ${total:.2f}')
        print(f'=============================================')
        while True:
            try:
                check = input(f'Enter x to go back to main menu or c to check out\n>> ')
                if check.isnumeric() == True:
                    print(f'==========================')
                    print(f'{"Please enter a valid input": ^26}')
                    print(f'==========================')
                    continue
                elif check.lower() == 'x':
                    break
                elif check.lower() == 'c':
                    print(f'Please pay ${total:.2f} at the counter! Thank you and come again')
                    clientsocket = getnewsocket()
                    clientsocket.connect(('localhost', 8089))
                    clientsocket.send('x'.encode())
                    clientsocket.close()
                    global end
                    end = 1
                    break
                else:
                    print(f'==========================')
                    print(f'{"Please enter x or c only": ^26}')
                    print(f'==========================')
                    continue
            except ValueError:
                print(f'==========================')
                print(f'{"Please enter a valid input": ^26}')
                print(f'==========================')
                continue

# Prints the whole menu
def wholemenu():
    daydict = {
    1:"Monday's Western",
    2:"Tuesday's Korean", 
    3:"Wednesday's Japanese",
    4:"Thursday's Singaporean",
    5:"Friday's Thai",
    6:"Saturday's Malay",
    0:"Sunday's Chinese"
}
    day = 0
    print(f'These are the day specific menus')
    for i in range(0, len(menu), 1):
        if day != int(menu[i]['Day']):
            day = int(menu[i]['Day'])
            print(f'--------------------------------')
            print(daydict[day], 'Menu')
            print(f'--------------------------------')
            print(menu[i]['Item'].ljust(25),'$' + menu[i]['Pricing'].ljust(25), sep = '')
        else:
            print(menu[i]['Item'].ljust(25),'$' + menu[i]['Pricing'].ljust(25), sep = '')

fxdict = {
    1:runmenu,
    2:runsearch,
    3:runcart, 
    4:checkout,
    5:wholemenu
}

while end == 0:
    print(gui.decode())
    try:
        msg = input('Msg to send [x to shutdown server] \n >> ')
        if msg.isnumeric():
            msg = int(msg)
        elif msg.lower() == 'x':
            clientsocket = getnewsocket()
            clientsocket.connect(('localhost', 8089))
            clientsocket.send(msg.encode())
            clientsocket.close()
            break
        else:
            print('Please enter a valid option')
            continue
    except ValueError: 
        print(f'Please enter a valid option')
        continue
    if (msg > len(fxdict) or msg < 1):
        print(f'Please enter a valid number')
        continue
    else:
        while True:
            fxdict[msg]()
            break
        pass