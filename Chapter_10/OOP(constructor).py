## Here, __init__ is a dunder method.


class Employee:
    language= "Python"
    salary= 1200000
    name= "Pratyush"


    def __init__(self, name, language, salary):     ## The funtions that are used with __(underscores) are called dunder methods in python and they are automatically called when the program is ran.
        self.name= name
        self.language= language
        self.salary= salary
        print("I am creating an object")

    def getinfo(self):
        print(f"The name is: {self.name}, The language is: {self.language}, Tghe salary is: {self.salary}")

    @staticmethod
    def greet():
        print("Hello World!!!")

Pratyush= Employee("Harry", "Javascript", 2000000)
print(Pratyush.name, Pratyush.language, Pratyush.salary)
Pratyush.greet()
Pratyush.getinfo()