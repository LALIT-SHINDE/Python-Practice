#22
s = "Python123@#"

count_d = 0
count_a = 0
count_s = 0

for i in s:
    if i.isdigit():
        count_d += 1
    elif i.isalpha():
        count_a += 1
    else:
        count_s +=1

print(f"String: {s}\nDigits: {count_d}, Alphabets: {count_a}  and  Special Charaters: {count_s}")

#23 Remove all vowels from a string.

s = "Programming"
a = list(s)
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        a.remove(i)

b = "".join(a)

print(b,type(b))

# or
v = "aeoiuAEOIU"
j = ""
for i in s:
    if i not in v:
        j = j + i

print(j)