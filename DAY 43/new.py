s = input("Enter the string: ").lower()
s1 = input("Enter the string2: ").lower()

s = sort(s)
s1 = sort(s)

if s == s1:
  print(f"{s} is a anagram to {s1}")
else:
   print(f"{s} is not anagram to {s1}")
