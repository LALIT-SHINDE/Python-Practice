#1 sum of even numbers 1 to n

n = int(input("Enter the value: "))
total = 0
for i in range(2, n+1, 2):
    total += i

print(total)

#2 fibonacci series from 0 to n
n = int(input("Enter the number: "))
a = 0
b = 1
while a <= n:
    print(a)
    a, b = b, a+b

#3 prime 
n = int(input("Enter the number: "))

if n <= 1:
    print(f"{n} is not a Prime Number")
else:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    
if prime:
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is not a Prime Number")

