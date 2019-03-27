from threading import Thread
import socket
import os
import sys

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9000
FILE_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
server_address = (SERVER_IP, SERVER_PORT)
print >> sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(1)

while True:
    	# Wait for a connection
    	print >>sys.stderr, 'waiting for a connection'
    	connection, client_address = sock.accept()
    	print >>sys.stderr, 'connection from', client_address
    	# Receive the data in small chunks and retransmit it
    	while True:
        	data = connection.recv(32)
        	print >>sys.stderr, 'received "%s"' % data
            	if data:
                	print >>sys.stderr, 'sending data back to the client'
                	connection.sendall('-->'+data)
            	else:
                	print >>sys.stderr, 'no more data from', client_address
                	break
        # Clean up the connection
	connection.close()