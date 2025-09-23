# class Programer:
#     name1= "Harry"
#     language1= "Java"
#     salary1= 2000000

#     name2= "Rohan"
#     language2= "Python"
#     salary2= 1000000

#     name3= "Bittu"
#     language3= "Rust"
#     salary3= 4000000


#     @staticmethod
#     def greet():
#         print("Hello!!!")
#     def getinfo(self):
#         print(f"The name of first employee is: {self.name1}, The language used by the first employee is: {self.language1}, The salary of the first employee is: {self.salary1}\n\n")
#         print(f"The name of second employee is: {self.name2}, The language used by the second employee is: {self.language2}, The salary of the second employee is: {self.salary2}\n\n")
#         print(f"The name of third employee is: {self.name3}, The language used by the third employee is: {self.language3}, The salary of the third employee is: {self.salary3}\n\n")


# Microsoft= Programer()
# Microsoft.getinfo()




class Programer:
    company= "Microsoft"
    def __init__(self, name, language, salary):
        self.name= name
        self.language= language
        self.salary= salary
        print("I am building an instance attribute of Programer!!!!")

m= Programer("Harry", "Java", 1000000)
print(f"The name of the first employee is: {m.name}, The language used by the first employee is: {m.language}, The salary of the first employee is: {m.salary}, The comnapny of the first employee is: {m.company}\n\n")

m= Programer("Rohan", "C++", 2000000)
print(f"The name of the first employee is: {m.name}, The language used by the first employee is: {m.language}, The salary of the first employee is: {m.salary}, The comnapny of the second employee is: {m.company}\n\n")

m= Programer("Bittu", "Python", 3000000)
print(f"The name of the first employee is: {m.name}, The language used by the first employee is: {m.language}, The salary of the first employee is: {m.salary}, The comnapny of the third employee is: {m.company}\n\n")
