import socket

def Main():
	host = '127.0.0.1'
	port = 9000

	s = socket.socket() # automatically TCP
	s.connect((host, port))

	while True:
		filename = raw_input("File? -> ") # diisi 'list' atau filename
		if filename == 'list':
			s.send("list")
			userResponse = s.recv(1024)
			print userResponse
		elif filename == 'q':
			s.close()
			break

		else:
			print "else"
			s.send(filename)
			data = s.recv(1024)
			if data[:6] == "EXISTS":
				filesize = long(data[7:])
				message = raw_input("File exists, " + str(filesize) + "Bytes, download? (y/n) -> ")

				if message == 'y' or message == 'Y':
					s.send("OK")
					f = open('new_' + filename, 'wb')
					data = s.recv(1024)

					totalRecv = len(data)
					f.write(data)
					while totalRecv < filesize:
						data = s.recv(1024)
						totalRecv += len(data)
						f.write(data)
						print str(totalRecv) + " of " + str(filesize)
					print "Download Complete!"

			else:
				print "File does not EXISTS"


if __name__ == '__main__':
	Main()