class calculator:

    @staticmethod
    def greet():
        print("Hello!!!")

    def __init__(self, n):
        self.n= n

    def square(self):
        print(f"The square of the number is: {self.n**2}")
    def cube(self):
        print(f"The cube of the number is: {self.n**3}")
    def square_root(self):
        print(f"The squazre_root of the number is: {self.n**(1/2)}")


No= calculator(3)
No.greet()
No.square()
No.cube()
No.square_root()

