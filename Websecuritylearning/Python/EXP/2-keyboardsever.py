import keyboard, threading, socket, time


class keyboardsever:
    def __init__(self):
        self.MLEN = 25565
        self.__networkinit()

    def __networkinit(self):
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
                print("\n断开的客户端：", client_addr)
                print("等待下一个连接......")
                break
            if not data:
                continue
            print(data)


def main():
    keyboardsever()


if __name__ == '__main__':
    main()
