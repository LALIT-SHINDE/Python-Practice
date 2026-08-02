#4 GDC
a = int(input("Enter the 1st value: "))
b = int(input("Enter the 2nd Value: "))

if a > b:
    c = b
else:
    c = a
print(f"The Comman Factores of {a} and {b} is...")
for i in range(1, c+1):
    if a % i == 0 and b % i == 0:
        print(i)
        gdc = i
        
print(f"The GDC of {a} and {b} is: {gdc}")

#Lcm 
a = int(input("Enter the 1st value: "))
b = int(input("Enter the 2nd Value: "))

if a > b:
    c = a
else:
    c = b

i = c
while True:
    if i % a == 0 and i % b == 0:
        print(i)
        break
    i += 1
print(f"The LCM of {a} and {b} is: {i}")

#factores
n = int(input("Enter the value: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

# count prime numbers