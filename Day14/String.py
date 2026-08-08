#1
n = "Python"
print(len(n))

#2
print(n[0])
print(n[-1])

#3
for i in n:
    print(i)

#4
name = "LaliIt"

n = name.lower()
count = 0

for i in name :
    if i == "a" or i == "o" or i == "u" or i == 'e' or i == 'i':
        count += 1
    else:
        pass

print(count)

#5
name = "LalIt"
upper = 0
lower = 0
for i in name:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    else:
        pass
print("upper : ",upper)
print("lower : ", lower)

#6
n = "lalit"
n = n.upper()
print(n)

#7
n = n.lower()
print(n) 

#8
n = "  Python  "
print(n.strip())

#9
n = "Python Programming"
print(n.replace(" ", "-"))

#10
if n[0] == "P" and n[1] == "y":
    print(f"String {n} start with Py")
else:
    print(f"String {n} is not start with Py")

if n[-1] == "g" and n[-2] == "n" and n[-3] == "i":
    print(f"String {n} end with ing")
else:
    print(f"String {n} is not end with ing")

#11
count = 0
name = "BAnana"

name = name.lower()
a = input("Enter the charater you want to search: ")

for i in name:
    if i == a:
        count+= 1
print(count)
          
#12
name = "Lalaiat"
a = input("Enter the charater you want to find: ")

for i in range(len(name)):
    if name[i] == a:
        print(f"{a} in the name: {name} at Index: {i}")
        break

#13
print(name)
for i in range(len(name)-1,-1,-1):
    if name[i] == a:
        print(f"{a} the last occurance of char: {a} is in index: {i}")
        break

#14
string = "Python Programming" 
substring = input("Enter the substring: ")

if substring in string:
    print(f"{substring} is the substring of string: {string}")

else:
    print(f"{substring} is not the substring of string: {string}")

#15
sen = "I am the king of the world"
a = sen.split()
count = 0

for i in a:
    count += 1 

print(count)

#16
string = "Lalit"
s = string[::-1]
print(s)

#17
string = "LAlit"
s = list(string)

l = 0
r = len(string) - 1

while l < r:
    s[l], s[r] = s[r], s[l]

    l += 1
    r -= 1

a = "".join(s)
print(a,type(a))
