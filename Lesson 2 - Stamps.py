def stamps(num):
    if num > 0:
        five = int(num/5)
        two = int(num%5/2)
        one = int(num%5%2)
        print (five, two, one)
    else:
        print (0,0,0)

stamps(8)
