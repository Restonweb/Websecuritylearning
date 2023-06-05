#集合创建方法:
myset = {1,2,3,4,5}
mysecset = set('arcaea is a rythmic games')
print (myset)
print (mysecset)#集合有去重功能
#添加元素
myset.add(6)
print (myset)
#移除元素
myset.remove(2)#移除2，但是如果这个元素不存在，将会报错
myset.discard(2)#移除2，但是如果这个元素不存在，将不会报错
myset.pop()#随机删除一个元素
print (myset)
#计算集合长度
print (len(myset))
#清空集合
myset.clear()
print (myset)
#判断元素是否在集合中
if('a' in mysecset):
    print ('true')
else:
    print ('false')