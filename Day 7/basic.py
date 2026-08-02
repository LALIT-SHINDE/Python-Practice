#1
n = int(input("Enter the value: "))

for i in range(1,n+1):
    print(i)

#2
print("reverse")
for i in range(n,0,-1):
    print(i)

#3
print("Numers that divisible by 3")
for i in range(1,101):
    if i % 3 == 0:
        print(i)

#4
print("Numers that divisible by 3 and 5")
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#5
print("Numers that divisible by 7")
count = 0
for i in range(1,101):
    if i%7 ==0:
        print(i)
        count += 1
print(f"{count} numbers are divisible by 7 between 1 to 100 ")