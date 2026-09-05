n = 'Banana'
new = ""

for i in n:
    if i not in new:
        count = 0
        for j in n:
            if i == j:
                count += 1

        new += i
        print(i, count)

n = 12343567
count = 0
print(n)

num = int(input("Enter the number: "))
while n != 0:
    current = n % 10
    if num == current:
        count += 1

    n //= 10
print(f"{num}:{count} times")




num = 2238921313289
n = num

seen = [False] * 10

while n != 0:
    i = n % 10
    a = num
    count = 0

    if not seen[i]:

        while a != 0:
            current = a % 10

            if i == current:
                count += 1

            a //= 10

        seen[i] = True
        print(i,count)

    n //= 10

num = 982312342658987654321
n = num
print(num)
seen = [False] * 10 

while n != 0:
    i = n % 10
    b = num

    count = 0

    if not seen[i]:
        while b != 0:
            current = b % 10

            if i == current:
                count += 1

            b //= 10

        print(f"{i} : {count}")
        seen[i] = True

    n//=10
print()

string = "Banana"
new = ""

print(string)

for i in string:

    if i not in new:
        count = 0

        for j in string:
            if i == j:
                count += 1

        print(f"{i} : {count}")
        new += i


string = "BananaBJKLLJHK"
new = ""

print(string)
for i in string:
    if i not in new:
        new += i

string = new
print(string)






