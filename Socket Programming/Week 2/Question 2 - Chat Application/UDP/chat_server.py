import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()
PORT = 9000
PORT_CLI = 9898

s.bind((HOST, PORT))

while True:
    data, addr = s.recvfrom(1024)
    print("Client's Message : ", str(data.decode("utf-8")))
    x = input("Server's Response : ").strip()
    s.sendto(bytes(x, "utf-8"), (HOST, PORT_CLI))
    if x == "Close":
        break

print("Server Terminiated")
s.close()
