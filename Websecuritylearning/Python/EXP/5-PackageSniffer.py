import socket


class IPsniffer:
    def __init__(self):
        print("%s  --->  %s" % (self.decodeIPHeader(self.catchIPData())['sourceAddress'], self.decodeIPHeader(self.catchIPData())['destinationAddress']))
    
    def catchIPData(self):
        HOST = socket.gethostbyname(socket.gethostname())   # 获取本机IP作为公共网络接口
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)   # 创建原始套接字
        s.bind((HOST, 0))
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        package = s.recvfrom(65535)
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        s.close()
        return package[0]

    def decodeIPHeader(self,package):
        IPDatagram = {}
        IPDatagram['version'] = package[0] >> 4
        IPDatagram['headLength'] = package[0] and 0x0f
        IPDatagram['serviceType'] = package[1]
        IPDatagram['totalLength'] = (package[2] << 8) + package[3]
        IPDatagram['identification'] = (package[4] << 8) + package[5]
        IPDatagram['flag'] = package[6] >> 5
        IPDatagram['moreFragment'] = IPDatagram['flag'] and 1
        IPDatagram['dontFragment'] = (IPDatagram['flag'] >> 1) and 1
        IPDatagram['fragmentOffset'] = ((package[6] and 0x1f) << 8) + package[7]
        IPDatagram['TTL'] = package[8]
        IPDatagram['protocol'] = package[9]
        IPDatagram['headerCheckSum'] = (package[10] << 8) + package[11]
        IPDatagram['sourceAddress'] = "%d.%d.%d.%d" % (package[12],package[13],package[14],package[15])
        IPDatagram['destinationAddress'] = "%d.%d.%d.%d" % (package[16],package[17],package[18],package[19])
        IPDatagram['options'] = []
        if IPDatagram['headLength'] > 5:
            step = 5
            while step < IPDatagram['headLength']:
                IPDatagram['options'].append(package[step * 4])
                IPDatagram['options'].append(package[step * 4 + 1])
                IPDatagram['options'].append(package[step * 4 + 2])
                IPDatagram['options'].append(package[step * 4 + 3])
                step += 1

        IPDatagram['data'] = []
        step = IPDatagram['headLength'] * 4
        while step < IPDatagram['totalLength']:
            IPDatagram['data'].append(package[step])
            step += 1
        return IPDatagram

if __name__ == '__main__':
    IPsniffer()