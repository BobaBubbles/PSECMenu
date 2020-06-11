import csv
import datetime

# Variables and lists
menu=[]
todmenu = []
cartlist=[]
end = 0

# Import all the items in the excel file
with open("Assignment/menu.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        menu.append(dict(row))

# Gets today's day and filters the menu
# "%w" gets the current day as a number
# 1 - Monday
# 2 - Tuesday
# 3 - Wednesday
# 4 - Thursday
# 5 - Friday
# 6 - Saturday
# 0 - Sunday
currentday = datetime.datetime.now()
y = currentday.strftime("%w")
todmenu[:] = [i for i in menu if i.get('Day') == currentday.strftime("%w")]

# Start of functions
# Prints the GUI
def printgui():
    print(f'------------------------')
    print(f'Welcome to the SPAM menu')
    print(f'------------------------\n')
    print(f"1. Display Today's Menu")
    print(f"2. Search Menu")
    print(f"3. Display Cart")
    print(f"4. Check Out")
    print(f'5. View daily menus')
    print(f'x. Quit')
    print(f'-------------------------')

# Prints the items on the menu
# "%A" Gets the day as the name of the day as a string
def printmenu():
    print(f'-----------------------------------------')            
    print('             ', currentday.strftime("%A"), "'s", " menu", sep = '')
    print(f'-----------------------------------------')            
    for i in range(0, len(todmenu), 1):
        print((i+1), '. ', todmenu[i]['Item'].ljust(25), '$' + todmenu[i]['Pricing'].ljust(25), sep = '')
    print(f'-----------------------------------------')            


# Menu function
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


# Dict that contains all the functions
fndict = {
    1:runmenu,
    2:runsearch,
    3:runcart, 
    4:checkout,
    5:wholemenu
}

# Start of program
while end == 0:
    printgui()
    try:
        choice = input('\nEnter your choice here: \n>> ')
        if choice.isnumeric() == True:
            choice = int(choice)
        elif choice.lower() == 'x':
            break
        else:
            print(f'Please enter a valid option')
            continue
    except ValueError:
        print(f'Please enter a valid option')
        continue
    if (choice > len(fndict) or choice < 1):
        print(f'\nPlease enter a valid number')
        continue
    else:
        while True:
            fndict[choice]()
            break
        pass
