import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 2345

s.connect((HOST, PORT))


while True:
    req = input("Message to server : ")
    s.send(bytes(req, "utf-8"))
    res = s.recv(1024).decode("utf-8")
    print("Server's Response : " + str(res))

s.close()
