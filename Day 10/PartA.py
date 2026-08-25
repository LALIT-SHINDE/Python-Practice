
#1 sqaure
n = 5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

#2 right
n = 5
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

#3 Left
n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

# 4 number triangel
n = 6
for i in range(1, n):
    for j in range(1, i+1):
        print(j,end=" ")
    print()

#5 number repated
n = 6 
for i in range(1,n):
    for j in range(1, i+1):
        print(i,end=" ")
    print()

#6 Floyd's Triangle
n = 6
current = 1
for i in range(1, n):
    for j in range(1, i+1):
        print(current,end=" ")
        current += 1
    print()
