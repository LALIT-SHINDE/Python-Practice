# Function to check palindrome.
def pali(n):
    # if isinstance(n, int):
    if type(n) == int:
        n1 = n
        reverse = 0
        while n != 0:
            current = n % 10
            reverse = reverse * 10 + current

            n = n // 10
        if n1 == reverse:
            print(f"{reverse} is Palindrome")
        else:
            print(f"{n1} and {reverse} is not a Palindrome")
    else:
        a = n.lower()
        reverse = a[::-1]
        if a == reverse:
            print(f"{reverse} is Palindrome")
        else:
            print(f"{a} and {reverse} is not a Palindrome")

pali(3467643)
pali("LAiTiAl")
pali("$ksdLdsk$")

#Function to check Armstrong number.
def my1(num):
    n = num
    a = str(n)
    summ = 0

    while n != 0:
        last_digit = n % 10
        total = last_digit ** len(a)
        summ += total

        n //= 10
    if num == summ:
        print(f"{num} is An Armstrong Number")
    else:
        print(f"{num} is not An Armstrong Number")
my1(143)
my1(153)

# Function to remove duplicates from a string.
def my2(s):
    print(s)
    new = ""
    for i in s:
        if i in new:
            continue
        new = new + i
    print(new)
my2("HHeellow")

# Function to count character frequency.
def my3(s):
    new = ""
    for i in s:
        if i in new:
           continue
        
        count = 0
        for j in s:
            if i == j:
                count += 1

        new += i
        print(i," : ", count)

my3("Programming")


def my4(s):
    new = "" 

    for i in s:
        if i in new:
            continue

        count = 0
        for j in s:
            if i == j:
                count += 1
        new += i

        print(f"{i} : {count}")
my4("Banana")

