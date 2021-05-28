if __name__ == '__main__':
    s = raw_input()
    u=0
    l=0
    d=0
    an=0
    a=0
    for i in s:
        if i.isupper()==True:
            u+=1
        if i.islower()==True:
            l+=1
        if i.isdigit()==True:
            d+=1
        if i.isalpha()==True:
            a+=1
        if i.isalnum()==True:
            an+=1
    if an>0:
        print("True")
    else:
        print("False")
    if a>0:
        print("True")
    else:
        print("False")
    if d>0:
        print("True")
    else:
        print("False")
    if l>0:
        print("True")
    else:
        print("False")
    if u>0:
        print("True")
    else:
        print("False")
    
