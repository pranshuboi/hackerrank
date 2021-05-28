if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    A=[]
    i=0
    j=0
    k=0
    while i<=x:
        j=0
        while j<=y:
            k=0
            while k<=z:
                L=[]
                if i+j+k!=n:
                    L.append(i)
                    L.append(j)
                    L.append(k)
                    A.append(L)
                k=k+1
            j=j+1
        i=i+1
    print(A)
