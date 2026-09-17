class car1:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive !")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail !")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly !")

c1 = car1("BMW","M06")
boat1 = Boat("Titan","Newr")
pe = Plane("AirIndia", "Hyper jet")

c1.move()
boat1.move()
pe.move()

for i in [c1, boat1, pe]:
    i.move()


# Inheritance Class Polymorphism

class vehical:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model

    def show(self):
        print(self.brand,":",self.model)

class car(vehical):
    def move(self):
        print("Drive !")

class boat(vehical):
    def move(self):
        print("Sail !")

class plane(vehical):
    def move(self):
        print("Fly !")

c1 = car("BMW","M06")
b1 = boat("Titan","Newr")
p1 = plane("AirIndia","Jet")

for i in [c1, b1, p1]:
    i.show()        # Inherit method
    i.move()        # polymorphism method
