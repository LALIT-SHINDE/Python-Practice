
s = ['H','e','l','l','o']

s = s[::-1]
print(s)

s[:] = s[::-1]
print(s)

left = 0
right = len(s) - 1

while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
    
print(s)
x = 12321
s = x
reverse = 0

while s != 0:
    last_digit = s % 10 
    reverse = reverse * 10 + last_digit
    s //= 10

if reverse == x:
    print(True)
else:
    print(False)

x = 1214121
a = str(x)

print(a == a[::-1])
