## Here, John_Doe.name returns "Harry". So, it's a instance attribute.
## And, .langauge and .salary is the class attribute.

class Employee:
    language= "Python"
    salary= 120000
    name= "John_Doe"

John_Doe= Employee()
John_Doe.name= "Harry"
print(John_Doe.name, John_Doe.language, John_Doe.salary)