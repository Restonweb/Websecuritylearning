list = ['Reston','RedCamellia','Camellia']#列表：方括号包裹
tinylist = ['Blue','green','red']
sum = list + tinylist
print (sum)
print (list + tinylist)

def reverselist(input):
    inputwords = input.split(" ")
    inputwords = inputwords[-1::-1]
    inputwords = ' '.join(inputwords)
    print (inputwords + '?')

src = "gay you Are"
reverselist(src)