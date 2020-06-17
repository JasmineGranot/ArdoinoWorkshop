#!/usr/bin/env python3
import server_side.handle_request as r
import socket
import server_side

HOST = '192.168.1.13'  # Standard loopback interface address (localhost) 192.168.1.4
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    print("disconnected")
                    break
                data = r.handle_request(data)
                if data:
                    conn.sendall(str.encode(str(data)))
                else:
                    conn.sendall(b"oh no")





