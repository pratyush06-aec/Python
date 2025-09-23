class Demo:
    a= 4

o= Demo()
print(o.a)        ## Prints the class attribute, as it is called. The assigned value of a is printed.

o.a= 3
print(o.a)        ## Prints the instance attribute, as it is called. The updated value is printed for a.
print(Demo.a)     ## Prints teh class attribute, as it is called. 


## This indicates that the class attribute is not changed, even after creating an instance attribute.
## Only the value of that particular instance is printed, which is called at that particular time.