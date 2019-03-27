import socket
import threading
import os

def RetrFile(name, sock):
	filename = sock.recv(1024)

	if filename[:4] == 'list': # list directory
		print "print directory list"
		print "directory path: " + filename[5:]
		filelist = os.listdir(filename[5:])
		print filelist
		sock.send(str(filelist))

	elif os.path.isfile(filename): # list to download image
		sock.send("EXISTS " + str(os.path.getsize(filename)))
		userResponse = sock.recv(1024)
		if userResponse[:2] == 'OK':
			with open(filename, 'rb') as f:
				bytesToSend = f.read(1024)
				sock.send(bytesToSend)
				while bytesToSend != "":
					bytesToSend = f.read(1024)
					sock.send(bytesToSend)
		else:
			sock.send("ERR")
		

	else:
		print "ERRORR!!!"

	sock.close()

def Main():
	host = '127.0.0.1'
	port = 9000

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
	s.bind((host, port))

	s.listen(5)

	print "Server Started."
	while True:
		c, addr = s.accept()
		print "client connected " + str(addr)
		t = threading.Thread(target=RetrFile, args=("retrThread", c))
		t.start()

	s.close()

if __name__ == '__main__':
	Main()