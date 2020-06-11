import socket
import csv
import datetime
import pickle 
from functions import printgui

menu = []
todmenu = []

with open("menu.csv", newline="") as csvfile:
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

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 8089))
print('Server starts listening')
serversocket.listen(1)

con, address = serversocket.accept()
con.sendall(printgui().encode())
menu = pickle.dumps(menu)
todmenu = pickle.dumps(todmenu)
con.send(menu)
con.send(todmenu)

while True:
    con, address = serversocket.accept()
    # con.sendall(printgui().encode())
    # menu = pickle.dumps(menu)
    # todmenu = pickle.dumps(todmenu)
    # con.send(menu)
    # con.send(todmenu)
    print('Got a new connection.. Waiting for msg now..')
    buf = con.recv(255)
    # if len(buf) > 0:
    #     print(buf.decode())
    if buf == b'x':
        con.close()
        break
    else:
        con.sendall(printgui().encode())
        con.close()

serversocket.close()
print('Server has stopped')