n = int(input("Enter any number: "))
f = 1

for i in range(n):
    f = f * n
    n = n - 1
    print(f)
