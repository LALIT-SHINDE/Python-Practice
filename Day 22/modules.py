
#6
# calculator.py
# def add(*n):
#     total = 0
#     for i in n:
#         total += i

#     return f"Addition of {n}: {total}"

# def subtract(*n):
#     total = 0
#     for i in n:
#         total -= i

#     return f"Substration of {n}: {total}"

# def multiply(*n):
#     total = 1
#     for i in n:
#         total *= i
#     return f"Multification of {n}: {total}"

# def divide(*n):
#     total = n[0]
#     try:
#         for i in n[1:]:
#             total /= i
#         return f"Divison of {n}: {total}"

#     except ZeroDivisionError:
#         print("Error: Can not Divided BY Zero")

import calculator
a = calculator.add(1,2,3,4,5,6)

print(a)
print(calculator.subtract(90,12,30,18,20))
print(calculator.multiply(90,12,30,18,20))
print(calculator.divide(1,2,3,4,5,6))

#7
# math_operations.py

# def square(num):
#     return f"Square of a {num} is {num*num}"

# def cube(num):
#     return f"Cube of a {num} is {num**3}"

from math_operations import square

n = 8
print(square(n))

#8
import math as m

print(m.sqrt(144))
print(m.factorial(5))
print(m.pi)

#9
# student.py
# def display_student(a,b):
#     return f"Name: {a} and Course: {b}"

# name = "Lalit"
# course = "MCA"
# display_student(name,course)
from student import name, course, display_student

print(display_student())

# method2 : Change data
import student 

student.name = "jani"
student.course = "Bca"
print(student.display_student())


#10
# 1st i have give file name as test.py but it was showing some errors so i change it to test1.py
# test1.py
# def hello():
#     return f"Hello, World"

# if __name__ == "__main__":
    #  print("This file is being executed directly")
#     hello()
import test1
test1.hello()



