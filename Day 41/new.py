# remove duplicate element 
arr = [1.2,3,4,5,1,2,3,4,5,43,12,,32,43,5]
new = []

for i in arr:
  if i not in new:
    new += i
print(new)
