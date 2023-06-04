#https://www.runoob.com/python3/python3-function.html
'''
+++可更改(mutable)与不可更改(immutable)对象+++

在 python 中,strings, tuples, 和 numbers 是不可更改的对象,而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10,这里实际是新生成一个 int 值对象 10,再让 a 指向它,而 5 被丢弃,不是改变 a 的值,相当于新生成了 a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改,本身la没有动,只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 C++ 的值传递,如整数、字符串、元组。如 fun(a),传递的只是 a 的值,没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值,则是新生成一个 a 的对象。

可变类型：类似 C++ 的引用传递,如 列表,字典。如 fun(la),则是将 la 真正的传过去,修改后 fun 外部的 la 也会受影响

python 中一切都是对象,严格意义我们不能说值传递还是引用传递,我们应该说传不可变对象和传可变对象。
'''

def caclarea():
    #计算面积
    def AREA(length,width):
        SUM = length*width
        return SUM

    print ("INPUT LENGTH AND WIDTH")
    length =  int(input("Length:"))
    width = int(input("Width:"))
    print ("This Area is about :{}.".format(AREA(length,width)))

#不可变对象
def nonVarible():
    def toA(a):
        print(id(a))#同一个对象
        a = 10      #新建了对象
        print(id(a))#id不同
    a = 5
    print(id(a))
    toA(a)

def doVarible():
    def tolist(mylist):
        mylist.append([1,2,3,4])
        print (mylist)
    mylist = [5,6,7,8]
    print (mylist)
    tolist(mylist)
    print (mylist)#函数外的随之改变，确认为同一个对象

#caclarea()
#nonVarible()
doVarible()