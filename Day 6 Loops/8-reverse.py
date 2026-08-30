#check prime Number
num = int(input("Enter the number: "))
if num <= 1:
    print(f"{num} is not a Prime Number")

else:
    prime = True 
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break

if prime:
    print(f"{num} is a Prime number")
else:
    print(f"{num} is not a Prime number")

#count  and print all the prime number for 1 to n
n = int(input("Enter the number: "))
count = 0

print(f"Prime numbers 1 to {n}")
for i in range(2, n+1):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)
        count += 1
print(f"{count} numbers of prime number in between {n}")


        
