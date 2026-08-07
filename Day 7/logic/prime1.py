num = int(input("Enter the Number: "))
n = num
if num <= 1:
    prime = False
    print(f"{num} is not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
        else:
            prime = True
            
if prime:
    print(f"{n} is a prime Number")
else:
    print(f"{n} is not a prime Number")
