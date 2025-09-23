## Abstuction & Incapsulation.

## Abstruction is the process of hiding the whole backend from the user.
## Incapsulation is the process of compiling the whole functiong components in a unit( Here class). 


class Employee:
    company= "Nvidia"
    @classmethod
    def show(cls):
        print(f"The name of the comapany where the employee is working is: {cls.company}\n")

    @property
    def name(self):
        return f"{self.fname}, {self.lname}"

    @name.setter    
    def name(self, value):
        self.fname= value.split(" ")[0]
        self.lname= value.split(" ")[1]



a= Employee()
a.company= "Google"
a.show()
a.name= "John Doe"
print(a.fname, a.lname)
