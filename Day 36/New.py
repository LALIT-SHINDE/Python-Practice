# 1. Second largest element

li = [12,43,23,54,65,77,87,34,44,65,32,89,89]

maxi = li[0]
maxi2nd = li[0]

for i in li:
    if maxi < i :
        maxi2nd = maxi
        maxi = i

    elif maxi2nd < i and maxi != i:
        maxi2nd = i

print(maxi2nd, maxi)
# Time complexity : O(n)
# Space complexty : O(1)

# 2. Remove duplicates
li = [10,20,10,50,40,30,10,20,40,50,10,60,20,30,40,50,]
new = []

for i in li:
    if i not in new:
        new += [i]

li = new
print(li)

# Time complexity : O(n**2)
# Space complexty : O(n)


# 3. Check if array is sorted
def sort(choice, li):

    if choice != "Ase" and choice != "Dse":
        print("Wrong Choice, try again.....")
        return

    is_sort = True


    for i in range(len(li)):
        while i != len(li)-1:
            if choice == "Ase":
            
                if li[i] <= li[i+1]:
                    pass

                else:
                    is_sort = False
                    break

            elif choice == "Dse":
                if li[i] >= li[i+1]:
                    pass
    
                else:
                    is_sort = False
                    break

    if is_sort:
        print(f"{li} Array is Sorted ")
    else:
        print(f"{li} Array is Not Sorted")
            
    

li = [10,20,30,40,50]
sort("Ase",li)

li = [10,20,30,40,50]
sort("Dse",li)

#4. Move zeros to the end
arr = [0,2,0,3,0,0,2,1,0,3]
arr = [0,0,0,0,1]
new = []

for i in arr:
    if i != 0:
        a = i
        arr.remove(i)
        new += [a]

for i in arr:
    if i == 0:
        new += [i]
    
print(new)
# Time Complexity = O(n**2)
# Space Complexity = O(n)



# 5. Rotate the array to the right by 1 position :  i took help so dont count this one
n = int(input("Enter the number of Rotation you want: "))
arr = [1,2,3,4,5]
rorate = 0

while n != rorate:

    temp = arr[-1]

    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i-1]

    arr[0] = temp
    rorate += 1

print(arr)

# Time Complexity = O(n)
# Space Complexity = O(1)

