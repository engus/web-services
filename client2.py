import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '0.0.0.0' #socket.gethostname()  #''
PORT = 2222

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (HOST, PORT)

sock.connect(server_address)

message = ""

try:
	while message != "close":
		message = input()
		print(message)
		sock.sendall(message.encode())

		amount_recieved = 0
		amount_expected = len(message.encode())

		while amount_recieved < amount_expected:
			data = sock.recv(1024)
			amount_recieved+= len(data.decode("utf-8"))
finally:
	print("closing socket")
	sock.close()
