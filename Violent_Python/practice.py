import pandas as pd
import numpy as np
import socket

data = {
    "names": ['Johan', "Sebas"],
    "ages": ["18", "25"]
}
df = pd.DataFrame(data, index=[1, 2])

print(df)

s = socket.socket()
s.listen()
HOST = 'localhost'
PORT = 8080

s.bind(HOST, PORT)

while True:
    connection, addr = s.accept()
    print(f"Connected from: {addr}")
    msg_Server = input("Insert a message for the client: ")
    connection.send(msg_Server)
    msg_Client = connection.recv(1024)