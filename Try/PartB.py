# part B 
# 6 
num = int(input("Enter the number: "))
n = num
re = 0

while num != 0:
    la = num % 10
    re = re * 10 + la

    num //= 10
print(f"Number {n} Reverse is {re}")

# 7

num = int(input("Enter the number: "))
re = 0
n = num

while num != 0:
    la = num % 10
    re = re * 10 + la
    num //= 10

if n == re:
    print(f"Number {n} is palimdrome")
else:
    print(f"Number {n} is not a palimdrome")

# 8
num = int(input("Enter the number: "))
large = 0
n = num

while num != 0:
    la = num % 10
    if la > large:
        large = la
    num//=10

print(f"The largest digit in number: {n} is {large}")

#9
num = int(input("Enter the number: "))
n = num
small = 9

while num != 0:
    la = num % 10
    if la < small:
        small = la
    num = num // 10

print(f"The samllest Digit in number {n} is {small} ")

#10

num = int(input("Enter the number: "))
sum = 0
n = num
while num != 0:
    la = num % 10
    sum += la
    num //= 10

print(f"Total sum of the digits of {n} is {sum}")

#11
num = int(input("Enter the value: "))
n = num 
pro = 1

while n != 0:
    la = n % 10
    pro *= la
    n //= 10

print(f"Total Product of the digits of {num} is {pro}")

#12 Armstrong number
num = int(input("Enter the number: "))
n = num
sum = 0

while n != 0:
    la = n % 10
    fac = la * la * la
    sum += fac
    n //= 10

if num == sum:
    print(f"{num} is a Armstorng number")
else:
    print(f"{num} is not a Armstorng number")

#13 strong number
n = int(input("Enter the number: "))
num = n
sum = 0

while n != 0:
    la = n % 10

    fact = 1
    for _ in range(la):
        fact = fact * la 
        la = la - 1
    print(fact)

    sum += fact
    n//=10

if num == sum:
    print(f"{num} is a storng number")
else:
    print(f"{num} is not a strong number")

#14 perfect number
num = int(input("Enter the nummber: "))
n = num
sum = 0

for i in range(1,num):
    if num % i == 0:
        sum += i

print(sum)
if n == sum:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")

#15 multipication table
num = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")