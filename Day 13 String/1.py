n = 17
j = 4
for i in range(1, n):
    if i == 11:
        break
     
    print(f"{j} * {i} = {i*n}")

print("End.....")


for i in range(0, 12):
    if i == 0 or i == 11 :
        continue

    print(i)

for i in range(1, 6):
    if i == 3:
        continue

    print(i)


for i in range(1,11):
    if i == 7:
        break
    print(i)

for i in range(1,21):
    if i == 3:
        continue
    print(f"{n} * {i} = {n*i}")


# while True:
#     num = input("Enter the Name: ")

#     print(f"Your Name: {num}")

#     if num == "Skip":
#         print(f"Quit: {num}")
#         break

c =0
while c != 3:
    print("--- Menu ---")
    print("1. say Hello.")
    print("2. Show Time ")
    print("3. Exit")

    c = int(input("Enter choice: "))
    match c:
        case 1:
            print("Hello, Jarvis")

        case 2:
            print("Feature coming soon... ")
            pass

        case 3: 
            print("Byy....")
            break

        case _ :
            print("Invaild Choice")
            pass
      



    
