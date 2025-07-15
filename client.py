import socket

port = 1234
ip = socket.gethostname()

skt = socket.socket() #helps with redundancy
skt.connect((ip, port))

message = "Hello, there! I'm from the client side. 🚫"
skt.send(message.encode("UTF-8"))
skt.close()
