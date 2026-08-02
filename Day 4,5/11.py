a = float(input("Enter the 1st value: "))
b = float(input("Enter the 2nd value: "))

c = input("Enter one operator(+, -, *, /): ")

if c == '+':
    print(f"{a} + {b} = {a+b}")
elif c == '-':
    print(f"{a} - {b} = {a-b}")
elif c == '*':
    print(f"{a} * {b} = {a*b}")
elif c == '/':
    if b == 0:
        print(f"{a} / {b} = Undefined")
    else:
        print(f"{a} / {b} = {a/b}")
else:
    print("Invalid Operator")