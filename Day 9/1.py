n = int(input("Enter the number: "))
count = 0

for i in range(2, n+1):
    prime = True
    
    for j in range(2, n):
         if i % j == 0:
            prime = False
            break
    if prime:
        prime = True
        count =+ 1
print(count)



