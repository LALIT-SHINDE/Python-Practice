a = int(input("Enter your age: "))

if a <= 0:
    print("Invalid Age....")
elif a < 5 :
    print(f"Movie ticket is free for age:{a} ")
elif a <= 17:
    print(f"Movie ticket is 100rs for age:{a}")
elif a <= 59:
    print(f"Movie ticket is 200rs for age:{a}")
else:
    print(f"Movie ticket is 120rs for age:{a}")
