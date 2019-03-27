import socket
import os

def Main():
    host = '127.0.0.1'
    port = 9000

    s = socket.socket() # automatically TCP
    s.connect((host, port))

    filename = raw_input("File? -> ")
    s.send(filename)
    if filename[:4] == 'list': # digunakan untuk list isi directory / folder
        userResponse = s.recv(1024)
        print "directory: \n" + str(userResponse)
        
    elif filename[:6] == 'upload':
        print "Uploading File to Server"
        upload_name = filename[7:]
        s.send("SENDING " + str(os.path.getsize(upload_name)))
        with open(upload_name, 'rb') as f:
                bytesToSend = f.read(1024)
                s.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    s.send(bytesToSend)
        f.close()

    else: # digunakan untuk download file
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
            if message == 'Y':
                s.send("OK")
                new_filename = filename.rsplit("/")[-1]
                f = open('client_'+new_filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"

                print "Download Complete!"
                f.close()
        else:
            print "File Does Not Exist!"
    s.close()


if __name__ == '__main__':
    Main()