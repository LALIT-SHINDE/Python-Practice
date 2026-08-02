n = 5 
for i in range(n):
    space = n - i - 1
    stars = 2 * i + 1
    for _ in range(space):
        print(" ", end=" ")

    for _ in range(stars):
        print("*", end=" ")

    print()