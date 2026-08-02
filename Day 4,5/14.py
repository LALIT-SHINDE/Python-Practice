kg = float(input("Enter Your Weight(kg): "))
m = float(input("Enter your Hight(meters): "))

bmi = kg/(m*m)

if bmi < 18.5:
    print("Uderwight")
elif bmi < 24.9:
    print("Normal")
elif bmi < 29.9:
    print("Overwight")
else:
    print("Obese")