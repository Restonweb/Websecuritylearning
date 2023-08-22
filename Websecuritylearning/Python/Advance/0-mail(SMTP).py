import smtplib
from email.message import EmailMessage

Sender = "???????@qq.com"
Senderpassword = "xxxxxxxxxxxxxx"
Receiver = "???????@qq.com"

def sendmail():
    try:
        msg = EmailMessage()
        msg["from"] = "Camellia <" + Sender + ">"#from头和to头一定要符合服务器规则！
        msg["to"] = "Anotherme <" + Receiver + ">"
        msg["subject"] = "这是来自SMTP的第一份邮件"
        msg.set_content("Hello World! 你好 世界！")

        server = smtplib.SMTP("smtp.qq.com", 587)
        server.starttls()  #587端口需要使用TLS加密
        server.login(Sender, Senderpassword)
        server.sendmail(Sender, [Receiver], msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("An error occurred:", str(e))
        return False

ret = sendmail()
if ret:
    print("Success!")
else:
    print("Failed!")
import smtplib
from email.message import EmailMessage

Sender = "2824398066@qq.com"
Senderpassword = "naoknigybsyxdcfh"
Receiver = "2824398066@qq.com"

def sendmail():
    try:
        msg = EmailMessage()
        msg["from"] = "Camellia <" + Sender + ">"#from头和to头一定要符合服务器规则！
        msg["to"] = "Anotherme <" + Receiver + ">"
        msg["subject"] = "这是来自SMTP的第一份邮件"
        msg.set_content("Hello World! 你好 世界！")

        server = smtplib.SMTP("smtp.qq.com", 587)
        server.starttls()  #587端口需要使用TLS加密
        server.login(Sender, Senderpassword)
        server.sendmail(Sender, [Receiver], msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("An error occurred:", str(e))
        return False

ret = sendmail()
if ret:
    print("Success!")
else:
    print("Failed!")
