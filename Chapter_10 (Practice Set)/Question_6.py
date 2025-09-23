## If we write something else, in place of self.... It would not affect the attribute as well as the output.


from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo= trainNo

    def trainbooking(self, fro, to):
        print(f"Your train no: {self.trainNo} is booked from {fro} to {to}")
    
    def trainstatus(self):
        print(f"Your train no: {self.trainNo} is running on time")

    def trainfare(self, fro, to):
        print(f"The fare of your train no: {self.trainNo} from {fro} to {to} is {randint(1000, 5000)}")


Duronto= Train(234875)
Duronto.trainbooking("Asansol", "New Delhi")
Duronto.trainstatus()
Duronto.trainfare("Asansol", "New Delhi")