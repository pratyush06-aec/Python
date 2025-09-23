from functools import reduce

a= [2, 4, 5, 6, 7, 8, 99, 44, 78]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, a))