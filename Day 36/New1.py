#7. Find duplicate
arr = [1,1,3,4,0,2]
new = []
a = []

for i in arr:
    if i not in new:
        new += [i]

    else:
        a += [i]
        
print(f"Duplicate: {a}")

# Time complexity : O(n)
# space Complexity : O(n**2)


#8. Frequency of elements
arr = [1,3,2,1,2,1,0]
new = []

for i in arr:
    count = 0

    if i not in new:

        for j in arr:
            if i == j:
                count += 1

        new += [i]
        print(f"{i} : {count}")

# Time complexity : O(n)
# Space Complexity : O(n)


#9. Linear search
arr = [4,2,3,5,2,6,7,1,0]
find = 7

for i in range(len(arr)):
    if find == arr[i]:
        print(f"{find}: Found at {i}th Position !!")
        break

# Time complexity : O(n) worst case   O(1) best case
# Space complexity : O(1)

#10. Two-pointer problem i didnt undestand the quetion.

a = [1,2,3,4,5]
print(a)

temp = a[-1]

for i in range(len(a)-1,0,-1):
    a[i] = a[i-1]

a[0] = temp
print(a)

while True:
    n = int(input("Enter the Number: "))
    arr = [1,2,3,4,5]

    if n <= 10:
        rotate = 0

        while n != rotate:
            temp = arr[-1]

            for i in range(len(arr)-1, 0, -1):
                arr[i] = arr[i-1]

            arr[0] = temp

            rotate += 1

        print(arr)

    else:
        print("Exit........")
        break
