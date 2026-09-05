
# 21. break Practice
for i in range(1, 101):
    print(i)
    if i != 37:
        break

# 22. continue Practice
for i in range(1,31):
    if i % 3 != 0:
        print(i)
        continue

# 23. Guessing Game
import random

num = random.randint(1, 100)

while True:
    guess = int(input("Enter the Interger: "))

    if guess > num:
        print("To High")

    elif guess < num:
        print("To Low")

    else:
        print(f"Secret Number: {num}\nMatch... You Won!")
        break
        


