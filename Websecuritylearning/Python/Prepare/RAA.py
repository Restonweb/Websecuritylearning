
from cryptography.hazmat.primitives import hashes
from datetime import datetime
import time
from SM2Enc import sm2Enc

sm2 = sm2Enc()

class RAA:
    P = '8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3'
    Kpub = None
    def __init__(self):
        self.__RAAkeypair = sm2.get_key()
        self.__kms = self.__RAAkeypair[1]
        self.__Kp = self.__RAAkeypair[0]
        RAA.Kpub = self.__Kp
        
    def swhash(self,message):
        Hashcode = hashes.Hash(hashes.SHA512())
        Hashcode.update(message)
        hash_original = Hashcode.finalize().hex()
        hash_moded = int(hash_original,base=16)
        while hash_moded > (RAA.P):hash_moded %= RAA.P
        return hex(hash_moded)

ra = RAA()

class EV:
    Kevp = None
    def __init__(self):
        self.__EVkeypair = sm2.get_key()
        self.__kevs = self.__EVkeypair[1]
        self.__kevp =self.__EVkeypair[0]
        EV.Kevp = self.__kevp

    #TODO:Get Kpub through network
    
    def Reg(self,IDEV,IDNEV,IDarea):
        return self.Enc(ra.Kpub,IDEV,IDNEV,IDarea)
        
    
    def Enc(self,key,*mess):#list arguments
        self.__mess = '||'.join(mess)
        return sm2.sm2_Enc(sm2.get_args(),key,self.__mess)
    
    def Dec(self,mess):
        self.Dmess = sm2.sm2_Dec(sm2.get_args(),self.__kevs,mess)
        self.Dlist = self.Dmess.split('||')
        print(self.Dlist)
ev = EV()
Emess =  ev.Reg('114514','114514','2')
ev.Dec(Emess)
# t = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
# print(t) 