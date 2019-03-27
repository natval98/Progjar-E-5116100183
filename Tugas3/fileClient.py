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
			print str(userResponse)

		elif filename == 'q':
			s.close()
			break

		else:
			s.send(filename)
	        data = s.recv(1024)
	        if data[:6] == 'EXISTS':
	            filesize = long(data[6:])
	            message = raw_input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
	            if message == 'Y':
	                s.send("OK")
	                f = open('new_'+filename, 'wb')
	                data = s.recv(1024)
	                totalRecv = len(data)
	                f.write(data)
	                while totalRecv < filesize:
	                    data = s.recv(1024)
	                    totalRecv += len(data)
	                    f.write(data)
	                    print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"
	                    print "total: " + str(totalRecv)

	                print "Download Complete!"
	                f.close()
	        else:
	            print "File Does Not Exist!"


if __name__ == '__main__':
	Main()