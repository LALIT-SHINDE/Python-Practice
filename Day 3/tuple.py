a = ('a', 1, 2, 3, 4)
print(a)

for x in range(len(a)):
    print(x, a[x])

i = 0
while i < len(a):
    print(a[i])
    i += 1

b = a * 2
print(b)