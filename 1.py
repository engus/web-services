# from requests import get
# print(get('http://stepik.org/favicon.ico').headers['server'])


import socket

# host = socket.gethostname() 
# print(host)
req = "Hello TCP"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect(('127.0.0.1', 4000))
	s.send(req.encode())
	rsp= s.recv(1024)

# s.close()