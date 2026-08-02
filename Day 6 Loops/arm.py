num = int(input("Enter the value: "))
num1 = num
sum = 0
while num != 0:
    la = num % 10
    total = la * la * la

    sum = sum + total
    num = num // 10
    print(f"Digit {la} : Cube {total} : sum {sum}")

if num1 == sum:
    print(f"{num1} is An Armstrong Number: {num1} is Equal to {sum}")
else:
    print(f"{num1} is not a Armstrong Number")

