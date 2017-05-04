import socket

enchufe = socket.socket()
enchufe.connect(("127.0.0.1",1111))

file = open ("ico.jpg", "rb")
l = file.read(1024)
while (l):
    enchufe.send(l)
    l = file.read(1024)
enchufe.close()