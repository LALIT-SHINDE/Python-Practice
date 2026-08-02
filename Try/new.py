n = int(input())
fact = 1

for _ in range(n):
    print(n)
    fact *= n
    n = n -1

print(fact)