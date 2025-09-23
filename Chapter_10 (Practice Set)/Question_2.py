class calculator:
    def __init__(self, n):
        self.n= n

    def square(self):
        print(f"The square of the number is: {self.n**2}\n")

    def cube(self):
        print(f"The cube of the number is: {self.n**3}\n")
    
    def square_root(self):
        print(f"The square_root of the number is: {self.n**(1/2)}\n")


No= calculator(4)
No.square()
No.cube()
No.square_root()


