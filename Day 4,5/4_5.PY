a = int(input("Enter the 1ST Value: "))
b = int(input("Enter the 2ND Value: "))

if a > b:
    print(f"A: {a} is greater than B: {b}")
elif a < b:
    print(f"B: {b} is greater than A: {a}")
else:
    print(f"A: {a} and B: {b} Both are Equal")

a = int(input("Enter the 1ST Value: "))
b = int(input("Enter the 2ND Value: "))
c = int(input("Enter the 2ND Value: "))

if b > a and b > c:
    print(f"B: {b} is greater than A: {a} and C: {c}")

elif a > b and a > c:
    print(f"A: {a} is greater than B: {b} and C: {c}")

elif c > a and c > b:
    print(f"C: {c} is greater than A: {a} and B: {b}")

elif a == b and b == c:
    print(f"A: {a}, B: {b}, and C: {c} are Equal to each other")