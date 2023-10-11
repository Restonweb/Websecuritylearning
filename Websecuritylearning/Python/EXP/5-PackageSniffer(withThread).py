import queue
import socket
import threading
from datetime import datetime


class IPsniffer:
    def __init__(self):
        self.packet_queue = queue.Queue()

    def start_sniffing(self):
        # 创建两个线程，一个用于数据包捕获，另一个用于数据包解析和打印
        capture_thread = threading.Thread(target=self.catchData)
        process_thread = threading.Thread(target=self.processprintData)

        # 启动线程
        capture_thread.start()
        process_thread.start()

        # 等待线程完成
        capture_thread.join()
        process_thread.join()

    def catchIPData(self):
        HOST = "192.168.123.54"  # 本机IP
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)  # 创建原始套接字
        s.bind((HOST, 0))
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        package = s.recvfrom(65535)
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        s.close()
        return package[0]

    def catchData(self):
        while True:
            data = self.catchIPData()
            self.packet_queue.put(data)

    def processprintData(self):
        while True:
            timestamp = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))

            data = self.packet_queue.get()
            package = self.decodeIPHeader(data)
            print("%s  --->  %s  %s IPv%s 协议：%s 数据包长度：%s Bytes" % (
                ("\033[036m" + package['sourceAddress']).center(20, ' ') + "\033[0m", "\033[035m" + package['destinationAddress'].center(20, ' ') + "\033[0m", timestamp,
                package['version'], self.protocolClassify(package['protocol']), package['totalLength']))

    def protocolClassify(self, PF):
        PF = int(PF)
        if PF == 1:
            return "\033[34mICMP\033[0m"
        elif PF == 6:
            return "\033[32mTCP\033[0m"
        elif PF == 17:
            return "\033[33mUDP\033[0m"
        elif PF == 41:
            return "IPv6"
        elif PF == 50:
            return "ESP"
        elif PF == 51:
            return "AH"
        elif PF == 89:
            return "OSPF"
        elif PF == 132:
            return "SCTP"
        else:
            return "\033[31mUKN\033[0m"

    def decodeIPHeader(self, package):
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
        IPDatagram['sourceAddress'] = "%d.%d.%d.%d" % (package[12], package[13], package[14], package[15])
        IPDatagram['destinationAddress'] = "%d.%d.%d.%d" % (package[16], package[17], package[18], package[19])

        IPDatagram['data'] = []
        step = IPDatagram['headLength'] * 4
        while step < IPDatagram['totalLength']:
            IPDatagram['data'].append(package[step])
            step += 1
        return IPDatagram


if __name__ == '__main__':
    IPsniffer().start_sniffing()
