# class vector:
#     def __init__(self, i, j, k):
#         self.i= i
#         self.j= j
#         self.k= k

#     def show(self):
#         print(f"The equation would be: {self.i}i + {self.j}j + {self.k}k\n")

#     @staticmethod
#     def show_that():
#         print("Now, We are starting with the calculation part!!!")

#     def __add__(self, num):
#         return vector(self.i+num.i, self.j+num.j, self.k+num.k)
    
#     def __mul__(self, num):
#         return vector(self.i*num.i, self.j*num.j, self.k*num.k)
    
#     def __str__(self):
#         return f"{self.i}i+{self.j}j+{self.k}k"

# a= vector(2, 3, 4)
# b= vector(4, 5, 6)
# a.show()
# a.show_that()

# print(a+b)
# print(a*b)



class vector:
    def __init__(self, i, j, k):
        self.i= i
        self.j= j
        self.k= k

    def show(self):
        print(f"The vector equation is: {self.i}i + {self.j}j + {self.k}k\n")

    @staticmethod
    def show_that():
        print("Now, We are starting away with the calculation part!!!!")

    def __add__(self, num):
        result= vector(self.i+num.i, self.j+num.j, self.k+num.k)
        return result
    
    def __add__(self, num):
        result= self.i+num.i + self.j+num.j + self.k+num.k
        return result
    
    def __mul__(self, num):
        result= self.i*num.i, self.j*num.j, self.k*num.k
        return result
    
    def __mul__(self, num):
        result= self.i*num.i + self.j*num.j + self.k*num.k
        return result
    
    def __str__(self):
        return f"vector({self.i}i, {self.j}j, {self.k}k)\n"
    

a= vector(2, 3, 4)
b= vector(5, 6, 7)

a.show()
b.show()

a.show_that()

print(a+b)
print(a*b)



