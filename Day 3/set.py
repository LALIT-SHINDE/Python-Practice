a = {1, 2, 3, 4, 5}
print(a)

for i in a:
    print(i)

b = list(a)
i = 0
while i < len(b):
    print(i, b[i])
    i += 1
