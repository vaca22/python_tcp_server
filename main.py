# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345


s.bind(('', port))
print("socket binded to %s" % (port))


s.listen(5)
print("socket is listening")


while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting'.encode())
    c.close()
    break