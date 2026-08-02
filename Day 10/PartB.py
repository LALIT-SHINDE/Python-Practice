#part B
# 7. Pyramid
n = 5
for row in range(n):
    space = n - row - 1
    stars = row * 2 + 1

    for _ in range(space):
        print(" ",end=" ")

    for _ in range(stars):
        print("*",end=" ")
    print()


# 8. Inverted Pyramid
n = 5
for row in range(n):
    space = row
    stars = (2 * n - 1) - (2 * row)
    for _ in range(space):
        print(" ",end=" ")

    for _ in range(stars):
        print("*",end=" ")
    print()

#9. Hollow Square
n = 5
for row in range(n):
    for clo in range(n):
        if row == 0 or row == n-1 or clo == 0 or clo == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#10. Hollow Rectangle
n = 4
num = 8
for row in range(n):
    for clo in range(num):
        if row == 0 or row == n-1 or clo == 0 or clo == num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#11 Multiplication Table (1–10)
num = 10
for i in range(1, num+1):
    for j in range(1, num+1):
        print(f"{i} * {j} = {i*j}")
    print()

#12 Diamond
n = 10
for row in range(n):
    space = n - row - 1
    stars = 2 * row + 1

    for _ in range(space):
        print(" ",end=" ")

    for _ in range(stars):
        print("*",end=" ")

    print()

for row in range(1,n):
    space = row
    stars = (2 * n - 3) - (2 * (row - 1))

    for _ in range(space):
        print(" ",end=" ")

    for _ in range(stars):
        print("*",end=" ")
    print()




