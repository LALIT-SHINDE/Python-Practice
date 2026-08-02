n = 5
for i in range(n):
    space = n - i - 1
    stars = 2 * i + 1
    for _ in range(space):
        print(" ",end=" ")

    for _ in range(stars):
        print("*",end=" ")
    print()

for i in range(1, n):
    stars = (2 * n - 1) - (2 * i)
    for _ in range(i):
        print(" ",end=" ")

    for _ in range(stars):
        print("*",end=" ")
    print()

n = 5
for i in range(n):
    stars = i * 2 + 2
    space = (n * 2) - stars

    for _ in range(i + 1):
        print("*",end=" ")

    for _ in range(space):
        print(" ",end=" ")

    for _ in range(i + 1):
        print("*",end=" ")
    print()

for i in range(1, n):
    space = i * 2
    
    for _ in range(n - i):
        print("*",end=" ")

    for _ in range(space):
        print(" ",end=" ")

    for _ in range(n - i):
        print("*",end=" ")
    print()