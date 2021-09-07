import socket
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created Successfully")


HOST = socket.gethostname()
PORT = 1234

s.bind((HOST, PORT))

s.listen(10)

while True:
    clientsocket, address = s.accept()
    print(f"Connection From {address} has been esablished...")
    clientsocket.send(bytes(str(datetime.now()), "utf-8"))
    clientsocket.close()
