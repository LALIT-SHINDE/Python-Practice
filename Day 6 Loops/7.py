n = int(input("Enter any number: "))
i = 0

if n == 0:
    print("Total digits in number are 1")
else:
    while n != 0:
        n //= 10
        i += 1

    print(f"Total digits in number are {i}")