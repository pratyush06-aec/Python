## @classmethod and using cls in place of self runs the value of the class attribute and not the instance attribute.

## self indicates the instance/object on which the method is running and cls indicates the class of the instance/object on which the method is running.


class Employee:
    salary= 2000000
    @classmethod
    def show(cls):
        print(f"The salary of the employee is: {cls.salary}\n")

a= Employee()
a.salary= 1000000
a.show()