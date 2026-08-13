# Base Case      :  A condition that stops the recursion
# Recursive Case :  The function calling itself with a modified argument
def count_down(n):
    if n <= 0:         # Base Case: This is the condition that stops the Recursion 
        print("Done!")     
    else:
        print(n)
        count_down(n-1)  # Recursive Case: Funtion calls itself and modified itself
count_down(5)   



def factorial(n):
    #Base case
    if n == 0 or n == 1:
        return 1
    
    #Recursive case
    else:
        return n * factorial(n-1)
a = 5
print(f"{a}! = {factorial(a)}")



def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
print(f"{7}! = {fact(7)}")


n = 0
m = 1
for _ in range(10):
    print(n)
    suum = n + m
    n, m = m, suum

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n - 2)
print(fibo(7))

num = 5
fa = 1
for _ in range(num):
    fa *= num
    num -= 1
print(fa)

def sum_list(num):
    if len(num) == 0:
        return 0
    else:
        return num[0] + sum_list(num[1:])

n = [1,2,3,4,5]
print(sum_list(n))

# remove duplicates 
s = "Prorogramminpg"
a = list(s.lower())

for i in a:
    new = []
    if i not in new:
        new += [i]

print(new)

