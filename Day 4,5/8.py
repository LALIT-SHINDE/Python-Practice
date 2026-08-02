m = int(input("Enter Your Marks: "))


if (m >= 90) and (m <= 100):
    print(f"Your marks: {m} and Gread: A")

elif (m >= 75) and (m <= 89):
    print(f"Your marks: {m} and Gread: B")

elif (m >= 60) and (m <= 74):
    print(f"Your marks: {m} and Gread: C")

elif (m >= 40) and (m <= 59):
    print(f"Your marks: {m} and Gread: D")

else:
    print(f"Your Marks: {m} and Gread: Fail")