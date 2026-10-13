n = [1,1,1,2,2,3,3,4,5,5,7,7,7,7,8,8,8,8,8,9]
x = int(input("Enter the number: "))

count = 0

for i in n:
    if x == i:
        count += 1

print(x,count)
