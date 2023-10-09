# 具体要求：对指定的网段和端口进行扫描。
# A、 可指定IP地址或是网段，可指定端口范围；
# B、 可设定扫描所需的线程数；
# C、 对扫描结果进行良好的显示。
import time, socket

def getipbydomain(domain):  #域名转ip
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        print("Exception:%s||%s"%(domain,e))

def __portscan(ip, portlist, timeout):  #端口扫描
    result_list = list()
    for port in portlist:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            RFlag = s.connect_ex((ip, port))  #connect_ex不引发错误，而是返回错误码
            if RFlag == 0:
                print("% 6d [OPEN]"%port)
                result_list.append(port)
            else:
                continue
        except Exception as e:
            print(e)
        finally:
            s.close()
    return result_list

def scanallport(ip, start_port = 1, end_port = 65535, timeout = 3):
    portlist = range(start_port, end_port+1)
    resultlist = __portscan(ip, portlist, timeout)
    return resultlist

if __name__ == '__main__':
    scanallport("127.0.0.1")