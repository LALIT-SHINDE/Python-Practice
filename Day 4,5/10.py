a = input("Enter a one Charater: ").lower()

if a in "abcdefghijklmnopqrstuvwxyz":
    print(f"{a} is AN Alphabets")
elif a in "1234567890":
    print(f"{a} is A Digit")
else:
    print(f"{a} is Special Charater")

if a.isalpha():
    print(f"{a} is AN Alphabets")
elif a.isdigit():
    print(f"{a} is A Digit")
else:
    print(f"{a} is Special Charater")
