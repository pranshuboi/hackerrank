n=int(input())
D={}
if n>=2 and n<=10:
    j=0
    while j<n:
        a=str(input())
        L=[]
        i=0
        while i<3:
            b=int(input())
            L.append(b)
            i=i+1
        D.update({a:L})
        j=j+1
    s=str(input())
    if s in D:
        L1=D[s]
        sum=0
        for k in L1:
            sum=sum+k
        avg=sum/3
        print(avg)
