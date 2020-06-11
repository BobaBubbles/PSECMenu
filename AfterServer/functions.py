def printgui():
    text = ('------------------------\n' 
    + 'Welcome to the SPAM menu\n'
    + '------------------------\n'
    + "1. Display Today's Menu\n"
    + "2. Search Menu\n"
    + "3. Display Cart\n"
    + "4. Check Out\n"
    + '5. View daily menus\n'
    + 'x. Quit\n'
    + '-------------------------')
    return text

def printmenu():
    print(f'-----------------------------------------')            
    print('             ', currentday.strftime("%A"), "'s", " menu", sep = '')
    print(f'-----------------------------------------')            
    for i in range(0, len(todmenu), 1):
        print((i+1), '. ', todmenu[i]['Item'].ljust(25), '$' + todmenu[i]['Pricing'].ljust(25), sep = '')
    print(f'-----------------------------------------')            
