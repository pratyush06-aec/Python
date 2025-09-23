## Always, in-case of priority, instance attribute is given importance before class attribute.

class Employee:
    language= "Python"                                    ## Here, language is a class attribute.
    salary= 1200000
    name= "Pratyush"

Pratyush= Employee()
Pratyush.language= "Javascript"                            ## Here, Pratyush.language is an instance attribute 
print(Pratyush.name, Pratyush.language, Pratyush.salary)