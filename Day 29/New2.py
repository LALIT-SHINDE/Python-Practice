#4
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

s1 = Employee("Amit", 30000)
s2 = Employee("Rahul", 50000)

print(s1.name, s1.salary)
print(s2.name, s2.salary)


# 5. Method Using Multiple Attributes
class Rectangel:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        print(f"Area: {self.lenght * self.width}")

s = Rectangel(10,5)
s.area()

#6
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount

    def show_Balance(self):
        print(self.balance)

a = BankAccount("Amit", 43000)
a.deposite(2000)
a.show_Balance()
