## Single Inheritance.
## Here, Employee class is (BASE CLASS) and Programmer class is (DERIVED CLASS).


class Employee:                   ## Base Class
    company= "ITC"
    language= "Java"
    def showlanguage(self):
        print(f"The language is: {self.language}, The campany is: {self.company}\n")

    
class Programmer(Employee):       ## Derived Class
    salary= 2000000
    def showsalary(self):
        print(f"The salary of the employee is: {self.salary}\n")


a= Employee()
b= Programmer()

a.showlanguage()
b.showsalary()
b.showlanguage()


## Above, a.showlaguage() and b.showlanguage() gives the same output caz, programmer class in the derived class and Employee class is inherited in it(base class).