n = 5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

#Right
for i in range(n):
    for _ in range(i+1):
        print("*",end=" ")
    print()

#Left
for i in range(n):
    for _ in range(n-i):
        print("*",end=" ")
    print()

#Number triangel
count = 0
for i in range(1, n):
    for j in range(1, i+1):
        print(j,end=" ")
    print()


#Reated triangel
for i in range(1, n):
    for _ in range(1, i+1):
        print(i,end=" ")
    print()

#flo triangle
n = 6
current = 1
for i in range(1, n):
    for j in range(1, i+1):
        print(current, end =" ")
        current += 1
    print()

#pyramid
n = 5
for row in range(n):
    space = n - row - 1
    stars = 2 * row + 1
    for _ in range(space):
        print(" ",end=" ")

    for _ in range(stars):
        print("*",end=" ")

    print()

#Inverted Pyramid


#Hollow squre
n = 5
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or col == 0 or col == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#hollow rectangel
for row in range(5):
    for clo in range(8):
        if row == 0 or row == 5-1 or clo == 0 or clo == 8-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


n = 5
for i in range(n+1):
    space = i
    for j in range(space):
        print("*",end=" ")
    print()


n = 5
for row in range(n):
    space = n - row - 1
    stars = 2 * row + 1
    for _ in range(space):
        print(" ",end=" ")

    for _ in range(stars):
        print("*",end=" ")
    print()

for row in range (1, n):
    space = row 
    stars = (2 * n - 1) - (2 * row)
    for _ in range(space):
        print(" ",end=" ")

    for _ in range(stars):
        print("*",end=" ")
    print()