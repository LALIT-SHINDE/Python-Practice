arr = [1,2,3,4,5,6]

li = 0
lii = 1

sort = False

while lii != len(arr):
  if arr[li] < arr[lii]:
    sort = True
    lii += 1

  else:
    break

if sort:
  print(arr, ": array is sorted")

else:
  print(arr, ": array is not sorted")
