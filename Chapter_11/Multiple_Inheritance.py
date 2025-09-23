class Employee:
    company= "ITC"
    salary= 2000000
    language= "C++"
    def show(self):
        print(f"The company of the employee is: {self.company}, The salary of the employee is: {self.salary}, The language used by the employee is: {self.language}\n")


class Company:
    name= "Microsoft"
    salary_range= "2000000-3000000"
    def show_that(self):
        print(f"The name of the compnay is: {self.name}, The salary_range of the company is: {self.salary_range}\n")


class Programmer(Employee, Company):
    language= "Python"
    def show_in(self):
        print(f"The language used by the programmer is: {self.language}\n")


a= Employee()
b= Company()
c= Programmer()


c.show()
c.show_that()
c.show_in()