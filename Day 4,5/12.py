a = float(input("Enter your Account Balance: "))
b = float(input("Enter Amount you want to Withdraw: "))

if b <= a:
    print(f"Withdrawal Amount: {b}\nTransaction Successful.....")
    print(f"Remaining Balance: {a-b:.2f}")
else:
    print(f"Insufficient Balance.")