from cryptography.hazmat.primitives import hashes
from datetime import datetime
import time
from SM2Enc import sm2Enc
import socket
import threading
import pymysql

sm2 = sm2Enc()


class EV:
    Register = None
    Kevp = None
    MLEN = 1024
    Kpub = None
    IDarea = None
    RIDev = None
    SQLTIMEOUT = 0.01
    
    def __init__(self):
        self.__EVkeypair = sm2.gen_key()
        self.__kevs = self.__EVkeypair[1]
        self.__kevp = self.__EVkeypair[0]
        EV.Kevp = self.__kevp
        self.__networkinit()
        self.dbinit('ev')

    def dbinit(self, table_name):
        db = pymysql.connect(host='localhost', user='root', password='', database='ev', connect_timeout=10)
        cursor = db.cursor()
        sql = f"SELECT * FROM {table_name}"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
        except:
            print("Unable to fetch data")
        IDEV = None
        for row in results:
            IDEV, IDNEV, RIDev, Kpub, Register, IDarea = row
        if IDEV is None:
            sql = f"INSERT INTO {table_name} VALUES (1,1,1,1,1,1);"  # 设置初值，因为下面的操作都是UPDATE
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
                print("Database initialization failed!")
        db.close()
        time.sleep(EV.SQLTIMEOUT)

    def sqlupdate(self, table_name, colname, data):
        db = pymysql.connect(host='localhost', user='root', password='', database='ev', connect_timeout=10)
        cursor = db.cursor()
        sql = f"UPDATE {table_name} SET {colname}='%s'" % data
        print("\033[35m---SQL---:\033[0m", sql)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()
        time.sleep(EV.SQLTIMEOUT)

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
        self.Bi = None
        while True:
            data = self.client.recv(self.MLEN).decode()
            if data.startswith("Kpub:"):
                ktemp = data.split(':')[1]
                print("Received Kpub:", ktemp)
                ltemp = ktemp[1:-1].split(',')
                EV.Kpub = (int(ltemp[0]), int(ltemp[1]))
                self.sqlupdate('ev', 'Kpub', ktemp)
            elif data.startswith("RIDev:"):
                EV.RIDev = data.split(":")[1]
                print(f"Received RIDev:{EV.RIDev}")
                self.sqlupdate('ev', 'RIDev', EV.RIDev)
                # 计算Bi
                p, a, b, h, G, n = sm2.get_args()
                kmult = sm2.multPoint(EV.Kpub, self.__kevs, p, a)
                E1 = sm2.bytesTint(sm2.pointTbytes(kmult))
                E2 = eval(EV.RIDev)
                self.Bi = E1 ^ E2
                print("KpubKevp ^ RIDev = Bi:", self.Bi)
            elif data.startswith("Error:"):
                Error = data.split(':')[1]
                raise Exception(f"Error:{Error}")
            elif data:
                print("Received data:", data)

    def Reg(self, IDEV, IDNEV, IDarea, register):
        self.sqlupdate('ev', 'IDEV', IDEV)
        self.sqlupdate('ev', 'IDNEV', IDNEV)
        self.sqlupdate('ev', 'IDarea', IDarea)
        self.sqlupdate('ev', 'Register', register)
        EV.Register = register
        EV.IDarea = IDarea
        while True:
            if EV.Kpub is None:  # 等待RA发送区域公钥Kpub
                continue
            elif EV.Kpub is not None:
                t = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
                # ts = "2023-09-12-12-57-10"
                print("\033[36m--------------------Ready to progress Registration,Current UTC time is <{time}>--------------------\033[0m".format(time=t))
                reg1 = "Reg1:" + self.Enc(EV.Kpub, IDEV, IDNEV, IDarea, t)
                print(reg1)
                self.client.send(reg1.encode())
                break
        while True:
            if self.Bi is None:
                continue
            elif self.Bi is not None:
                reg2 = "Reg2:" + self.Enc(EV.Kpub, str(self.Bi), str(EV.Kevp), EV.RIDev, EV.IDarea)
                print(reg2)
                self.client.send(reg2.encode())
                break

# t = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
# print(t)
