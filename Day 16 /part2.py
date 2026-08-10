
#21
def sumof(a, b):
    return a+b
z = 5
y = 3
print(f"{z} + {y} = {sumof(z,y)}")

#22
def large(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(large(8,7,9))

#23
def prime(n):
    if n <= 1:
        isprime = False
    else:
        isprime = True
        for i in range(2,n):
            if n % i == 0:
                isprime = False
                break
    if isprime:
        return "Is a prime number "
    else:
        return "Is not a prime number "
a = int(input("Enter the number: "))
print(prime(a))

#24
def reverse(a):
    s = a[::-1]
    return s
k = "HELLO"
print(reverse(k))

#25
def vowels(a):
    count = 0
    for i in a:
        if i in "AEIOUaeiou":
            count += 1
    return count
k = "Hlloai"
print(vowels(k))

#26
def s(a):
    total = 0
    for i in a:
        total += i
    return total
k = [1,2,3,4,5,6,7,8,9]
print(s(k))
