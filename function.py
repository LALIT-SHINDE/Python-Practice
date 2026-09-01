#1
def my_function():
    return "Hello world!"
print(my_function())

#2
def my(a):
    return a
print(my("Lalit"))

#3
def my1():
    for i in range(1,11):
        print(i)
my1()

#4
def my2():
    for i in range(0,50,2):
       print(i)
my2()

#5
def my8():
    for i in range(1,50,2):
        print(i)
my8()

#6
def my3():
    for i in range(1,11):
        print(f"{7} * {i} = {7*i}")
my3()

#7
def my4():
    print("Vowles: A E I O U")
my4()

#8
def my5():
    for i in range(1, 11):
        print(f"{i} Square = {i*i} or {i**2}")
my5()

#9
def my6():
    for i in range(1,11):
        print(f"{i} cube = {i**3}")
my6()

#10
def my7(n):
    for row in range(n):
        for i in range(row + 1):
            print("*",end=" ")
        print()
my7(5)

