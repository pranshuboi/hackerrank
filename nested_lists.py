L=[]
L1=[]
for _ in range(int(raw_input())):
    L1=[]
    name = raw_input()
    score = float(raw_input())
    L1.append(name)
    L1.append(score)
    L.append(L1)
L2=[]
i=0
while i<len(L):
    L2.append(L[i][1])
    i=i+1
L2.sort()
i=1
L3=[]
while i<len(L2):
    if L2[i]!=L2[i-1]:
        L3.append(L2[i])
        break
    i=i+1
L4=[]
i=0
while i<len(L):
    if L[i][1]==L3[0]:
        L4.append(L[i][0])
    i=i+1
L4.sort()
for i in L4:
    print(i)





    
    
    

    
