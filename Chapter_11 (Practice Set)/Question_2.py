class Animals:
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
    @staticmethod
    def show():
        print("Bowhh Bowhhh!!!!!")


a= Dogs()
a.show()