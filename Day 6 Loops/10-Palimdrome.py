num = int(input("Enter any number: "))
reverse = 0
num1 = num

while num != 0:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num = num // 10

if num1 == reverse:
    print(f"{num1} is Palimdrome")
else:
    print(f"{num1} is not Palimdrome")
