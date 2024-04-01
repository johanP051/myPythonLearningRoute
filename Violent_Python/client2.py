# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65431  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input("Insert a message: ")
        msg = bytes(msg, 'utf-8')
        s.sendall(msg)
        data = s.recv(1024)

        print(f"Server Received: {data!r}")
        if data == bytes("exit()", 'utf-8'):
                print("Exit message sended")
                break
        else:
            continue