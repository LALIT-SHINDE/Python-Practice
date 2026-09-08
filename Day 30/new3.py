# Level 4 — Challenge

# 9. Student Result

# Create a Student class with:

# name
# marks

# Create a method:

# result()

# If marks are ≥ 40:

# Amit: Pass

# Otherwise:

# Amit: Fail

# Test it with at least two different objects.

class Student:
    def __init__(self, name, marks):
        self.n = name
        self.m = marks

    def result(self):
        if self.m >= 40:
            print(f"{self.n}: Pass")

        else:
            print(f"{self.n}: Fail")

a = Student("Amit", 53)
b = Student("Nitin", 87)
c = Student("Sonu", 32)

a.result()
b.result()
c.result()

# 10. Mini OOP Challenge 🔥

class Book:
    def __init__(self, title, author, price):
        self.t = title
        self.a = author
        self.p = price

    def show_detailes(self):
        print(f"Title: {self.t}\nAuthor: {self.a}\nPrice: {self.p}\n")

    def discount(self, percentage):
        
        dis = (percentage/100) * self.p
        print(f"Book: '{self.t}' \nPrice: {self.p}")
        print(f"You have {percentage}% Discount on {self.p}Rs.")

        self.p -= dis

        print(f"Discounted price: {self.p}\n")

a = Book("Soul","J.k", 950)
a.show_detailes()
a.discount(20)

b = Book("Miss","s.j", 645)
b.show_detailes()
b.discount(30)



class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"Product: {self.name} \nPrice: {self.price}")

p1 = product("laptop",50000)
p1.show()

# 12. Temperature Converter
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenite(self):
        fahrenite = (self.celsius * 9/5) + 32

        print(f"{self.celsius} celsius = {fahrenite} Fahrenite")

t1 = Temperature(30)
t1.to_fahrenite()

#13. Counter — Changing Object Data
class Counter:
    def __init__(self, count= 0):
        self.count = count

    def increment(self):
        self.count += 1
        

    def show(self):
        print(self.count)

c1 = Counter()
c1.increment()
c1.increment()
c1.increment()

c1.show()

# 14. Two Different Objects 🔥
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount

    def show(self):
        print(f"{self.owner} : {self.balance}")

a1 = BankAccount("Amit", 1500)
a1.deposite(500)
a1.show()

a2 = BankAccount("Nitin", 1700)
a2.deposite(300)
a2.show()

# 15. Employee Salary 🔥🔥
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"{self.name} : {self.salary}")

    def increase(self, percent):
        increase = (percent/100) * self.salary

        self.salary += increase
        print(self.salary)

E1 = Employee("Nitin", 100)
E1.show_details()
E1.increase(20)
