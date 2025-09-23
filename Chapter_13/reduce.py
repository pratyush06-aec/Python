# from functools import reduce

l= [1, 2, 3, 4, 5, 67, 8, 9, 100]

# def sum(a, b):
#     return a+b

# print(reduce(sum, l))


from functools import reduce

def mul(a, b):
    return a*b

print(reduce(mul, l))