# from requests import get
# print(get('http://stepik.org/favicon.ico').headers['server'])


import socket

host = socket.gethostname() #socket.gethostname() 
port = 2222



req = "Hello TCP"



f=1
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	s.connect((host, port))
	while f != "stop":
		f = input()
		s.send(f.encode())
		rsp= s.recv(1024)


print("done")
