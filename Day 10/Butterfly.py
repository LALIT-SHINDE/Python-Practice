n = 10

#upper Half
for row in range(n):
    stars = row + 1
    space =  2 * (n - stars)

    for clo in range(row + 1):
        print("*",end=" ")
        
    for clo in range(space):
        print(" ",end=" ")

    for clo in range(row + 1):
        print("*",end=" ")
    print()

#Lower Half
for row in range(1, n):
    sp = 2 * row  

    for clo in range(n - row):
        print("*",end=" ")

    for clo in range(sp):
        print(" ",end=" ")

    for clo in range(n - row):
        print("*",end=" ")
    print()