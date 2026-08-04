n = int(input("Enter any number"))
fact = 1
total = 0
for i in range(2, n+1):
    fact *= i
    total += fact

print(f"{n}! = {fact}")
print(total)
    
