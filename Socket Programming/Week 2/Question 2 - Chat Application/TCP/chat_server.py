import socket
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 3000
HOST = socket.gethostname()


s.bind((HOST, PORT))

s.listen(10)

clientsocket, address = s.accept()
print(f"Connection From {address} has been established")

while True:
    print("Message from client: " + str(clientsocket.recv(1024).decode('utf-8')))
    x = input("Server: ")
    clientsocket.send(bytes(x, "utf-8"))
    if x == "Close":
        break

print("Chat Application Closed")
clientsocket.close()
s.close()
