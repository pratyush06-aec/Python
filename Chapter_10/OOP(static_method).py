## staticmethod eliminates the need of object creation. And here, greet() function is a staticmethod which doesn't need any object.  


class Employee:
    name= "Harry"
    language= "Java"
    salary= 2000000

    def getinfo(self):
        print(f"The name is: {self.name}, The language is: {self.language}, The salary is: {self.salary} ")

    @staticmethod
    def greet():
        print("Hello!!!")

Harry= Employee()
Harry.getinfo()
# Employee.getinfo(Harry)
Harry.greet()