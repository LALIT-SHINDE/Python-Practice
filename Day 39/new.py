s = input("Enter the String: ")
li = list(s)

l = 0
r = len(li) - 1

palindrome = True

while l < r:
  if li[l] != li[r]:
    palindrome = False
    break
  l += 1
  r -= 1

if palindrome:
  print(f"{s} is a Palindrome")
  
else:
  print(f"{s} is not a Palindrome")
  

# Sample Output 1:
# Enter the String: lalit
# lalit is not a Palindrome

# Sample Output 2:
# Enter the String: lalilal
# lalilal is a Palindrome
    
  
