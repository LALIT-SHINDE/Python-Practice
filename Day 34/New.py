n = int(input("Enter the number: "))
if n <= 1:
  prime = False

else:
  prime = True
  for i in range(2, n):
    if n % i == 0:
      prime = False
      break
if prime:
  print(f"{n} is a Prime Number.")
else:
  print(f"{n} is not a Prime Number.")
