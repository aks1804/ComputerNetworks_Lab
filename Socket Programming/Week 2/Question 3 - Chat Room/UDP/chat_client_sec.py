import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()
PORT = 5000

s.bind((HOST, PORT))

target = (HOST, 3000)

while True:
    req = input("Message to Server : ")
    s.sendto(bytes(req, "utf-8"), target)
    res, address = s.recvfrom(1024)
    res = res.decode("utf-8")
    print("Server's Response : " + str(res))

s.close()
