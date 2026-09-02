#1  Take two numbers from the user and print:

# Sum
# Difference
# Product
# Division
# Floor division
# Remainder

while True:
    a = int(input("\nEnter the 1st Value: "))
    b = int(input("Enter the 2nd value: "))
    c = input("Enter the Operation +, -, *, /, // or % :")
    print()

    match c:
        case "+":
            print(f" Sum: \n {a} + {b} = {a+b}")

        case "-":
            print(f"Difference: \n {a} - {b} = {a-b}")
    
        case "*":
            print(f"Product: \n {a} * {b} = {a*b}")
      
        case "/":
            if b == 0:
                print(f"Division:\n {a} / {b} = Undifined")
            else:
                print(f"Division:\n {a} / {b} = {a/b}")

        case "//":
            if b == 0:
                print(f"Floor Division: \n {a} / {b} = Undifined")
            else:
                print(f"Floor Division: \n {a} / {b} = {a/b}")

        case "%" :
            if b == 0:
                print(f"Division:\n {a} % {b} = Undifined")
            else:
                print(f"Division:\n {a} % {b} = {a%b}")
        
        case _ :
            print(f"Invalid Indut")
            break

# 2. Type Conversion
# Take a number as a string:

# num = "25"

# Convert it into an integer and float and print their types.

num = input("Enter Any Number: ")
print(num, type(num))

num_int = int(num)
print(num_int, type(num_int))

num_float = float(num)
print(num_float, type(num_float))

# 3. Even or Odd
# Take a number and check whether it is even or odd.

num = int(input("Enter the Number: "))
if num % 2 == 0:
    print(num,"is an Even Number")
else:
    print(num,"is an Odd Numbber")

# 4. Largest of Three
# Take three numbers and find the largest using if-elif-else.

a = int(input("Enter the 1st Number: "))
b = int(input("Enter the 2nd Number: "))
c = int(input("Enter the 3rd Number: "))

if b < a > c:
    print(f"{a} is Largest")

elif a < b > c:
    print(f"{b} is Largest")

elif a < c > b:
    print(f"{c} is Largest")

elif a == b and a > c:
    print(f"{a} and {b} are same and Largest")

elif a == c and a > b:
    print(f"{a} and {c} are same and Largest")

elif b == c and b > a:
    print(f"{b} and {c} are same and Largest")

else:
    print(f"{a}, {b} and {c} are Equle.")
    

# 5. Simple Calculator
# Create a calculator using:

# +  -  *  /  %

# Use if-elif-else.

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = input("Enter the opration +, -, *, or , / : ")

if c == '+':
    print(f"{a} + {b} = {a+b}")

elif c == '-':
    print(f"{a} - {b} = {a-b}")

elif c == '*':
    print(f"{a} * {b} = {a*b}")

elif c == '/':
    if b == 0:
        print(f"{a} / {b} = Undinfed")
    else:
        print(f"{a} / {b} = {a%b}")
elif c == '%':
    if b == 0:
        print(f"{a} % {b} = Undinfed")
    else:
        print(f"{a} % {b} = {a%b}")
