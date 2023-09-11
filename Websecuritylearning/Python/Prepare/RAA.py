
from cryptography.hazmat.primitives import hashes
from datetime import datetime
import time
from SM2Enc import sm2Enc
import socket

sm2 = sm2Enc()

class RAA:
    P = '8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3'
    Kpub = None
    MLEN = 1024
    def __init__(self):
        self.__RAAkeypair = sm2.get_key()
        self.__kms = self.__RAAkeypair[1]
        self.__Kp = self.__RAAkeypair[0]
        RAA.Kpub = self.__Kp
        self.__networkinit()

    def swhash(self,message):
        Hashcode = hashes.Hash(hashes.SHA512())
        Hashcode.update(message)
        hash_original = Hashcode.finalize().hex()
        hash_moded = int(hash_original,base=16)
        while hash_moded > (RAA.P):hash_moded %= RAA.P
        return hex(hash_moded)

    def __networkinit(self):
        host = '127.0.0.1'
        port = 9696
        self.tcps = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcps.bind((host,port))
        self.tcps.listen(10)
        NFLAG = True
        while True:
            if NFLAG:
                print("服务器启动，等待连接...")
            elif not NFLAG:
                print("服务器等待下一个连接中...")
            tcp,addr = self.tcps.accept()
            NFLAG = False
            print("连接的客户端：",addr)
            tcp.send("Hello Client!".encode('utf-8'))
            while True:
                data = tcp.recv(RAA.MLEN)
                if data:
                    print("收到客户端的消息:", data)
                if not data:
                    print("断开的客户端：", addr)
                    break
        tcp.close()

    def closeconnect(self):
        self.tcps.close()
        print("服务器已关闭。")

ra = RAA()



ev = EV()
Emess =  ev.Reg('114514','114514','2')
ev.Dec(Emess)
# t = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
# print(t) 