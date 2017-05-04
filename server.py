import socket

enchufe = socket.socket()
enchufe.bind(("127.0.0.1",1111))

enchufe.listen(1) # Acepta hasta 10 conexiones entrantes.

while True:
	conn, addr = enchufe.accept()

	print addr
	i=1
	file = open('file_'+ str(i)+".jpg",'wb') #open in binary
	i=i+1
	while (True):       
	# recibimos y escribimos en el fichero
		l = conn.recv(1024)
		while (l):
			file.write(l)
			l = conn.recv(1024)
	file.close()
	conn.close()
enchufe.close()