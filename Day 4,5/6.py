year = int(input("Enter any Year: "))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(f"{year} It's a Leap Year")
else:
    print(f"{year} It's not a Leap Year")