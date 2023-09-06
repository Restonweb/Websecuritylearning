import hashlib

s = 'abc'
Vsha1 = hashlib.sha1()
Vsha1.update(s.encode('utf-8'))
print(Vsha1.hexdigest())

#需要注意的是，hashlib的update如果重复使用，相当于在原来加密的字符串后加上新的字符串来加密（加盐）

user = 'Reston'
pwd = '114514'
upe = user + pwd
newsha1 = hashlib.sha1()
newsha1.update(upe.encode('utf-8'))
newsha1.hexdigest()
newsha2 = hashlib.sha1()
useri = input('Username:')
pwdi = input('Password:')
newsha2.update((useri + pwdi).encode('utf-8'))
if newsha1.hexdigest() == newsha2.hexdigest():
    print("Hash Matched!")
else:
    print("Hash Failed!")
