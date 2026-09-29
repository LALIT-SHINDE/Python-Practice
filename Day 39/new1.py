num = int(input("Enter any number: "))
n = num
a = str(num)
total = 0

while n != 0:
    current = n % 10

    total += current ** len(a)

    n //= 10

if num == total:
    print(f"{num}  its an armstong Number")
else:
    print(f"{num} is not an armstrong Number")
