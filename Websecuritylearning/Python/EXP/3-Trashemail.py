import random
import smtplib
import time
from email.message import EmailMessage

Sender = "2824398066@qq.com"
Senderpassword = "naoknigybsyxdcfh"
Receiver = input("Input Reciver email:")
msg1 = "原神怎么你了？原神怎么你了？原神怎么你了？原神怎么你了？原神怎么你了？原神怎么你了？"


def sendmail():
    try:
        msg = EmailMessage()
        msg["from"] = "Camellia <" + Sender + ">"  # from头和to头一定要符合服务器规则！
        msg["to"] = "Anotherme <" + Receiver + ">"
        rand = random.randint(0, 32767)
        msg["subject"] = "我是垃圾邮件" + str(rand)  # 随机标题内容，以免被限制
        # msg.set_content("*垃圾*" + str(rand * 2))
        msg.set_content(msg1 + str(rand * 2))

        server = smtplib.SMTP("smtp.qq.com", 587)
        server.starttls()  # 587端口需要使用TLS加密
        server.login(Sender, Senderpassword)
        server.sendmail(Sender, [Receiver], msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("An error occurred:", str(e))
        return False


mailcount = int(input("Input mailcount:"))
delay = int(input("Input delay:"))
for i in range(mailcount):
    if sendmail():
        print("Mail[%d] Sended!" % (i + 1))
    else:
        print("Mail[%d] Failed!" % (i + 1))
    time.sleep(delay)
