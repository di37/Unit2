def fix_machine(debris, product):
    l = len(product) - 1
    i= 0
    while(0 <= l):
        if(debris.find(product[i])==-1):
           return "Give me something that's not useless next time."
        i=i+1
        l= l-1
        #print (i, l)
    return product

### TEST CASES ###
print ("Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time.")
print ("Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity')
print ("Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity')
print ("Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt')
