import socket

ip = socket.gethostname()
port = 1234
buffersize = 2000

skt = socket.socket()
skt.bind((ip, port))
skt.listen()

print("The server is ready!")

con, addr = skt.accept()
print(f"The client address is {addr}")
data = con.recv(buffersize).decode(encoding="UTF-8")
print(f"The received data is {data}")
