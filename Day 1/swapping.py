#There are three ways to swap numbers to one variable to another

# Method 1:
print("Method 1")

a = 3
b = 4
print("Vari : A B")
print("OG   :",a,b)

a, b = b, a
print("Swap :",a,b,"\n")

#Method 2
print("Method 2")

a, b = 3, 4
print("Vari : A B")
print("OG   :",a,b)

c = a
a = b
b = c
 
print("Swap :",a,b,"\n")

#Method 3
print("Method 3")

a = 3
b = 4
print("Vari : A B")
print("OG   :",a,b)

a = a + b
b = a - b
a = a - b

print("Swap :", a,b)

