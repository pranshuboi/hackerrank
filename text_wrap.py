

def wrap(string, max_width):
    for i in range(0,len(string),max_width):
        result=string[i:i+max_width]
        if len(result)==max_width:
            print(result)
        else:
            return(result)
