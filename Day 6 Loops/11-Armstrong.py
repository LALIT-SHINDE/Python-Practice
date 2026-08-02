num = int(input("Enter the number: "))
sum = 0
num1 = num

while num != 0:
    last_digit = num % 10
    total = last_digit *  last_digit * last_digit

    sum += total
    num //= 10

if num1 == sum:
    print(f"{num1} is Armstrong")
else:
    print(f"{num} is not an Armstrong")