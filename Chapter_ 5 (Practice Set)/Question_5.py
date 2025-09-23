s= set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)
print(len(s))


## when comparison operators are used in python, it checks the value of operator first, if they are same then they would be considered as a single value, ignoring the data type.
## For ex: In the above code, 20 and 20.0 are treated as a single unit.