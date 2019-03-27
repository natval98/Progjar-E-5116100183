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

    elif filename[:6] == 'upload':
        print "Uploading File to Server"
        uploadResponse = sock.recv(1024)
        if uploadResponse[:7] == "SENDING":
            f = open('server_' + filename[7:], 'wb')
            data = sock.recv(1024)
            filesize = long(uploadResponse[8:])
            totalRecv = len(data)
            f.write(data)
            while totalRecv < filesize:
                data = sock.recv(1024)
                totalRecv += len(data)
                f.write(data)
                print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"

            print "Receiving File From Client Complete!"
            f.close()
        else:
            sock.send("ERR")

    elif filename[:8] == 'download' and os.path.isfile(filename[9:]): # list to download
        sock.send("EXISTS " + str(os.path.getsize(filename[9:])))
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(filename[9:], 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
            print "Sending File to Client Complete!"
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