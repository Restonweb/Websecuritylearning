import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9696
server.bind((host, port))
server.listen(5)

while True:
    client, addr = server.accept()
    print("连接地址：", str(addr))
    msg = "Hello! Client!"
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)
    if not data:
        break
    print(data.decode())
server.close()