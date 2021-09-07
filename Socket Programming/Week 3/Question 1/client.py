import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



HOST = socket.gethostname()
PORT = 7890

s.connect((HOST, PORT))

print("To close the connection, enter 'Bye'")


while True:
    msg = input("Message to Server : ")
    s.send(bytes(msg, "utf-8"))
    resp = s.recv(1024).decode("utf-8")
    print("Server's Response : " + str(resp))
    if resp == "Bye":
        print("Client has sucessfully signed off...")
        break

s.close()
