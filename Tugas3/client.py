import socket
import sys

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

while True:
	x = sys.stdin.readline()
	print x
	# sock.sendto(x, (SERVER_IP, SERVER_PORT))
	sock.sendall(x)
	if x == "END\n":
		sock.close()

