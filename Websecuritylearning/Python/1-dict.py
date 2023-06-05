#字典是另一种可变容器模型，且可存储任意类型对象。
#字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中
#键必须是唯一的，但值则不必。
#值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
dict0 = {"name":"RedCamellia","age":20}
#访问字典元素通过键[key]来访问其值，如下所示    ！确保键存在于字典中，否则会出错
print (dict0["name"])
print (dict0["age"])
#删除，清空字典的操作:
dict1 = {'A':1,'B':2,'C':3,'D':4,'E':5}
del dict1['C']#删除元素C:3
dict.clear    #清空字典
del dict1     #删除整个字典
dict0['age'] = 19#修改值
dict0['addr'] = 'Earth'#添加键值对
dict1['A':1,'B':2,'C':3,'D':4,'E':5,'E':6]#一个字典不允许出现重复的键，如果出现，则保留最后的值
print(dict1['E'])
#键需要不可变，即可以用数字，字符串，元组充当，而列表就不行
'''
###内置函数###
序号	函数及描述
1	dict.clear()
删除字典内所有元素
2	dict.copy()
返回一个字典的浅复制
3	dict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	dict.get(key, default=None)
返回指定键的值，如果键不在字典中返回 default 设置的默认值
5	key in dict
如果键在字典dict里返回true，否则返回false
6	dict.items()
以列表返回一个视图对象
7	dict.keys()
返回一个视图对象
8	dict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	dict.update(dict2)
把字典dict2的键/值对更新到dict里
10	dict.values()
返回一个视图对象
11	pop(key[,default])
删除字典 key（键）所对应的值，返回被删除的值。
12	popitem()
返回并删除字典中的最后一对键和值。
'''