class Employee:
    salary= 100
    increament= 20

    @property
    def salaryafterincreament(self):
        return ((self.salary*(self.increament/100))+ self.salary)
    
    @salaryafterincreament.setter
    def salaryafterincreament(self, salary):
        self.amount_increamented= (((salary/self.salary)-1)*100)

a= Employee()
print(a.salaryafterincreament)

# a.salaryafterincreament= 120
# print(a.amount_increamented)
