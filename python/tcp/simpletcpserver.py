import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 6789))
s.listen(1)
print("Waiting for requests..")
while True:
    conn, addr = s.accept()

    data = conn.recv(65536).decode("utf-8")

    transformed_data = data.strip().upper()[::-1] + "\n"

    conn.sendall(transformed_data.encode("utf-8"))