class Employee:
    company= "Microsoft"
    def show(self):
        print(f"The name of the company of the employee is: {self.company}\n")

class Programmer(Employee):
    name= "John Doe"
    def show_that(self):
        print(f"The name of the programmer is: {self.name}\n")

class Coder(Programmer):
    naming= "Harry"
    def show_in(self):
        print(f"The name of the coder is: {self.naming}\n")



a= Employee()
b= Programmer()
c= Coder()

c.show()
b.show_that()
c.show_in()



# a= Employee()
# a.show()
# a= Programmer()
# a.show()
# a.show_that()
# a= Coder()
# a.show()
# a.show_that()
# a.show_in()
