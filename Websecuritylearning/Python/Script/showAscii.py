def ascx():
    while True:
        x = int(input("Ascii:"))
        if x:
            print(chr(x))
        else:
            break
def chrx():
    while True:
        s = input("chr:")
        if s:
            print(ord(s))
        else:
            break
        
ascx()
#chrx()