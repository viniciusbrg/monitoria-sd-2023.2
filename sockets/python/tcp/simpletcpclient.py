import socket

PORT = 6789
HOST = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
msg = input("Mensagem: ") + "\n"

s.send(msg.encode("utf-8"))

data = s.recv(65536).decode('utf-8')
s.close()
print('FROM SERVER: \n{s}'.format(s=data))