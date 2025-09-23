class vector:
    def __init__(self, l):
        self.l= l

    def __len__(self):
        return len(self.l)             ## This __len__(dunder method) gives the length of the string.

a= vector([2, 3, 5])

print(len(a))
