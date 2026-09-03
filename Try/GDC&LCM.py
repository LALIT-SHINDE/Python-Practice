#GDC
a = int(input("Enter the 1st Number: "))
b = int(input("Enter the 2nd Number: "))

if a > b:
    c = b
else:
    c = a

print(f"Comman factores of {a} and {b}: ")
for i in range(1, c+1):
    if a % i == 0 and b % i == 0:
        print(i)
        gdc = i

print(f"{gdc} is the GDC of {a} and {b}")

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

if a > b:
    c = a
else:
    c = b

while True:
    if c % a == 0 and c % b == 0:
        print(f"LCM of {a} and {b} is {c}")
        break
    c += 1

    
