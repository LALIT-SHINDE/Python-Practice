# large
num = int(input("Enter the value: "))
n = num
large = 0

while num != 0:
    current = num % 10

    if large < current:
        large = current
    
    num = num // 10
print(f"Large digit in number: {n} is {large}")

#small
num = int(input("Enter the number: "))
n = num
small = 9

while num != 0:
    current = num % 10

    if current < small:
        small = current
    
    num //= 10
print(f"Small digit in number: {n} is {small}")
    
#sum
num = int(input("Enter the number: "))
n = num
total = 0

while num != 0:
    current = num % 10
    total += current
    num //= 10

print(f"Sum of digits in number {n} is a {total}")

