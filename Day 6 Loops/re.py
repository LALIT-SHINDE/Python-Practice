num = int(input("Enter any number: "))
re = 0

while num != 0:
    l = num % 10
    re = re * 10 + l
    num //= 10

print(re)