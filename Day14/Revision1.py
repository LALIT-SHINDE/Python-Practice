
#11
for i in range(1,101):
    if i  % 3 == 0 and i % 5 == 0:
        print(i)

#12
n = int(input("Enter the number: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i

print(f"{n}! = {fact}")

#13
for num  in range(1, 101):
    if num == 1:
        prime = False
    else:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
    if prime:
        print(num)

#14
num = int(input("Enter the Number: "))
print(num)
reverse = 0
while num != 0:
    current = num % 10
    reverse = reverse * 10 + current

    num = num // 10

print(reverse)

#15
n = int(input("Enter the number: "))
num = n
a = str(n)
sum = 0

while n != 0:
    current = n % 10
    total = current ** len(a)
    sum += total

    n //= 10
if num == sum:
    print(f"{num} is a Armstrong number")
else:
    print(f"{num} is not a Armstrong number")

#16
num = int(input("Enter the number: "))
num1 = num
total = 0

while num != 0:
    current = num % 10
    if current % 2 == 0:
        total += current

    num //= 10

print(f"Addition of Even digits in number {num1} is {total}")


#17
num = int(input("Enter the nummber: "))
num1 = num
count = 0

while num != 0:
    current = num % 10

    if current <= 1:
        prime = False
    else:
        prime = True
        for i in range(2, current):
            if current % i == 0:
                prime = False
                break
        if prime:
            count += 1

    num //= 10
print(f"There are {count} prime digits in {num1}")
