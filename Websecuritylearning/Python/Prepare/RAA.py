"""
SECP256k1
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
import cryptography.exceptions
from datetime import datetime
import time
from SM2Enc import sm2Enc

class RAA:
    P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    Kpub = None
    def __init__(self):
        self.__kms = ec.generate_private_key(ec.SECP256K1)
        self.__Kp = self.__kms.public_key()
        RAA.Kpub = self.__Kp.public_bytes(serialization.Encoding.PEM,serialization.PublicFormat.SubjectPublicKeyInfo)
        
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
        self.__kevs = ec.generate_private_key(ec.SECP256K1)
        self.__kevp =self.__kevs.public_key()
        EV.Kevp = self.__kevp.public_bytes(serialization.Encoding.PEM,serialization.PublicFormat.SubjectPublicKeyInfo)
    
    def Reg(self,IDEV,IDNEV,IDarea):
        #TODO:Get Kpub through network
        loaded_Kpub = serialization.load_pem_public_key()#Load the serialized Public Key
        pass
    
    def Enc(self,key,*mess):
        self.__mess = '||'.join(mess)
        pass
    
ev = EV()
# t = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
# print(t) 