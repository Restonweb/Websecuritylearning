import hashlib
from base64 import b64encode
from uuid import uuid4
import time
fmd5 = hashlib.md5("/hints.txt".encode()).hexdigest()
target = "0d5735350c7d6b398c0c8d0719ff3aa0"
stime = time.time()
while True:
    cookiesecret = b64encode(uuid4().bytes + uuid4().bytes)
    generatemd5 = hashlib.md5((str(cookiesecret)[2:-1] + fmd5).encode())
    if generatemd5 == target:
        print("+++++++++++++++++++++++\ncookiesecret:%s\n+++++++++++++++++++++++"%cookiesecret)
        etime = time.time()
        print("[Elapse time] %3ss"%(etime - stime))
        break
    else:
        continue
