import socket
import sys

msg = "testeeeeeeet"
HOST = "127.0.0.1"
PORT = 6789
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(1)

try:
    s.sendto(bytes(msg, 'utf-8'), (HOST, PORT))

    data, address = s.recvfrom(1024)
    response_data = data.decode("utf-8")
    print(response_data)

    s.close()
except:
    print("Tempo excedido")
