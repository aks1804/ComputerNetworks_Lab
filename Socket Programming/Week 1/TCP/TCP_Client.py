import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully... Please wait...")

PORT = 3124
HOST = socket.gethostname()
s.connect((HOST, PORT))


print("Server connection established...")
data = s.recv(1024)
print(str(data.decode('utf-8')))
s.close()
