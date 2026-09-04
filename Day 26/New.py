# 11. Print all prime numbers between 1 and 100.
for num in range(1,101):
    if num <= 1:
        prime = False

    else:
        prime = True
        for i in range(2,num):
            if num % i == 0:
                prime = False
                break

    if prime:
        print(num)

# 12. Find the HCF/GCD of two numbers.
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
hcf = 0

c = min(a,b)

for i in range(1, c+1):
    if a % i == 0 and b % i == 0:
        hcf = i

print(hcf)

# #HCF Euclidean Algorithm
a = int(input("Enter the 1st Number: "))
b = int(input("Enter the 2nd Number: "))

while b != 0:
    reminder = a % b
    a, b = b, reminder

print(a)




# 13. LCM
m = int(input("Enter the 1st Number: "))
n = int(input("Enter the 2nd Number: "))
lcm = 0

if m > n:
    maxi = m
else:
    maxi = n

for i in range(maxi, m*n+1):
    if i % m == 0 and i % n == 0:
        lcm = i
        break

print(lcm)


# 14. Multiplication Table
# Take a number from the user and print its multiplication table from 1 to 10.

num = int(input("Enter the Number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")

# 15. Number Frequency
# Take a number and count how many times a particular digit occurs.
num = 1223445882935428

print(num)
n = int(input("Enter the Digit you want to check: "))
count = 0

for i in str(num):
    if str(n) == i:
        count += 1

print(count)

num = int(input("Enter the NUmber: "))
n = int(input("Enter a Digit: "))
count = 0

while num != 0:
    current = num % 10
    if n == current:
        count += 1


    num //= 10

print(count)

# 16. Reverse a Number
num = int(input("Enter the Number: "))
rev = 0

while num != 0:
    rev = rev * 10 + num % 10
    num//= 10

print(rev)

# 17. Palindrome Number
# Check whether a number is a palindrome.

def palin(num):
    n = num
    rev = 0

    while num!= 0:
        rev = rev * 10 + num % 10

        num //= 10

    if rev == n :
        return f"{n} is a Palindrome"
    else:
        return f"{n} is not a Palindrome"

print(palin(123432145))
print(palin(1234321))

# 18. Sum of Digits
# Take a number and find the sum of all its digits.

num = int(input("Enter the NUmber: "))
summ = 0

while num != 0:
    current = num % 10
    summ += current

    num //= 10

print(summ)

# 19. Count Digits
# Take a number and count how many digits it contains.
num = int(input("Enter the Number: "))
count = 0

while num != 0:
    count += 1
    num //= 10

print(count)


# 20. Armstrong Number
# Check whether a number is an Armstrong number.

def arm(num):
    n = num

    total = 0

    while num != 0:
        current = num % 10
        total += current**len(str(n))

        num //= 10

    if total == n:
        return f"{n} is an Armstrong Number"
    else:
        return f"{n} is not a Armstrong Number"

print(arm(153))
print(arm(12))
