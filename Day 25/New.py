# # 1. Count vowels and consonants
# text = "Hello World"
# vowles = 0
# consonants = 0


# for i in text:
#     if i in "aeiouAEIOU":
#         vowles += 1

#     elif i == " ":
#         pass

#     else:
#         consonants += 1
# print(f"{text}: vowles:{vowles} Consonants:{consonants}")

# # 2. Reverse a string using a loop
# s = "python"

# for i in range(len(s)-1,-1,-1):
#     print(s[i],end="")
# print()

# #or
# s = "python"
# s = list(s)
# l = 0
# r = len(s) - 1

# while l < r:
#     s[l], s[r] = s[r],s[l]

#     l += 1
#     r -= 1
# s = "".join(s)
# print(s)

# # 3. Check whether a string is a palindrome
# #Method 1
# s = "madam"
# new = ""
# for i in range(len(s)-1,-1,-1):
#     new += s[i]

# if new == s:
#     print(f"{s} is a palindrome")
# else:
#     print(f"{s} is not a palindrome")

# #Method 2
# st = "madam"
# s = list(st)
# l = 0
# r = len(s) - 1
# palindrome = True

# while l < r:
#     if s[l] != s[r]:
#         palindrome = False
#         break

#     l += 1
#     r -= 1

# if palindrome:
#     print(f"{st} is Palindrome")
# else:
#     print(f"{st} is not a Palindrome")


# # 4. Count the frequency of each character
# text = "banana"
# new = ""

# for i in text:
#     if i not in new:
#         count = 0

#         for j in text:
#             if i == j:
#                 count += 1

#         print(f"{i}: {count}")
#         new += i

# # 5. Find the first repeating character

# text = "programming"
# new = ""

# for i in text:
#     if i in new:
#         print(i)
#         break

#     new += i
# print(new)

# # 6. Remove duplicate characters
# txt = "Programming"
# new = ""

# for i in txt:
#     if i not in new:
#         new += i

# print(new)

# # 7. Count words without using split()
# text = "I love learning Python"
# space = " "
# count = 1

# for i in text:
#     if space == i:
#         count += 1
# print(f"Total words is '{text}' are {count}")


# text = "Python is an amazing language".split()
# t = list(text)
# maxi = t[0]

# for i in text:
#     if len(maxi) < len(i):
#         maxi = i

# print(f"{maxi}: {len(maxi)}")

# # 9. Check if two strings are anagrams

# def anagram(a,b):
#     def sort(txt):
#         txt = txt.lower()
#         t = list(txt)
#         new = []

#         while len(t) != 0:
#             mini = t[0]

#             for i in t:
#                 if mini > i:
#                     mini = i

#             new += [mini]
#             t.remove(mini)

#         txt = "".join(new)
#         return txt

#     m = sort(a)
#     n = sort(b)

#     if m==n:
#         return f"{a} and {b} are Anagrams"
#     else:
#         return f"{a} and {b} are not Anagrams"

# i = "lalIt"
# j = "Allti"
# print(anagram(i,j))

# # 10. String compression

# string = "aaabbcccc"
# new = ""

# for i in string:
#     if i not in new:
#         count = 0

#         for j in string:
#             if i == j:
#                 count += 1

#         print(f"{i}{count}",end="")
#         new += i

# string = input("Enter a String: ")
# s = list(string)

# l = 0
# r = len(s) - 1

# while l < r:
#     temp = s[l]
#     s[l] = s[r]
#     s[r] = temp

#     l += 1
#     r -= 1

# rev_string = "".join(s)

# print(string)
# print(rev_string)

# string = input("Enter the string: ")
# s = list(string)
# rev_string = ""

# for i in range(len(s)-1,-1,-1):
#     rev_string += s[i]

# print(string)
# print(rev_string)

# string = input("Enter the String: ")
# s = string[::-1]
# print(string)
# print(s)
# new = ""

# for i in string[::-1]:
#     new += i

# print("Hi", new)


# num = int(input("Enter the Number: "))
# if num % 2 == 0:
#     print(f"{num} is Even.")
# else:
#     print(f"{num} is Odd.")


# import math
# num = int(input("Enter the number: "))
# if num <= 1:
#     prime = False

# else:
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break

# if prime:
#     print(f"{num} is a Prime Number.")
# else:
#     print(f"{num} is not a Prime Number.")



# num = int(input("Enter the number: "))
# fact = 1

# for i in range(2, num + 1):
#     fact *= i
# print(f"{num}! : {fact}")

n = int(input("Enter the Number: "))
a = 0 
b = 1
print(f"{a}\n{b}\n")

for i in range(n+1):
    print(a)
    c = a + b

    b = a
    a = c
    if a >= n:
        break

