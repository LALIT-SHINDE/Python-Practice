#1
n = int(input("Enter the number:"))
total = 0

for i in range(0, n+1, 2):
    total += i
print(total)

#2
total = 0
for i in range(2, n+1, 2):
    total += i

print(f"addition of odd numbers between 1 to {n} is {total}")

#methode 2
total = 0
for i in range(1,n+1):
    if i % 2 != 0:
        total += i

#3
total = 1
for i in range(1, n+1):
    total *= i
print(f"product of a number between 1 to {n} are {total}")

#4
num = int(input("Enter the number: "))
n = num
count = 0
while num != 0:
    la = num % 10
    if la % 2 == 0:
        count += 1
    num //= 10

print(f"total Even number in {n} are {count}")

#5
n1 = n
count = 0
while n != 0:
    la = n % 10
    if la % 2 != 0:
        count += 1
    n //= 10
print(f"total Odd number in {n1} are {count}")