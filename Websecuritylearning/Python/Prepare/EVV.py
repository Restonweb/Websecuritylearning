from cryptography.hazmat.primitives import hashes
from datetime import datetime
import time
from SM2Enc import sm2Enc
import socket
import threading

sm2 = sm2Enc()


class EV:
    Kevp = None
    MLEN = 1024
    Kpub = None
    RIDev = None
    def __init__(self):
        self.__EVkeypair = sm2.get_key()
        self.__kevs = self.__EVkeypair[1]
        self.__kevp = self.__EVkeypair[0]
        EV.Kevp = self.__kevp
        self.__networkinit()

    def Reg(self, IDEV, IDNEV, IDarea):
        while True:
            if EV.Kpub is None:  # 等待RA发送区域公钥Kpub
                continue
            elif EV.Kpub is not None:
                t = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
                # ts = "2023-09-12-12-57-10"
                print("----------Ready to progress Registration,Current UTC time is <{time}>----------".format(time=t))
                reg1 = "Reg1:" + self.Enc(EV.Kpub, IDEV, IDNEV, IDarea, t)
                print(reg1)
                self.client.send(reg1.encode())
                break

    def Enc(self, key, *mess):  # list arguments
        self.__mess = '||'.join(mess)
        return sm2.sm2_Enc(sm2.get_args(), key, self.__mess)

    def Dec(self, mess):
        self.Dmess = sm2.sm2_Dec(sm2.get_args(), self.__kevs, mess)
        self.Dlist = self.Dmess.split('||')
        # print(self.Dlist)
        return self.Dlist

    def __networkinit(self):
        host = '127.0.0.1'
        port = 9696
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        receive_thread = threading.Thread(target=self.__receivedata)
        receive_thread.start()

    def __receivedata(self):
        while True:
            data = self.client.recv(self.MLEN).decode()
            if data.startswith("Kpub:"):
                ktemp = data.split(':')[1]
                print("Received Kpub:", ktemp)
                ltemp = ktemp[1:-1].split(',')
                EV.Kpub = (int(ltemp[0]), int(ltemp[1]))
            elif data.startswith("RIDev:"):
                EV.RIDev = data.split(":")[1]
                print(f"Received RIDev:{EV.RIDev}")
                # 计算Bi
            elif data.startswith("Error:"):
                Error = data.split(':')[1]
                raise Exception(f"Error:{Error}")
            elif data:
                print("Received data:", data)

# t = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
# print(t)
