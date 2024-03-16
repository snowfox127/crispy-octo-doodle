import socket

# creates socket object
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

host = socket.gethostname() # or just use (host = '')
port = 3000

s.connect((host, port))

tm = s.recv(1024) # msg can only be 1024 bytes long

s.close()
print("Request from port %s" % tm.decode('ascii'))