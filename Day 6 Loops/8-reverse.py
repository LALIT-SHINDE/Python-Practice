num = int(input("enter any number: "))
reverse = 0

while num != 0:
    la = num % 10
    reverse = reverse * 10 + la
    num = num // 10

print(f"Reverse: {reverse}")


num = int(input("enter the number: "))
count = 0

while num != 0:
    num = num // 10
    count = count + 1

print("Count: ",count)