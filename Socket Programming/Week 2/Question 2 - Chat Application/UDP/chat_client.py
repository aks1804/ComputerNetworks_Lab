import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()
PORT = 9898
PORT_SER = 9000

s.bind((HOST, PORT))

while True:
    s.sendto(bytes(input("Message To Server : ").strip(), "utf-8"), (HOST, PORT_SER))
    data, addr = s.recvfrom(1024)
    if bytes("Close", "utf-8") == data:
        break
    print("Server's Response: " + data.decode("utf-8"))

print("Client has logged off...")
s.close()
