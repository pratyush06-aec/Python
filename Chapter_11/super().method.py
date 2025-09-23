class Coder:
    def __init__(self):
        print(f"Constructor of Coder\n")
    name= "Harry"

class Programmer(Coder):
    def __init__(self):
        super().__init__()
        print(f"Constructor of Programmer\n")
    language= "Java"

class Employee(Programmer):
    def __init__(self):
        print(f"Constructor of Employee\n")
    
    salary= 2000000

a= Coder()
print(a.name)
a= Programmer()
print(a.name, a.language)
a= Employee()
print(a.name, a.language, a.salary)

