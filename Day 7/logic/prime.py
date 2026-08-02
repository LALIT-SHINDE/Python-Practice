n = int(input("Entre A Number: "))
count = 0
if n <= 1:
    print(f"{n} is not a Prime Number")
else:
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False
            break
    count += 1
            
    
print(count)
if prime:
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is not a Prime Number")



