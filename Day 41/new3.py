num = int(input("Enter the Numbe"))

if num < 1:
  prime = False

else:
  prime = True
  for i in range(2,num):
    if num % i == 0:
      prime = False
      break

if prime:
  print(num,"is a Prime Number")
else:
  print(num,"is not a Prime Number")
