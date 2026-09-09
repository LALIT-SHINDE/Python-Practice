class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Lalit", 22)

print(s1.name)
print(s1.age)

s1.name = "sumit"
print(s1.name)

s1.age = 23
print(s1.age)

print(s1.name,s1.age)

class Animal:
    species = "Human" # class property

    def __init__(self, name):#object/instance property
        self.name = name 

A1 = Animal("Toby")
A2 = Animal("Yobt")

print("Class Properties: ")
print(A1.name)
print(A2.name)
print("\nInstance Properties:")
print(A1.species)
print(A2.species)

class person:
    lastname =""

    def __init__(self, name):
        self.name = name

p1 = person("toby")
person.lastname ="Toby"

print(p1.lastname, p1.name)



class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = person("lalit", 22)
print(p1)

1. Basic Class & Object

Create a Student class with:

name
age
course

Create two objects and print their details.

class Student:
    name = "Lalit"
    age = 22
    course = "MCA"

s1 = Student()
print(s1.name, s1.age, s1.course)

s2 = Student()
s2.name = "Sumit"
s2.age = 21
s2.course = "BCA"

print(s2.name, s2.age, s2.course)

2. Constructor Practice

Create a Car class whose __init__() takes:

brand
model
price

Create an object and display all three properties.

class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(self.brand, self.model, self.price)

c1 = Car( "Tata", "Safari", 400000)
c1.display()

# 3. Instance Method
# Create a Person class with:

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old.")

p1 = Person("lalit", 22)
p1.greet()

#4. Modify Object Properties

# Create a BankAccount class with:

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def show(self):
        print(f"Account Holder: {self.account_holder}\nBalance: {self.balance}\n")
        
b1 = BankAccount("LALIT", 50000)
b1.show()

b1.balance = 60000
b1.show()

# 5. Multiple Objects

# Create an Employee class with:

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def show(self):
        print(f"Name: {self.name}\nSalary: {self.salary}\nDepartment: {self.department}\n")

    

e1 = Employee("Lalit", 40000, "IT")
e2 = Employee("Sumit", 50000, "BPO")
e3 = Employee("Nitin", 6000, "IT")

e1.show()
e2.show()
e3.show()

elm = [e1, e2,e3]
high = max(elm, key = lambda  x: x.salary)

print(f"Employee with highest salary: ")
high.show()


Methode one use if else
if e1.salary < e2.salary and e3.salary < e2.salary or e1.salary == e3.salary:
    high = e2.salary

elif e2.salary < e1.salary and e3.salary < e1.salary or e3.salary == e2.salary:
    high = e1.salary

elif e1.salary < e3.salary and e2.salary < e3.salary or e2.salary == e1.salary:
    high = e3.salary

elif e1.salary > e2.salary and e3.salary == e2.salary:
    high = e2.salary, e3.salary    

elif e2.salary > e1.salary and e1.salary == e3.salary:
    high = e3.salary, e1.salary

elif e3.salary > e2.salary and e1.salary == e2.salary:
    high = e1.salary, e2.salary

else:
    high = e1.salary == e2.salary == e3.salary,"All salaries are same"

print(f"\nHighest salary: {high}")

Method 2 max()

# 6. Instance Method With Calculation

# Create a Rectangle class with

class Rectangle:
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight

    def area(self):
        print(f"Area: {self.hight * self.width}")

    def perimeter(self):
        print(f"Perimeter: {2 * (self.hight + self.width)}")

R1 = Rectangle(10,20)
R1.area()
R1.perimeter()

# 7 Class Property / Class Variable ⭐

# Create a Student class with:

class Student:
    school = "ABC School."

s1 = Student()
s2 = Student()
s3 = Student()

print(Student.school, s1.school, s2.school, s3.school)

