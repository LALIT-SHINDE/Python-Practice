
#11
def my_function(name):
    print("Hello,",name)
my_function("Lalit")

#12
def my1(a,b):
    return a+b
print(my1(3,4))

#13
def my2(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both are same."
print(my2(78,78))

#14
def my3(a):
    if a % 2 == 0:
        print(f"{a} is Even")
    else:
        print(f"{a} is Odd")
my3(52)

#15
def my4(a):
    print(f"{a} = {a**2}")
b = int(input("Enter the number: "))
my4(b)

#16
def string(a):
    print(len(a))
b = input("Enter the string: ")
string(b)

#17
def string1(a):
    return a.upper()
b = input("Enter the string: ")
print(string1(b))

#18
def s(a):
    i = a[::-1]
    return i

b = input("Enter the string: ")
print(s(b))

#or

def s1(a):
    b = list(a)
    l = 0
    r = len(b) - 1

    while l < r:
        temp = b[l]
        b[l] = b[r]
        b[r] = temp

        #or b[l], b[r] = b[r], b[l]

        l += 1
        r -= 1
    
    n = "".join(b)
    print(n, type(n))
c = input("Enter the String: ")
s1(c)

#19
def me(l):
    for i in l:
        print(i)
j = ["Hi",43,"By"]
me(j)

#20
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(f"{n}! = {fact}")
n = int(input("Enter the Number: "))
factorial(n)

