import socket

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 55000))

    a = input()
    sock.send(bytes(a, encoding='UTF-8'))
    data = sock.recv(1024)
    print(data.decode())

    sock.close()