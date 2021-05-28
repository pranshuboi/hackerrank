b=''
c=0

def Binary(num):
    b=''
    if num==1:
        return 1
    else:
        while(num>=1):
            c=num%2
            b=b+str(c)
            num=num//2
        b=b[::-1]
        return b
def LenBinary(num):
    b=''
    if num==1:
        return 1
    else:
        while(num>=1):
            c=num%2
            b=b+str(c)
            num=num//2
        b=b[::-1]
    length=len(b)
    return length
def Octal(num):
    b=''
    if num==1:
        return 1
    else:
        while(num>=1):
            c=num%8
            b=b+str(c)
            num=num//8
        b=b[::-1]
        return b
def HexaDecimal(num):
    b=''
    if num==1:
        return 1
    else:
        while(num>=1):
            c=num%16
            if c<10:
                b=b+str(c)
            elif c==10:
                b=b+"A"
            elif c==11:
                b=b+"B"
            elif c==12:
                b=b+"C"
            elif c==13:
                b=b+"D"
            elif c==14:
                b=b+"E"
            elif c==15:
                b=b+"F"
            num=num//16
        b=b[::-1]
        return b
def print_formatted(num):
    l=LenBinary(num)
    for i in range(1,num+1):
        b=Binary(i)
        h=HexaDecimal(i)
        o=Octal(i)
        f=str(b)
        x=(str(i).rjust(l),str(o).rjust(l+1),str(h).rjust(l+1),str(b).rjust(l+1))
        final=''.join(x)
        print(final)
