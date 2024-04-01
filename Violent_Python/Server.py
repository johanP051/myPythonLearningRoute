#Creating a Server

import socket

my_socket = socket.socket()
my_socket.bind(('localhost', 8187))
my_socket.listen(10)

while True:
    connection, address = my_socket.accept() #my_socket.accept() returns a tuple = (host, addr)
    #print(connection, address)

    #Sending a msg to client
    connection.send(b"Hi from the server!!")
    
    #Receiving a msg from the client of 1024 bytes
    dataClient = connection.recv(1024)
    print(dataClient)

    #Closing the connection
    connection.close()
