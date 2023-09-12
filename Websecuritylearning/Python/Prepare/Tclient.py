import socket
import threading
import random
import hashlib

# 生成随机ID
client_id = str(random.randint(1, 1000))

# 连接服务端
server_address = ('localhost', 9696)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)


def receive_data():
    while True:
        data = client_socket.recv(1024).decode()
        if data.startswith("RID:"):
            rid = data.split(":")[1]
            print(f"Received RID: {rid}")
            # 在这里可以进行进一步处理，如保存RID等
        elif data.startswith("AID:"):
            aid = data.split(":")[1]
            print(f"Received AID: {aid}")
            # 在这里可以进行进一步处理，如保存AID等
            send_sid_request(aid)
        elif data.startswith("SID:"):
            sid = data.split(":")[1]
            print(f"Received SID: {sid}")
            # 在这里可以进行进一步处理，如保存SID等
        else:
            print(f"Received: {data}")


def send_register_request():
    request = f"Reg:{client_id}"
    client_socket.send(request.encode())


def send_sid_request(aid):
    # 二次HASH处理
    combined_id = aid + client_id
    sid = hashlib.sha256(combined_id.encode()).hexdigest()
    request = f"SID:{sid}"
    client_socket.send(request.encode())


# 创建接收数据的线程
receive_thread = threading.Thread(target=receive_data)
receive_thread.start()

# 发送注册请求
send_register_request()


# 在客户端主线程中可以继续进行其他操作
print("shit")
