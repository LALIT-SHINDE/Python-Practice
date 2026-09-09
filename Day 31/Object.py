# Level 2
# 6. Method That Changes Object Data
class BankAccount:
    def __init__(self, name, balance):
        self.b = balance
        self.n = name

    def deposit(self, amount):
        self.b += amount

    def show_Balance(self):
        print(f"Name: {self.n}\nBalance: {self.b}\n")

s = BankAccount("Amit",1500)
s.deposit(500)
s.show_Balance()

s.deposit(600)
s.show_Balance()

s.deposit(400)
s.show_Balance()

# Level 3
# 7. Class vs Object

class Dog:
    species = "Dog"

d1 = Dog() # d1 is the object of the class
d2 = Dog() # d2 is the object of the class

print(d1.species)
print(d2.species)
print(Dog.species) # Dog is class and called the object

# 8. Fix the Code
class Mobile:

    def __int__(self, brand, price):
        self.brand = brand
        self.price = price

    def show():
        print(self.brand, self.price)


m1 = Mobile("Samsung", 20000)
m1.show()

class Mobile:
    def __init__(self, brand, price): # Its __init__() not a __int__()
        self.brand = brand
        self.price = price

    def show(self): # its need a parameter of self to called self values
        print(self.brand, self.price)

m1 = Mobile("Samsung", 20000)
m1.show()

