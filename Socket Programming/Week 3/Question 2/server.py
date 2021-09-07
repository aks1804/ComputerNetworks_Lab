import socket


def myfunc(e):
    return len(e)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


HOST = socket.gethostname()
PORT = 2468

s.bind((HOST, PORT))
s.listen(5)

clientsocket, address = s.accept()
strings = []

while True:
    string = clientsocket.recv(1024).decode("utf-8")
    print("Client's Request : " + str(string))
    if string == "!!":
        break
    else:
        strings.append(string)


clientsocket.send(bytes(
    "\t\tMENU\n1. Sort by length\n2. Sort alphabetically\nEnter Your Choice[1/2]", "utf-8"))
choice = clientsocket.recv(1024).decode("utf-8")

if choice == '1':
    strings.sort(key=myfunc)
elif choice == '2':
    strings.sort()

clientsocket.send(bytes("Sorted strings : " + str(strings), "utf-8"))
clientsocket.close()

print("Client has terminiated the connection...")
s.close()
