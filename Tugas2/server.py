from threading import Thread
import socket
import os

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9000
FILE_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
server_address = (SERVER_IP, SERVER_PORT)
sock.bind(server_address)

imagenames = ["birthday.jpg", "cupcake.jpg", "pie.jpg"]

def sendImage(CLIENT_IP, CLIENT_PORT):
	addr = (CLIENT_IP, CLIENT_PORT)
	sock.sendto("START", (addr))
	for image_name in imagenames:
		image_size = os.stat(image_name).st_size
		sock.sendto("SEND {}" .format(image_name), (addr))

		fp = open(image_name,'rb')
		k = fp.read()
		x_size = 0

		for x in k:
			sock.sendto(x, (addr))
			x_size = x_size + 1
   			print "\r terkirim {} of {} " . format(x_size ,image_size)

   		sock.sendto("FINISH", (addr))
   		fp.close()

   	sock.sendto("END", (addr))



while True:
	data, addr = sock.recvfrom(1024) # maximum size of data
	print "Receiving: " + str(data)
	if str(data) == "READY":
		thread = Thread(target=sendImage, args=(addr))
		thread.start()
	


