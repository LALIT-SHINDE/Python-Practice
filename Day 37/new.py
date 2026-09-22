# Problem 1 — Sum
arr = [5, 10, 15, 20, 25]
total = 0

for i in arr:
    total += i

print(total)

# Time = o(n)
# space = o(1)

# Problem 2 — Count Odd Numbers
arr = [12, 7, 5, 20, 33, 40, 9]
count = 0

for i in arr:
    if i % 2 != 0:
        count += 1

print(count)

# Time = o(n)
# space = o(1)

# Problem 3 — Minimum
arr = [45, 12, 89, 3, 67, 21]
mini = arr[0]

for i in arr:
    if mini> i:
        mini = i
print(mini)

# Time = o(n)
# space = o(1)

# Problem 4 — Maximum
arr = [14, 72, 9, 56, 91, 32]
maxi = arr[0]

for i in arr:
    if maxi < i:
        maxi = i

print(maxi)

# Time = o(n)
# space = o(1)

# Problem 5 — Linear Search
arr = [10, 25, 30, 45, 50, 60]
target = 45

for i in arr:
    if target == i:
        print("Found")
        break

else:
    print("Not Found")

# time = Best case O(1)   worst case O(n)
# space = o(1)

# Problem 6 — Reverse an Array
arr = [10,20,30,40,50,60]
l = 0
r = len(arr) - 1

while l < r:
    arr[l], arr[r] = arr[r], arr[l]

    l += 1
    r -= 1

print(arr)

# Problem 7 — Count Occurrences



arr = [2, 5, 2, 8, 2, 9, 5, 2]
target = 2
count = 0

for i in arr:
    if target == i:
        count += 1

print(count)

# Problem 8 — Find Second Largest

arr = [10, 25, 8, 40, 30, 40] 
maxi = arr[0]
maxi2nd = arr[0]

for i in arr:
    if maxi < i:
        maxi2nd = maxi
        maxi = i

    elif maxi2nd < i and maxi != i:
        maxi2nd = i

print(maxi, maxi2nd)

# problem 9 — Copy an Array

arr = [10, 20, 30, 40, 50]
new = []

for i in arr:
    i *= 2
    new += [i]

print(new)

# Time = o(n)
# space = o(n)

# Problem 10 — DSA Complexity Challenge

arr = [10, 20, 30, 40, 50]

count = 0

for i in arr:   # Time = o(n)
    count += 1

for i in arr:    # time = o(n2)
    for j in arr:
        count += 1

# O(n) + O(n2) = O(2n2)
# space = O(1)
