a = lambda x : x ** 2
print(a(4))

b = lambda x : x ** 3
print(b(8))


c = lambda a,b,c : a+b+c 
print(c(1,2,3))

def new(n):
    return lambda a : a * n
   

new1 = new(2)
new2 = new(3)
print(new1(3))
print(new2(4))

num = [1,2,3,4,5,6,7]
double = list(map(lambda x : x ** 2, num))
print(double)

num = [0,2,4,6,8]
double = list(map(lambda i : i*3-4/2*2, num))
print(double)

num = [0,1,2,3,4,5,6,7,8,9]
even = list(filter(lambda i : i % 2 == 0,num))
print(even)

odd = list(filter(lambda i: i %2 != 0,num))
print(odd)

o = num[0]
maxi = list(filter(lambda i : i > 2 and i < 6, num))
print(maxi)

stu = [(3, 25), (2, 22), (4, 28)]
s = sorted(stu, key =lambda x: x[1])
print(s)


#Descending
stu = [89,7,435,523,45432,5324,5,3245,43,256,56,4543,52,54634,245,2,4,52,3,4,532,6]
new = []

while stu:
    maxi = stu[0]

    for i in stu:
        if maxi < i:
            maxi = i

    new += [maxi]
    stu.remove(maxi)

print(new)

#Asceding
stu = [89,7,435,523,45432,5324,5,3245,43,256,56,4543,52,54634,245,2,4,52,3,4,532,6]
new = []

while stu:
    mini = stu[0]
    for i in stu:
        if mini > i:
            mini = i

    new += [mini]
    stu.remove(mini)
print(new)

l = [3,9,2,7,1,3,5,7,2,8,3,6]
new = []

while l:
    mini = l[0]
    for i in l:
        if mini > i:
            mini = i
    print(mini)
    new += [mini]
    l.remove(mini)

print(new)

s = "proFSGGASRONDAggaramming"
s = s.lower()
a = ""
for i in s:
    if i not in a:
        a += i
print(a)

st = "Banana"
s = ""

for i in st:
    if i not in s:
        count = 0

        for j in st:
            if j == i:
                count += 1
        print(f"{i} : {count}")
        s += i


s = "Banana"
st = ""
for i in s:
    if i not in st:
        count = 0

        for j in s:
            if i == j:
                count += 1
        print(f"{i} : {count}")
        st += i
