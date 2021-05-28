def swap_case(s):
    o=""
    for i in s:
        if i.isupper()==True:
            o+=i.lower()
        elif i.islower()==True:
            o+=i.upper()
        else:
            o+=i
    return o

