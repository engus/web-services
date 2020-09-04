import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '0.0.0.0' #socket.gethostname()  #''
PORT = 2222

server_address = (HOST, PORT)


sock.bind(server_address)

sock.listen(10)

while True:
	# print("wating for connection")
	connection, client_address = sock.accept()
	try:
		# print("connection from", client_address)
		while True:
			data = connection.recv(1024)
			if not data or data.decode("utf-8") == "close":
				break
			print(data.decode("utf-8"))
			connection.sendall(data)
	finally:
		connection.close()
		print("connection closed")