citizenship = input("Enter Your Citizenship: ").lower()
age = int(input("Enter your age:"))

if citizenship == "indian" and age >= 18:
    print("Eligible for voting")
else:
    print("Not Eligible")