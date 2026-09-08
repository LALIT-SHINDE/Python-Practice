l = [3,8,9,3,4,2,1,9,5,4,7,6]
mini = l[0]

for i in l:
    if mini > i:
        mini = i

print(mini)

l = [3,8,9,3,4,2,1,9,5,4,7,6]
new = []

while len(l) != 0:
    mini = l[0]

    for i in l:
        if mini > i:
            mini = i

    new += [mini]

    temp = []
    for i in l:
        if i != mini:
            temp += [i]
            
    l = temp

l = new
print(l)
