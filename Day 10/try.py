n = 10
for row in range(n):
    space = n - row - 1
    stars = 2 * row + 1
    for clo in range(space):
        print(" ",end=" ")

    for clo in range(stars):
        if row == 0 or row == n-1 or clo == 0 or clo == stars-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()

n = 10
for row in range(n):
    space = row
    stars = (2 * n - 1) - (2 * row)

    for clo in range(space):
        print(" ",end=" ")

    for clo in range(stars):
        if row == 0 or row == n-1 or clo == 0 or clo == stars-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    








