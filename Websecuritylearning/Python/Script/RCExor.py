def symbolxor(alpha):
    for i in range(0,127):
        for j in range(0,127):
            shift = i^j
            if ord(alpha) == shift and (i <= 126 and i >= 33) and (j <= 126 and j >= 33):
                print('|||  ' + chr(i) + "  |||ASCII:  " + str(i) + "  ----------xor----------  " + '|||  ' + chr(j) + '  |||ASCII:  ' + str(j) + ' ' + "==" + ' ' + chr(shift) + ' ' + "ASCII: " + str(shift))
                return  "'" + chr(i) + "'" + '^' + "'" + chr(j) + "'"
        
def wordsxor(str):
    result = []
    words = str.split(' ')
    for word in words:
        sen = []
        for i in word:
            sen.append(symbolxor(i))
        cmpsen = constructsen(sen=sen)
        result.append(word + ' : ' +cmpsen)
    for word in result:
        print(word)
        
def constructsen(sen):
    rcesen = ''
    lens = len(sen)
    for i in range(lens):
        if i == 0:
            rcesen += '(' + sen[i] + ')'
        else:
            rcesen += '.' + '(' + sen[i] + ')'
    return rcesen

while True:         
    x = input("Input your sentences words use ' ' to divide.\n")
    if x:
        wordsxor(x)
    else:
        break