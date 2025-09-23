class Employee:
    language= "C++"
    salary= 100000
    name= "Alice"

    def getinfo(self):
        print(f"The name is: {self.name}, The language is: {self.language}, The salary is: {self.salary}")

Alice= Employee()
Alice.language= "Java"
Alice.getinfo()
# Employee.getinfo(Alice)

## Here, Alice.getinfo()== Employee.getinfo(Alice) 
