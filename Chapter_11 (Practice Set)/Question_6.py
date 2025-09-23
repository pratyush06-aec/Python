class vector:
    def __init__(self, i, j, k):
        self.i= i
        self.j= j
        self.k= k

    def show(self):
        print(f"The vector equation is: {self.i}i + {self.j}j + {self.k}k\n")

    @staticmethod
    def show_that():
        print("So now, Let's start with the calculation part!!!\n")

    def __add__(self, num):
        return self.i+num.i, self.j+num.j, self.k+num.k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k\n"    

a= vector(2, 3, 4)
b= vector(3, 4, 7)
a.show()
a.show_that()

print(a+b)