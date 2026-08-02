num = int(input("Enter the number: "))
n = num
total = 0

while num != 0:
    current = num % 10
    c = current
    fact = 1
    for i in range(current):
        fact *= current 
        current -= 1
    print(f"{c}! = {fact}")

    total += fact 
    num //= 10

if n == total:
    print(f"{total} is a strong number")
else:
    print(f"{total} is not a strong number")