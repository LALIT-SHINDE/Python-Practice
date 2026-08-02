#16 fibonacci number
num = int(input("Enter the number: "))
a = 0
b = 1

while a <= num:
    print(a)
    c = a + b
    b = a
    a = c
    