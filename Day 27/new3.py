# 24. Reverse a String
s = input("Enter the string: ")
new = ""

for i in range(len(s)-1, -1, -1):
    new += s[i]

s = new
print(s)

#or
s = input("Enter the string: ")
li = list(s)

l = 0
r = len(s) - 1

while l < r:

    li[l], li[r] = li[r], li[l]
    # temp = li[l]
    # li[l] = li[r] can use this methode also.
    # li[r] = temp

    l += 1
    r -= 1

s = "".join(li)

print(s)

# 25. Count Characters
