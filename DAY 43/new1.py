arr = [2,1,2,0,2,1,0,0,2,1]
new = []

while len(arr) != 0:
    mini = arr[0]

    for i in arr:
        if mini > i:
            mini = i

    arr.remove(mini)
    new += [mini]

print(new)
