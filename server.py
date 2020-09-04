# from requests import get
# print(get('http://stepik.org/favicon.ico').headers['server'])


import socket


HOST = socket.gethostname()  #''
PORT = 4000

def recieve_text_data(skt, msg_len):
	msg = ""
	while len(msg) < msg_len:
		chunk = skt.recv(msg_len - len(msg))
		if chunk == '':
			raise RuntimError("Broken")
		# print(type(chunk))
		msg = msg + chunk.decode("utf-8")
	return msg


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))

    s.listen(10)

    conn, addr = s.accept()

    with conn:

        print('Connected by', addr)
        while True:
        	data = recieve_text_data(conn ,1024)
        	print(data)
            # data = conn.recv(1024)
            # print(data)
            # if not data: break

            # conn.sendall(data)

