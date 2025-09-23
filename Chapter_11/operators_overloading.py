class sum:
    def __init__(self, n):
        self.n= n

    def __add__(self, num):
        return self.n+num.n
    
a= sum(1)
b= sum(2)

print(a+b)
