#1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Amit", 21)
print(s1.name, s1.age)

#2
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

c1 = Car("BMW","Black")
print(c1.brand, c1.color)

#3
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

s1 = Person("John")
s1.greet()

