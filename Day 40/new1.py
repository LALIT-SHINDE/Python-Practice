num = int(input("Enter the number:")) 
n = num
a = list(num)

total = 0

while n != 0:
  current = n % 10
  total += current ** len(a)

  n //= 10

if total == num:
  print(f"{num} Strong Number")

else:
  print(f"{num} not a Strong Number")
