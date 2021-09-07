import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


HOST = socket.gethostname()
PORT = 7890

s.bind((HOST, PORT))
s.listen(5)

clientsocket, address = s.accept()

while True:
    string = clientsocket.recv(1024).decode("utf-8")
    print("Client's Request : " + str(string))
    if string == "Bye":
        clientsocket.send(bytes("Bye", "utf-8"))
        break
    else:
        clientsocket.send(bytes(string.upper(), "utf-8"))
clientsocket.close()
print("Client has closed the connection to the server...")


s.close()
