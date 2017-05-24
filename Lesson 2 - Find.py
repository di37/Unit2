def find_second(a, b):
    find_first = a.find(b)
    return a.find(b, find_first + 1)


danton = "De l'audace, encore de l'audace, toujours de l'audace"
print (find_second(danton, 'audace'))
