class vector1:
    def __init__(self, i, j):
        self.i= i
        self.j= j

    def vec1(self):
        print(f"The 2-D vector is: {self.i}i + {self.j}j\n")


class vector2(vector1):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k= k
    def vec2(self):
        print(f"The 3-D vector is: {self.i}i + {self.j}j + {self.k}k\n")


a= vector1(2, 3)
a.vec1()
b= vector2(2, 3, 4)
b.vec2()