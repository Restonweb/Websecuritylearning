import queue
import socket
import threading
from datetime import datetime
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt, Slot, Signal, QObject  # Flag Argument
from Ui_sniffer import Ui_Form


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CF = False

    def closeEvent(self, event):
        self.CF = True
        event.accept()


class IPsniffer(QObject):
    packet_recved = Signal(dict)

    def __init__(self):
        super().__init__()
        self.s = None
        self.PORT = 0
        self.app = QApplication([])
        self.window = MyWindow()
        self.packet_queue = queue.Queue()
        self.ui_init()

    def ui_init(self):
        self.packet_recved.connect(self.outputr)
        self.window.ptcset.addItems(["全部协议", "TCP", "UDP", "ICMP", "IPV6", "ESP", "AH", "OSPF", "SCTP"])
        self.window.ptcset.setCurrentIndex(0)

    def start_sniffing(self):
        # 创建两个线程，一个用于数据包捕获，另一个用于数据包解析和打印
        capture_thread = threading.Thread(target=self.catchData)
        process_thread = threading.Thread(target=self.processprintData)

        # 启动线程
        capture_thread.start()
        process_thread.start()

        self.window.show()
        self.app.exec()

        # 等待线程完成
        capture_thread.join()
        process_thread.join()

    def getLocalIP(self):
        st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        st.connect(("8.8.8.8", 80))
        LIP = st.getsockname()[0]
        self.window.selfip.setText("本机IP: %s:%s" % (LIP, self.PORT))
        st.close()
        return LIP

    def catchIPData(self):
        HOST = self.getLocalIP()  # 本机IP
        self.s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)  # 创建原始套接字
        self.s.bind((HOST, self.PORT))
        self.s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        self.s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        package = self.s.recvfrom(65535)
        self.s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        self.s.close()
        return package[0]

    def catchData(self):
        try:
            while True:
                if self.window.startsniff.isChecked():
                    self.window.startsniff.setText("停止抓取")
                    self.window.output.clear()
                    while True:
                        data = self.catchIPData()
                        self.packet_queue.put(data)
                        if self.window.startsniff.isChecked() is False:
                            self.window.startsniff.setText("抓取")
                            self.window.selfip.setText("开始抓取以获取IP")
                            self.s.close()
                            break
                        elif self.window.CF is True:
                            self.window.selfip.setText("开始抓取以获取IP")
                            self.s.close()
                            raise Exception("Manual Stop：UI is closed")
                elif self.window.CF is True:
                    self.s.close()
                    raise Exception("Manual Stop：UI is closed")
                else:
                    continue
        except PermissionError:
            self.window.output.setPlainText("错误：请以管理员身份运行")
        except Exception:
            print("UI is closed")

    def processprintData(self):
        while True:
            timestamp = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
            data = self.packet_queue.get()
            if data:
                package = self.decodeIPHeader(data)
                self.packet_recved.emit(package)
                print("%s  --->  %s  %s IPv%s 协议：%s 数据包长度：%s Bytes" % (
                    (("\033[036m" + package['sourceAddress']) + ":" + str(package['sourcePort'])).center(20,
                                                                                                         ' ') + "\033[0m",
                    ("\033[035m" + package['destinationAddress'] + ":" + str(package['destinationPort'])).center(20,
                                                                                                                 ' ') + "\033[0m",
                    timestamp,
                    package['version'], self.protocolClassify(package['protocol']), package['totalLength']))

    def elementchange(self):
        self.window.ptcset.currentIndexChanged.connect(lambda: self.window.output.clear())
        if self.window.portset.text() == '':
            self.PORT = 0
        else:
            self.PORT = int(self.window.portset.text())

    @Slot(dict)
    def outputr(self, package):
        self.elementchange()
        timestamp = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # 获取文本框的内容
        src_filter = self.window.srcfil.text()
        dst_filter = self.window.dstfil.text()
        # 获取选择的协议
        selected_protocol_index = self.protocolfillter(self.window.ptcset.currentIndex())

        if (    # 过滤器
                (selected_protocol_index == 0 or package['protocol'] == selected_protocol_index) and
                (src_filter == '' or package['sourceAddress'] == src_filter) and
                (dst_filter == '' or package['destinationAddress'] == dst_filter)
        ):
            result = "%s  --->  %s | %s | IPv%s | 协议：%s | 数据包长度：%s Bytes" % (
                (package['sourceAddress'] + ":" + str(package['sourcePort'])).center(20, ' '),
                (package['destinationAddress'] + ":" + str(package['destinationPort'])).center(20, ' '), timestamp,
                package['version'], self.protocolClassifys(package['protocol']), package['totalLength'])
            self.window.output.appendPlainText(result)

    def protocolfillter(self, pindex):
        if pindex == 0:
            return 0
        elif pindex == 1:
            return 6
        elif pindex == 2:
            return 17
        elif pindex == 3:
            return 1
        elif pindex == 4:
            return 41
        elif pindex == 5:
            return 50
        elif pindex == 6:
            return 51
        elif pindex == 7:
            return 89
        elif pindex == 8:
            return 132

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

    def protocolClassifys(self, PF):
        PF = int(PF)
        if PF == 1:
            return "ICMP"
        elif PF == 6:
            return "TCP"
        elif PF == 17:
            return "UDP"
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
            return "UKN"

    def decodeIPHeader(self, package):  # 解包IP包头字典
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
        IPDatagram['sourceAddress'] = "%d.%d.%d.%d" % (package[12], package[13], package[14], package[15])  # 源地址
        IPDatagram['destinationAddress'] = "%d.%d.%d.%d" % (package[16], package[17], package[18], package[19])  # 目的地址
        IPDatagram['data'] = []
        if IPDatagram['protocol'] == 6 or IPDatagram['protocol'] == 17:  # 当为TCP包或UDP包时，解析其包头，获取源地址与目的地址的端口
            tupack = package[IPDatagram['headLength']:]
            IPDatagram['sourcePort'] = (tupack[0] << 8) + tupack[1]
            IPDatagram['destinationPort'] = (tupack[2] << 8) + tupack[3]
        else:
            IPDatagram['sourcePort'] = "UKN"
            IPDatagram['destinationPort'] = "UKN"
        step = IPDatagram['headLength'] * 4
        while step < IPDatagram['totalLength']:
            IPDatagram['data'].append(package[step])
            step += 1
        return IPDatagram


if __name__ == '__main__':
    IPsniffer().start_sniffing()
