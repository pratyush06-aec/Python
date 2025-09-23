class Complex:

    
    def __init__(self, i, n):
        self.i= i
        self.n= n

    @staticmethod
    def show_that():
        print("Hello, Now we starting with the calculation!!!!")


    def show(self):
        print(f"The complex number is: {self.i}i + {self.n}")


    def __add__(self, num):
        return Complex(self.i+num.i, self.n+num.n)
    
    def __mul__(self, num):
        return Complex(self.i*num.i, self.n*num.n)
    
    def __str__(self):                                ## This __str__(dunder method) is used for string representation of the output.
        return f"{self.i}i+{self.n}"

a= Complex(2, 4)
b= Complex(3, 5)
a.show_that()
a.show()

print(a+b)
print(a*b)


