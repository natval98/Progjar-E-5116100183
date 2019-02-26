import sys
import socket

# Create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect socket to the port where server is listening
server_address = ('localhost', 10000)
print >> sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

'''
try:
	# send data
	message = 'KIRIM DATA'
	print >> sys.stderr, 'sending "%s"' % message
	sock.sendall(message)

	# Look for response
	amount_received = 0
	amount_expected = len(message)
	while amount_received < amount_expected :
		data = sock.recv(16)
		amount_received += len(data)
		print >> sys.stderr, 'received "%s"' % data
finally:
	print >> sys.stderr, 'closing socket'
	sock.close()
'''

while True:
	message = raw_input("== ")
	if not message:
		break
	print >> sys.stderr, 'sending "%s"' % message
	sock.sendall(message)

	# Look for response
	amount_received = 0
	amount_expected = len(message)
	while amount_received < amount_expected :
		data = sock.recv(16)
		amount_received += len(data)
		print >> sys.stderr, 'received "%s"' % data

sock.close()