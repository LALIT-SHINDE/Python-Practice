# Factorial number
num = int(input("Enter the Number: "))
fact = 1

for i in range(1,num+1):
    fact = fact * i

print(f"{num}! is {fact}")

# sum of Factorial number series from 1 to n using one loop
n = int(input("Enter the number: "))
total = 0
fact = 1

for i in range(1, n+1):
    fact *= i

    print(f"{i}! is {fact}")
    total += fact

print(f"Sum of factorial series 1 to {n} : {total}")


# sum of Factorial number series from 1 to n using tow loop
n = int(input("Enter the number: "))
total = 0

for i in range(1, n+1):
    fact = 1

    for j in range(1, i+1):
        fact = fact * j
        
    print(f"{i}! is {fact}")
    total += fact

print(f"Sum of factorial series 1 to {n} : {total}")


# Resvers Number
n = int(input("Enter the value: "))
num = n
reverse = 0

while n != 0:
    current = n % 10
    reverse = reverse * 10 + current
    n = n // 10

print(f"Number: {num}\nReverse Number: {reverse}")

