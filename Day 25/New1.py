num = int(input("Enter the number: "))
a = 0
b = 1

for _ in range(num + 1):
  print(a)
  
  c = a + b
  b = a
  a = c
  if a > num:
    break
