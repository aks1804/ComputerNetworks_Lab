import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 2468

s.connect((HOST, PORT))

print("To close the connection, enter '!!'")
print("Enter strings: \n")

while True:
    req = input("Message to Server : ")
    s.send(bytes(req, "utf-8"))
    if req == '!!':
        break

print()
choose = input(s.recv(1024).decode("utf-8") + " : ")
s.send(bytes(choose, "utf-8"))
print(s.recv(1024).decode("utf-8"))

s.close()
