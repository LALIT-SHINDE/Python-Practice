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
s = 'Programming'
v = 'AEIOUaeiou'
j = ''
for i in s:
    if i not in v:
        j = j + i
    
print(j)

#24 Find the largest character (ASCII order)
a = '8ehwjkehaGdhBC!WY*9'
b = a[0]
for i in a:
    if i > b:
        b = i

print(f"{b} {ord(b)} is largest ASIIC Number in String {a}")

#25 Find the smallest character (ASCII order)
c = a[0]
for i in a:
    if i < c:
        c = i

print(f"{c} {ord(c)} is smallest ASIIC Number in String {a}")

#26String formatting with f-strings
h = 'Hello'
b = 'python'
print(f"{h} there, i am learning {b} language")

#27 Student report card formatting
name = "LALIT SHINDE"
std = "10th"
age = 16
div = "B"

print("-------- Student Info --------\n")
print(f"NAME: {name}\nAge: {age}\nSTD: {std}\nDiv: {div}")
print("------------------------------")

p = 'python'
m = 94
mat = 'math'
ma = 43
print(f"Subject  \t  Marks\n")
print(f"{p}  \t   {m}")
print(f"{mat}   \t\t   {ma}")
print("------------------------------\n")


#28 Count frequency of every character
s = "banana"
p = ""
for i in s:
    if i not in p:
        count = 0

        for j in s:
            if i == j:
                count += 1

        print(f"{i} is repeaed {count} times")
        p += i

#29
s = 'Banana'
p = ""

for i in s:
    if i not in p:
        count = 0
        for j in s:
            if i == j:
                count += 1
                
        print(f"{i} is repeted {count} time in {s}")
        p += i









