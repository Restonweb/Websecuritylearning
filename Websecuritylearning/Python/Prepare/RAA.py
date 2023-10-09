import random

from cryptography.hazmat.primitives import hashes
from datetime import datetime
import time
from SM2Enc import sm2Enc
import socket
import threading

sm2 = sm2Enc()


class RAA:
    P = '8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3'
    Kpub = None
    MLEN = 1024
    deltaT = 32767

    def __init__(self):
        self.__RAAkeypair = sm2.get_key()
        self.__kms = self.__RAAkeypair[1]
        self.__Kp = self.__RAAkeypair[0]
        RAA.Kpub = self.__Kp
        self.__networkinit()

    def swhash(self, message):
        Hashcode = hashes.Hash(hashes.SHA512())
        Hashcode.update(message.encode())
        hash_original = Hashcode.finalize().hex()
        hash_moded = int(hash_original, base=16)
        while hash_moded > int(RAA.P, base=16): hash_moded %= int(RAA.P, base=16)
        return hex(hash_moded)

    def Vtimestamp(self, timestamp) -> bool:  # 时间戳验证
        timestamps = timestamp.split('-')
        time_nows = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')  # '%Y-%m-%d-%H-%M-%S' '0-1-2-3-4-5'
        time_now = time_nows.split('-')
        AF = True
        for i in range(5):  # 一分钟内的时间戳视为有效
            if timestamps[i] != time_now[i]:
                AF = False
        return AF

    def Enc(self, key, *mess):  # list arguments
        self.__mess = '||'.join(mess)
        return sm2.sm2_Enc(sm2.get_args(), key, self.__mess)

    def Dec(self, mess):
        self.Dmess = sm2.sm2_Dec(sm2.get_args(), self.__kms, mess)
        self.Dlist = self.Dmess.split('||')
        # print(self.Dlist)
        return self.Dlist

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
            tcp, Caddr = self.tcps.accept()
            NF = False
            print("连接的客户端：", Caddr)
            AreaPk = 'Kpub:' + str(RAA.Kpub)
            tcp.send(AreaPk.encode())
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
            if data.startswith("Reg1:"):
                R1list = self.Dec(data.split(":")[1])
                # print("?", R1list)
                if self.Vtimestamp(R1list[3]):  # 验证成功，计算RID
                    print("\033[32mtimestamp is vaild!\033[0m")
                    client_socket.send("\033[32mTimeStamp is valid!\033[0m".encode())
                    RIDevS = [R1list[0], R1list[1], R1list[2]]
                    RIDev = self.swhash('||'.join(RIDevS))
                    print("Generate RIDev:", RIDev)
                    client_socket.send(f"RIDev:{RIDev}".encode())
                else:  # 验证未成功，发送错误信息
                    print("\033[31mTimestamp is invalid!\033[0m")
                    client_socket.send("Error:TimeStamp is invalid!".encode())
            elif data.startswith("Reg2:"):
                p, a, b, h, G, n = sm2.get_args()
                R2list = self.Dec(data.split(":")[1])
                Bist, Kevist, RIDevst, IDareast = R2list
                kevt = Kevist[1:-1].split(",")
                Kevi = (int(kevt[0]), int(kevt[1]))
                kmult = sm2.multPoint(Kevi, self.__kms, p, a)
                E1 = sm2.bytesTint(sm2.pointTbytes(kmult))
                E2 = eval(RIDevst)
                E3 = E1 ^ E2
                Bi = int(Bist)
                if E3 == Bi:
                    print("\033[32mBi valid!\033[0m")
                    r1 = random.randint(1, p-1)
                    kmultl = sm2.multPoint(Kevi, self.__kms, p, a)
                    E1l = sm2.bytesTint(sm2.pointTbytes(kmultl))
                    E2l = eval(self.swhash(RIDevst))
                    LIDev = E1l ^ E2l
                    r1Kp = sm2.multPoint(RAA.Kpub, r1, p, a)
                    E3t = eval(self.swhash('||'.join([str(r1Kp), str(LIDev), str(RAA.deltaT)])))
                    Fi = E2l ^ E3t
                    SIDev = Fi | RAA.deltaT
                    print(SIDev)
                else:
                    print("\033[31mBi invalid!\033[0m")
                    client_socket.send("Error:Registration Failed!".encode())
# t = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
# print(t)
