from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo= trainNo

    def trainbooking(self, fro, to):
        print(f"Your train no: {self.trainNo} is booked from: {fro} to {to}")
    
    def gettrainstatus(self):
        print(f"The train no: {self.trainNo} is running on time")

    def trainFare(self, fro, to):
        print(f"Your train no: {self.trainNo} from {fro} to {to} is: {randint(100, 2000)}")


Rajdhani= Train(123456)
Rajdhani.trainbooking("Asansol", "Durgapur")
Rajdhani.gettrainstatus()
Rajdhani.trainFare("Asansol", "Durgapur")

