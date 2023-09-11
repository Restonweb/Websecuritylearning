import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9696
client.connect((host,port))

msg = client.recv(1024)
print(msg)
client.send("Hello!,Server!".encode('utf-8'))
client.close()
