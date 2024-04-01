# Creating a Client connection to the server
import socket

my_socket = socket.socket()
my_socket.connect(('localhost', 8187))

dataServer = my_socket.recv(1024)
print(dataServer)

#my_socket.send(b"Hi from the Client!!")
msg = input("Insert the msg to the server: ")
my_socket.send(bytes(msg, "utf-8"))

#my_socket.close()
