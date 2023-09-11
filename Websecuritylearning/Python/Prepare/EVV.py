from cryptography.hazmat.primitives import hashes
from datetime import datetime
import time
from SM2Enc import sm2Enc
import socket

sm2 = sm2Enc()


class EV:
    Kevp = None
    MLEN = 1024

    def __init__(self):
        self.__EVkeypair = sm2.get_key()
        self.__kevs = self.__EVkeypair[1]
        self.__kevp = self.__EVkeypair[0]
        EV.Kevp = self.__kevp
        self.__networkinit()


    def Reg(self, IDEV, IDNEV, IDarea):
        return self.Enc('0', IDEV, IDNEV, IDarea)

    def Enc(self, key, *mess):  # list arguments
        self.__mess = '||'.join(mess)
        return sm2.sm2_Enc(sm2.get_args(), key, self.__mess)

    def Dec(self, mess):
        self.Dmess = sm2.sm2_Dec(sm2.get_args(), self.__kevs, mess)
        self.Dlist = self.Dmess.split('||')
        print(self.Dlist)

    def __networkinit(self):
        host = '127.0.0.1'
        port = 9696
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        msg = self.client.recv(EV.MLEN)
        print(msg.decode())
        self.client.send("Hello Server!".encode('utf-8'))

    def closeconnect(self):
        self.client.send("Bye,Server!".encode('utf-8'))
        self.client.close()

    def sendmsg(self):
        msg = input("Input message:")
        self.client.send(msg.encode('utf-8'))