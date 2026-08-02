# Answer for Part A
for i in range(1,101):
    print(i)

for i in range(100,0,-1):
    print(i)

for i in range(1,101):
    if i % 7 == 0:
        print(i)
        
#sum of even no
n = int(input("Enter the Number: "))
sum = 0
for i in range(2,n+1,2):
    sum += i

num =int(input("Enter the number: "))
n = num
count = 0
while num != 0:
    la = num % 10
    print(f"{la}")
    count += 1
    num //= 10

print(f"The total digit in {n} are {count}")