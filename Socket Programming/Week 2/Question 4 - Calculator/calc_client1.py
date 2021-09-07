import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


HOST = socket.gethostname()
PORT = 3500

s.connect((HOST, PORT))


while True:
    req = input("Expression to be evaluated : ")
    s.send(bytes(req, "utf-8"))
    res = s.recv(1024).decode("utf-8")
    print("Server's Answer: " + str(res))

s.close()
