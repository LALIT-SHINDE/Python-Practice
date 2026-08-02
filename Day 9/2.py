n = int(input("Enter the number: "))
fact = 1
total = 0

for i in range(1, n+1):
    fact = fact * i
    print(f"{i}! = {fact}")

    total = total + fact

print(f"The Sum of the factorial of 1 to {n} : {total}")
