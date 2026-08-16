Number Analyzer 
def EvenOdd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def PosiNega(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return 0," : Neither Positive or Negative"

def NumberofDigits(n):
    count = 0
    while n != 0:
        last = n % 10
        count += 1

        n//=10
    return count


def SumofDigits(n):
    total = 0
    while n != 0:
        last_digit = n % 10
        total += last_digit

        n //= 10
    return total

def Reverse(n):
    reverse = 0
    while n != 0:
        last_digit = n % 10
        reverse = reverse * 10 + last_digit

        n //= 10
    return reverse

def palindrome(n):
    num = n
    reverse = 0

    while num != 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit

        num //= 10

    if n == reverse:
        return f"{n} is a Palindrome"
    else:
        return f"{n} is Not a Palindrome"

def Prime(n):
    if n <= 1:
        prime = False
    else:
        prime = True
        for i in range(2,n):
            if n % i == 0:
                prime = False
                break

    if prime:
        return f"{n} is a Prime Number"
    else:
        return f"{n} is not a Prime Number"
    
def Armstrong(n):
    num = n
    a = str(n)
    b = int(a)
    
    total = 0

    while num != 0:
        last_digit = num % 10
        l = last_digit ** len(a)

        total += l

        num //= 10
    if b == total:
        return f"{b} is an Armstrong Number"
    else:
        return f"{b} is not an Armstrong Number"
    
def Number_Analyzer(num):
    print(f"{num} is {EvenOdd(num)}")
    print(f"{num} is {PosiNega(num)}")
    print(f"{num}: Number of Digits is {NumberofDigits(num)}")
    print(f"{num}: Sum of Digits is {SumofDigits(num)}")
    print(f"{num}: Reverse : {Reverse(num)}")
    print(palindrome(num))
    print(Prime(num))
    print(Armstrong(num))

Number_Analyzer(15436)
