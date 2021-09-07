import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 3124
HOST = socket.gethostname()
s.bind((HOST, PORT))

s.listen(5)

while True:
    print("Server idle...")
    clientsocket, address = s.accept()
    print(f"Client at {address} has been established")
    msg = "Welcome to the server"
    clientsocket.send(bytes(msg, 'utf-8'))
