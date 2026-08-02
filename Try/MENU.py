choice = 0
while choice != 5 :
    print("\n--- Menu ---")
    print("1 Add.\n2 Sub.\n3 Multi.\n4 Div.\n5 Exit.")

    choice = int(input("Enter the coice: "))
    match choice:
        case 1:
            a = int(input("Enter the 1st number: "))
            b = int(input("Enter the 2nd number: "))
            print(f"{a} + {b} = {a+b}")
        
        case 2:
            a = int(input("Enter the 1st number: "))
            b = int(input("Enter the 2nd number: "))
            print(f"{a} - {b} = {a-b}")
         
        case 3:
            a = int(input("Enter the 1st number: "))
            b = int(input("Enter the 2nd number: "))
            print(f"{a} * {b} = {a*b}")
            
        case 4:            
            a = int(input("Enter the 1st number: "))
            b = int(input("Enter the 2nd number: "))

            if b == 0:
                print(f"{a} / {b} = Undifined")
            else:
                print(f"{a} / {b} = {a/b}")
        
        case 5:
            print("Exit......")

        case _:
            print("Invaild choice.....\nTry Again ")
            

