import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

HOST = socket.gethostname()
PORT = 8008

msg = "Hello UDP Server"
s.sendto(bytes(msg,'utf-8'),(HOST, PORT))

data, address = s.recvfrom(4096)

print("Server responed with...")
print(str(data.decode()))

s.close()
