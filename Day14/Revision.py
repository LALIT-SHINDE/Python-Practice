#Part A
#1
print("Hello, World!")

#2
a = int(input("Enter The 1st no: "))
b = int(input("Enter the 2nd no: "))
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
if b == 0:
    print(f"{a} / {b} = undifine")
else:
    print(f"{a} / {b} = {a/b}")

#3
a = 4.65
b = 5.89
print(int(a), int(b))

#4
a = 4
b = 5
print(f"a: {a}, b: {b}")
a, b = b, a
print(f"a: {a}, b: {b}")

#or
a = 4
b = 3

print(f"a: {a}, b: {b}")

a = a + b
b = a - b
a = a - b
print(f"a: {a}, b: {b}")

#5
a = 10
b = 3.14
c = "Hello"
d = True
print(f"{a}: {type(a)}")
print(f"{b}: {type(b)}")
print(f"{c}: {type(c)}")
print(f"{d}: {type(d)}")

#6
a = int(input("Enter the 1st no: "))
b = int(input("Enter the 2nd no: "))
c = int(input("Enter the 3rd no: "))
if b < a > c:
    print(F"A: {a} is the largest no.")
elif a < b > c:
    print(F"B: {b} is the largest no.")
elif a < c > b:
    print(f"C: {c} is the largest no.")
elif a == b > c:
    print(f"A: {a} and B: {b} both are equal and largest than C: {c}")
elif a < b == c:
    print(f"B: {b} and C: {c} both are equal and largest than A: {a}")
elif a == c > b:
    print(f"A: {a} and C: {c} both are equal and largest than B: {b}")
else:
    print(f"A: {a}, B: {b} and C: {c} are Equal")

#7 
year = int(input("Enter any Year: "))
if year % 4 == 0:
    print(f"{year} is a Leap Year")

elif year % 100 == 0:
    print(F"{year} not a Leap year")

elif year % 400 == 0:
    print(f"{year} is a Leap Year")

else:
    print(F"{year} not a Leap year")

#8
unit = float(input("Enter your eletrical bill in Unit: "))
slab_rate = int(input("Enter your slab Rate: "))
FPPCA = 53.2
fixed_rate = 47.96
electric_bill = 89.3

total_rate = (unit * slab_rate) + fixed_rate + electric_bill  + FPPCA
print(F"Total Eletrical Bill : {total_rate}")

#9
s = str(input("Enter single character: "))
a = "AEIOUaeiou"
if s in a:
    print(f"{s} is a Vowle")
elif s not in a and s.isalpha():
    print(f"{s} is a consonant")
elif s.isdigit():
    print(f"{s} is a Digit")
else:
    print(f"{s} is a Special Character")

#10
a = int(input("Enter the 1st value: "))
b = int(input("Enter the 2nd value: "))
c = str(input("Enter the operatoer +, -, *, or / :"))
if c == "+":
    print(f"{a} + {b} = {a+b}")
elif c == "-":
    print(f"{a} - {b} = {a-b}")
elif c == "*":
    print(f"{a} * {b} = {a*b}")
elif c == "/":
    if b == 0:
        print(f"{a} / {b} == Undifined")
    else:
        print(f"{a} / {b} = {a/b}")
else:
    print("Invaild Operator")



