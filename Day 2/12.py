citizenship = input("Enter Your Citizenship: ").lower()
age = int(input("Enter your age:"))

if citizenship == "indian" and age >= 18:
    print("Eligible for voting")
else:
    print("Not Eligible")

# Output

# Case 1
# Enter Your Citizenship: Indian
# Enter your age: 32
# Eligible for voting

# Case 2
# Enter Your Citizenship: Indian
# Enter your age: 12
# Not Eligible

# Case 3
# Enter Your Citizenship: USA
# Enter your age: 32
# Not Eligible
