import socket
import threading
import random
import hashlib

# 生成随机ID
server_id = str(random.randint(1001, 2000))

# 创建Socket服务器
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9696)
server_socket.bind(server_address)
server_socket.listen(5)


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        if data.startswith("Reg:"):
            client_id = data.split(":")[1]
            # 连接并HASH生成RID
            combined_id = server_id + client_id
            rid = hashlib.sha256(combined_id.encode()).hexdigest()
            response = f"RID:{rid}"
            client_socket.send(response.encode())
            sendaid(server_id)
        elif data.startswith("SID:"):
            sid = data.split(":")[1]
            print(f"Received SID: {sid}")
            # 在这里可以进行进一步处理，如保存SID等
        else:
            print(f"Received: {data}")
            # 在这里可以处理其他请求

def sendaid(serverid):
    aid = hashlib.sha256(serverid.encode()).hexdigest()
    response = f"AID:{aid}"
    client_socket.send(response.encode())


while True:
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
