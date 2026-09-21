class Vehical:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehical):
    def move(self):
        print(self.brand, self.model,"Dive !!")

class Boat(Vehical):
    def move(self):
        print(self.brand, self.model, "Sail !!")

class Palne(Vehical):
    def move(self):
        print(self.brand, self.model, "Fly !!")

c1 = Car("BMW", "M06")
b1 = Boat("Titan","m32")
p1 = Palne("Air Jet", "New")

c1.move()
b1.move()
p1.move()
