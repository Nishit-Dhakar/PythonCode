import socket

#step 1 - create client socket
c= socket.socket()

#step 2 - bind to server socket
c.connect(("localhost",9999))

#step 3 - get data from user
name = input("Enter Name - ")

c.send(bytes(name,'utf8'))

#step 4 - get data from server
print(c.recv(1024).decode())
