def biggest(a,b,c):
    if(a > b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b
        else:
            return c


print (biggest(3, 6, 9))
