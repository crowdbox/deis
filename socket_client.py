# Echo client program
import socket
import sys

HOST = 'deis-controller.local'    # The remote host
PORT = 9000              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall("do")
s.sendall("\r\n")

while True:
    data = s.recv(1024)
    sys.stdout.write(data)
    if not data: break
s.close()
