## Tuples are similar like lists i.e., they store all types of data type, but unlike lists they are immutable.
# a= (1, 5, "Orange", 3.45)
# print(type(a))  # Output: <class 'tuple'>


a= (1)                # In this case, the compiler treats it like an integer
b= (1,)               # Giving a comma after an element inside round brackets gives us a tuple with one element.
c= ()                 # This indicates an empty tuple
print(type(a))
print(type(b))
print(type(c))