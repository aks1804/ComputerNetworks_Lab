import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client Created Successfully")

PORT = 1234
HOST = socket.gethostname()

s.connect((HOST, PORT))

date = s.recv(1024)

print("Today's Date from server is: " + str(date.decode('utf-8')))
s.close()
