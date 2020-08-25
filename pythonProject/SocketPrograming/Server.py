import socket

#step 1 - Declare a server socket
s = socket.socket();
print("Socket Created")

#step 2 - bind socket
s.bind(("localhost",9999))

#step 3 - start listening and mention # of connection eg. 3
s.listen(3)

#step 4 wait indefinately for incoming connection
while True:
    #step 5, create client socket and store address
    c, addr = s.accept()
    #step 6 - get data from client
    name = c.recv(1024).decode()

    print("Client connected, address - ", addr, name)

    #step 7 - send data to client
    c.send(bytes("Hello " + name,'utf8'))
    #step 8 - close connection
    c.close()
