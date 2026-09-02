#6. Sum of Numbers
# Take n and calculate:

n = int(input("Enter the Number: "))
count = 0

for i in range(n+1):
    count += i

print(count)

# 7. Factorial
# Find the factorial of a number using a while loop.
num = int(input("Enter the number: "))
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print(fact)

fact = 1

for i in range(1, num + 1):
    fact *= i

print(fact)

# 8. Reverse a Number
num = int(input("Enter the number: "))
rev = 0
print(num)

while num != 0:
    rev = rev * 10 + num % 10
    num //= 10

print(rev)

# 9. Count Digits
num = int(input("Enter the Number: "))
count = 0

while num != 0:

    count += 1
    num //= 10

print(count)

#10 Prime number
num = int(input("Enter the number: "))
if num <= 1:
    prime = False

else:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

if prime:
    print(f"{num} is a Prime Number.")

else:
    print(f"{num} is not a prime Number")
        
