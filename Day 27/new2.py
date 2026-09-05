# 16. Square Pattern
n = 5

for _ in range(n):
    for _ in range(n):
        print("*", end=" ")
    print()

# 17. Right Triangle
n = 5
for row in range(n):
    for _ in range(row + 1):
        print("*",end=" ")
    print()

# 18. Inverted Triangle
n = 5
for row in range(n):
    for _ in range(n - row):
        print("*",end =" ")
    print()

# 19. Pyramid
n = 5
for row in range(n):
    space = n - row - 1
    stars = 2 * row + 1
    
    for _ in range(space):
        print(" ",end = " ")

    for _ in range(stars):
        print("*",end=" ")

    print()

# 20. Hollow Square
n = 5
for row in range(n):
    for clo in range(n):
        if row == 0 or row == n-1 or clo == 0 or clo == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
