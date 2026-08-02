#18
name = "Python"
n = name[::2]
print(n)

#19 using sliceing
name = "python"
s = ""
for i in name[::-1]:
    print(i)
    s = s + i

print(s)

#19 using range() and len()
name = "python"
s = ""
for i in range(len(name)-1,-1,-1):
   print(name[i])
   s = s + name[i]

print(s)

#20
name = "cPython "
print(name[2:8])

#21
s = input("Enter the String: ")
a = s[:]
b = s[::-1]

if a == b:
    print(f"{s} is the palimdrome")

else:
    print(f"{s} is the palimdrome")
