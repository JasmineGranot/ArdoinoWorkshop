#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address 77.139.206.49
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        d = input("enter str: ")
        s.sendall(str.encode(d))
        data = s.recv(1024)

        print('Received', str(data))
