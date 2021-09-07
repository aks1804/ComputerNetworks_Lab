import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 3000
HOST = socket.gethostname()

s.connect((HOST, PORT))

while True:
    x = input("Client: ")
    s.send(bytes(x, "utf-8"))
    y = str(s.recv(1024).decode('utf-8'))
    print("Message from server: " + y)

s.close()
