from gmssl import sm3
import random
from math import ceil,gcd,log

class sm2Enc:
    
    def intTbytes(self,x,k):
        if pow(256,k) <= x:
            raise Exception("IntToBytes Error:Length k is to short!")
        h = hex(x)[2:].rjust(2*k,'0')[:2 * k] #Hex string:double length
        bytestring = b''
        for i in range(k):
            bytestring += bytes([eval('0x' + h[2*i:2*i+2])])
        return bytestring
    
    def bytesTint(self,s):
        l = len(s)
        integer = 0
        for i in range(l-1,-1,-1):
            integer += pow(256,l-1-i) * s[i] #base 2^8
        return integer
    
    def bitsTbytes(self,s):
        k = ceil(len(s)/8)          
        s = s.rjust(k*8,'0')           
        M = b''         
        for i in range(k):
            M = M + bytes([eval('0b' + s[i*8: i*8+8])])
        return M
    
    def bytesTbits(self,s):
        bitslist = []
        for i in s:
            bitslist.append(bin(i)[2:].rjust(8, '0'))
        s = ''.join(bitslist)
        return s
    
    def fEleTbytes(self,x):
        q = eval('0x' + '8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3')
        u = ceil(log(q, 2))
        l = ceil(u/8) #sm2 document indicate that field element convert to bytes length is ceil(ceil(log(q, 2)/8))
        return self.intTbytes(x,l)
    
    def bytesTfEle(self,x):
        self.bytesTint(x)
        
    def fEleTint(self,x):
        return x
    
    def pointTbytes(self,p):#p is tuple
        xp,yp = p[0],p[1]
        x = self.fEleTbytes(xp)
        y = self.fEleTbytes(yp)
        PC = bytes([0x04]) #PointCompression = 0x04(Not Compressed)
        s = PC + x + y
        return s
        
    def bytesTpoint(self,s):
        if len(s) % 2 == 0:
            raise Exception("Compress Error:String must be NONE COMPRESSED")
        l = (len(s) - 1) // 2
        PC = s[0]
        if PC != 4:
            raise Exception("PC Error:PC must be b'04")
        x = s[1:l+1]
        y = s[l+1:2*l+1]
        xp = self.bytesTfEle(x)
        yp = self.bytesTfEle(y)
        P = (xp,yp)
        return P
    
    #Addtional datatype convert
    def fEleTbits(self,x):
        xby = self.fEleTbytes(x)
        xbi = self.bytesTbits(xby)
        return xbi

    def pointTbits(self,p):
        pby = self.pointTbytes(p)
        pbi = self.bytesTbits(pby)
        return pbi
    
    def intTbits(self,x):
        xby = bin(x)[2:]
        k = ceil(len(xby)/8)
        xbi = xby.rjust(8*k,'0')
        return xbi
    
    def bytesThex(self,s):
        hexlist = []
        for i in s:
            e = hex(i)[2:].rjust(2,'0')
            hexlist.append(e)
        hexr = ''.join(hexlist)
        return hexr
    
    def bitsThex(self,s):
        sby = self.bitsTbytes(s)
        she = self.bytesThex(sby)
        return she
    
    def hexTbits(self,s):
        bitslist = []
        for i in s:
            bbi = bin(eval('0x'+ i))[2:].rjust(4,'0')
            bitslist.append(bbi)
        bitsstring = ''.join(bitslist)
        return bitsstring
    
    def hexTbytes(self,s):
        hbi = self.hexTbits(s)
        hby = self.bitsTbytes(hbi)
        return hby
    
    def fEleThex(self,x):
        xby = self.fEleTbytes(x)
        xhe = self.bytesThex(xby)
        return xhe
    
    def KDF(self,s,klen):#Key Derivation Function 666 This function hao niu b
        O = 256
        if klen >= (pow(2,32) -1) * O:
            raise Exception("KDF Error:Please Check The length of klen!")
        ct = 0x00000001
        if klen % O == 0:
            l = klen // O 
        else:
            l = klen // O + 1
        ha = []
        for i in range(l):
            m = s + self.intTbits(ct).rjust(32,'0')
            mby = self.bitsTbytes(m)
            mlist = [i for i in mby]
            hash_hex = sm3.sm3_hash(mlist)#Use sm3 hash 支持国产
            hash_bin = self.hexTbits(hash_hex)
            ha.append(hash_bin)
            ct += 1
        if klen % O != 0:
            ha[-1] = ha[-1][:klen - O*(klen//O)]
        k = ''.join(ha)
        return k
    
    def modInverse(self,a,b):#逆元
        if gcd(a,b) != 1:
            return None
        u1,u2,u3 = 1,0,a
        v1,v2,v3 = 0,1,b
        while v3 != 0:
            q = u3 // v3
            v1,v2,v3,u1,u2,u3 = (u1 - q * v1),(u2 - q * v2),(u3 - q * v3),v1,v2,v3
        return u1 % b
    
    def fracTint(self,nume,deno,p):#Fractional Mod分数模运算
        num = gcd(nume,deno)
        nume //= num
        deno //= num #约分
        return nume * self.modInverse(deno,p) % p
    
    def pointAdd(self,P,Q,p):
        if P == 0:
            return Q
        if Q == 0:
            return P
        x1,y1,x2,y2 = P[0],P[1],Q[0],Q[1]
        e = self.fracTint(y2 - y1,x2 - x1,p)
        x3 = (e*e - x1 - x2) % p
        y3 = (e*(x1 - x3) - y1) % p
        ans = (x3,y3)
        return ans
    
    def doublePoint(self,P,p,a):#a is parameter of EC
        if P == 0:
            return P
        x1,y1 = P[0],P[1]
        e = self.fracTint(3 * x1 * x1 + a,2 * y1,p)
        x3 = (e*e - 2 * x1) % p
        y3 = (e*(x1 - x3) - y1) % p
        Q = (x3,y3)
        return Q
    
    def multPoint(self,P,k,p,a):
        s = bin(k)[2:]
        Q = 0
        for i in s:
            Q = self.doublePoint(Q,p,a)
            if i == '1':
                Q = self.pointAdd(P,Q,p)
        return Q
    
    def isOnCurve(self,args,P):
        p,a,b,h,G,n = args
        x,y = P
        if pow(y,2,p) == ((pow(x,3,p)+ a*x + b) % p):
            return True
        return False
    
    def sm2_Enc(self,args,PB,M):
        p,a,b,h,G,n = args
        M_bytes = bytes(M,encoding='ascii')
        k = random.randint(1,n-1)
        # k_hex = hex(k)[2:]
        C1 = self.multPoint(G,k,p,a)
        C1_bits = self.pointTbits(C1)
        S = self.multPoint(PB,h,p,a)
        if S == 0:
            raise Exception("Caculation Error:Caculated Point is infinity far!")
        x2,y2 = self.multPoint(PB,k,p,a)#good
        x2_bits = self.fEleTbits(x2)
        y2_bits = self.fEleTbits(y2)
        M_hex = self.bytesThex(M_bytes)
        klen= 4 *len(M_hex)
        t = self.KDF(x2_bits + y2_bits,klen)
        if eval('0b' + t) == 0:
            raise Exception("KDF ERROR:Please check KDF algorithm!")
        # t_hex = self.bitsThex(t)
        C2 = eval('0x' + M_hex + '^' + '0b' + t)
        x2_bytes = self.bitsTbytes(x2_bits)
        y2_bytes = self.bitsTbytes(y2_bits)
        hash_list = [i for i in x2_bytes + M_bytes + y2_bytes]
        C3 = sm3.sm3_hash(hash_list)
        C1_hex = self.bitsThex(C1_bits)
        C2_hex = hex(C2)[2:]
        C3_hex = C3
        C_hex = C1_hex + C2_hex + C3_hex
        print("Encrypt message:",C_hex)
        return C_hex

    def sm2_Dec(self,args,SB,C):
        p,a,b,h,G,n = args
        l = ceil(log(p,2)/8)
        bytes_l1 = 2*l+1
        hex_l1 = bytes_l1 * 2
        C_bytes = self.hexTbytes(C)
        print("将十六进制密文串转换为字节串是：", C_bytes)
        C1_bytes = C_bytes[0:2*l+1]
        print("从密文字节串中取出的C1的字节串是：", C1_bytes)
        C1 = self.bytesTpoint(C1_bytes)
        print("将C1字节串转换为椭圆曲线上的点是：", C1)
        if not self.isOnCurve(args,C1):
            raise Exception("Point Error:C1 Point is not on the EC!")
        x1,y1 = C1[0],C1[1]
        x1_hex,y1_hex = self.fEleThex(x1),self.fEleThex(y1)
        S = self.multPoint(C1,h,p,a)
        if S == 0:
            raise Exception("Caculation Error:Caculated Point is infinity far!")
        xS,yS = S[0],S[1]
        xS_hex,yS_hex = self.fEleThex(xS),self.fEleThex(yS)
        temp = self.multPoint(C1,SB,p,a)
        x2,y2 = temp[0],temp[1]
        x2_hex,y2_hex = self.fEleThex(x2),self.fEleThex(y2)
        hex_l3 = 64
        hex_l2 = len(C) - hex_l1 - hex_l3
        klen = hex_l2 * 4
        x2_bits,y2_bits = self.hexTbits(x2_hex),self.hexTbits(y2_hex)
        t = self.KDF(x2_bits + y2_bits,klen)
        if eval('0b' + t) == 0:
            raise Exception("KDF ERROR:Please check KDF algorithm!")
        t_hex = self.bitsThex(t)
        C2_hex = C[hex_l1:-hex_l3]
        M1 = eval('0x' + C2_hex + '^' +'0x' + t_hex)
        M1_hex = hex(M1)[2:].rjust(hex_l2,'0')
        M1_bits = self.hexTbits(M1_hex)
        cmp_bits = x2_bits + M1_bits + y2_bits
        cmp_bytes = self.bitsTbytes(cmp_bits)
        cmp_list = [i for i in cmp_bytes]
        u = sm3.sm3_hash(cmp_list)
        C3_hex = C[-hex_l3:]
        if u != C3_hex:
            raise Exception("Hash Error:Hash match failed!")
        M_bytes = self.hexTbytes(M1_hex)
        M = str(M_bytes,encoding='ascii')
        print("Decryption Message:",M)
        return M
        
    def get_args(self):
        p = eval('0x' + '8542D69E 4C044F18 E8B92435 BF6FF7DE 45728391 5C45517D 722EDB8B 08F1DFC3'.replace(' ', ''))
        a = eval('0x' + '787968B4 FA32C3FD 2417842E 73BBFEFF 2F3C848B 6831D7E0 EC65228B 3937E498'.replace(' ', ''))
        b = eval('0x' + '63E4C6D3 B23B0C84 9CF84241 484BFE48 F61D59A5 B16BA06E 6E12D1DA 27C5249A'.replace(' ', ''))
        h = 1
        xG = eval('0x' + '421DEBD6 1B62EAB6 746434EB C3CC315E 32220B3B ADD50BDC 4C4E6C14 7FEDD43D'.replace(' ', ''))
        yG = eval('0x' + '0680512B CBB42C07 D47349D2 153B70C4 E5D7FDFC BFA36EA1 A85841B9 E46E09A2'.replace(' ', ''))
        G = (xG, yG)            # G 是基点
        n = eval('0x' + '8542D69E 4C044F18 E8B92435 BF6FF7DD 29772063 0485628D 5AE74EE7 C32E79B7'.replace(' ', ''))
        args = (p, a, b, h, G, n)           # args是存储椭圆曲线参数的元组。
        return args
    
    def get_key(self):
        xB = eval('0x' + '435B39CC A8F3B508 C1488AFC 67BE491A 0F7BA07E 581A0E48 49A5CF70 628A7E0A'.replace(' ', ''))
        yB = eval('0x' + '75DDBA78 F15FEECB 4C7895E2 C1CDF5FE 01DEBB2C DBADF453 99CCF77B BA076A42'.replace(' ', ''))
        PB = (xB, yB)           # PB是B的公钥
        dB = eval('0x' + '1649AB77 A00637BD 5E2EFE28 3FBF3535 34AA7F7C B89463F2 08DDBC29 20BB0DA0'.replace(' ', ''))
        # dB是B的私钥
        key_B = (PB, dB)
        return key_B

#Encryption
ac = sm2Enc()
args = ac.get_args()
key_B = ac.get_key()
PB,SB = key_B
print("SB:",SB)
M = input('Input message:')
C = ac.sm2_Enc(args,PB,M)
#Decryption
D = ac.sm2_Dec(args,SB,C)


# print('1',ac.intTbytes(52,10))
# print('2',ac.bytesTint(b'\x00\x00\x00\x00\x00\x00\x00\x00\x004'))
# print('3',ac.bitsTbytes('101010101000111'))
# print('4',ac.bytesTbits(b'\x00\x00\x00\x00\x00\x00\x00\x00\x004'))
# print('5',ac.fEleTbytes(2))
# print('6',ac.bitsThex('1'))
# print('7',ac.KDF('101010',128))