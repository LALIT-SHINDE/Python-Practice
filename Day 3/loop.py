x = [1, 3.5, 43j, "Hi", "fsa"]
print(x)

for i in x:
    print(i)

for i in range(len(x)):
    print([i])

new = ["apple", "banana", "cherry", "Mango"]
j = 0
while j < len(new):
    print(new[j])
    j += 1

new = ["apple", "banana", "cherry", "Mango"]
[print(x) for x in new]