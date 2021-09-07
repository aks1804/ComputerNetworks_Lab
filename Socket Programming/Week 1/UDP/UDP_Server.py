import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

PORT = 8008
HOST = socket.gethostname()

s.bind((HOST, PORT))

while True:
    data, address = s.recvfrom(4096)
    print(str(data))
    msg = (bytes("Welcome to UDP Server","utf-8"))
    s.sendto(msg, address)
