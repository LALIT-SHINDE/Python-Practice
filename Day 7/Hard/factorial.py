num = int(input("Enter the value: "))
n = num
fact = 1

for i in range(num):
    fact = fact * num    #fact *= num
    num = num - 1
print(f"{n}! : {fact}")


num = int(input("Enter any number: "))
n = num
total = 0

while num != 0:
    current = num % 10
    c = current

    fact = 1
    for _ in range(current):
        fact = fact * current
        current = current - 1
    print(f"{c}! = {fact}")

    total = total + fact
    num //= 10

if n == total:
    print(f"{n} is a strong number")
else:
    print(f"{n} is not a Strong number")