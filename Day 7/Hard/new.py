n = int(input("Enter the value: "))
large = 0

while n != 0:
    current = n % 10
    if current > large:
        large = current
    n //= 10

print(large)

num = int(input("Enter the value: "))
small = 9
while num != 0:
    current = num % 10
    if current < small:
        small = current
    num //= 10

print(small)