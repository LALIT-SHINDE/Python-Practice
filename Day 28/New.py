# 28. Function + *args
# Create:
# def calculate(*numbers):
# The function should return:
# Total
# Maximum
# Minimum
# Average

def calculate(*numbers):
    total = 0
    maxi = numbers[0]
    mini = numbers[0]
    
    for i in numbers:
        total += i

        if maxi < i:
            maxi = i

        if mini > i:
            mini = i
       

    average = total / len(numbers)

    return f"{numbers}\nTotal:{total}\nMaximum:{maxi}\nMinimum:{mini}\nAverage:{average}"

print(calculate(10,20,30,40,50))

# 29. Student Marks Analyzer
# Create a function-based program using a dictionary/list.
# Total marks
# Average
# Maximum
# Minimum
# Pass/Fail
# Grade

def Analysis(record):
    for name, marks in record.items():
        maxi = marks[0]
        mini = marks[0]

        total = 0

        for i in marks:
            total += i

            ave = total / len(marks)

            if maxi < i:
                maxi = i

            if mini > i:
                mini = i

            if ave <= 40:
                result = "Pass"
            else:
                result = "Fail"

            if ave <= 100 and ave >= 91:
                grade = "A+"

            elif ave <= 90 and ave >= 81:
                grade = "A"

            elif ave <= 80 and ave >= 71:
                grade = "B"

            elif ave <= 70 and ave >= 55:
                grade = "C"

            elif ave <= 54 and ave >= 40:
                grade = "D"

            else :
                grade = "F"

        print(f"Name : {name}\nMarks : {marks}\nTotal : {total}\nAverage : {ave}\nMaximum : {maxi}\nMinimum : {mini}\nResult : {result}\nGrade : {grade}\n")

students = {
    "Amit": [78, 85, 67, 90, 72],
    "Priya": [88, 92, 79, 85, 90]
}
Analysis(students)

# 30. Final Challenge — Combine Everything
# ===== STUDENT MANAGEMENT SYSTEM =====

# 1. Add Student
# 2. Display Students
# 3. Calculate Total
# 4. Calculate Average
# 5. Find Highest Marks
# 6. Find Lowest Marks
# 7. Check Pass/Fail
# 8. Display Grade
# 9. Exit

students = {
    "Amit": [78, 85, 67, 90, 72],
    "Priya": [88, 92, 79, 85, 90]
}

def add_student(dics, name, marks):
       
        if len(marks) == 5:
            dics[name] =  marks
            return f"Added."

        else:
            return f"Invaild Entry"

def total(stu):
    for name, marks in stu.items():
        total = 0

        for i in marks:
            total += i
        print(f"{name} : Total Marks :{total}")

def average(stu):
    for name, marks in stu.items():
        total = 0

        for i in marks:
            total += i

        average = total / len(marks)
        print(f"{name} : Average marks :{average}")

def highest_marks(stu):
    for name, marks in stu.items():
        maxi = marks[0]

        for i in marks:
            if maxi < i:
                maxi = i
        print(f"{name} : Highest Marks: {maxi}")

def lowest_marks(stu):
    for name, marks in stu.items():
        mini = marks[0]

        for i in marks:
            if mini > i:
                mini = i

        print(f"{name}: Lowest marks: {mini}")

def result(stu):
    for name, marks in stu.items():
        total = 0

        for i in marks:
            total += i

        average = total / len(marks)
        if average <= 40:
            print(f"{name} : Fail")
        else:
            print(f"{name} : pass")

def grade(stu):
    for name, marks in stu.items():
        total = 0

        for i in marks:
            total += i

        ave = total/len(marks)

        if ave <= 100 and ave >= 91:
            grade = "A+"

        elif ave <= 90 and ave >= 81:
            grade = "A"

        elif ave <= 80 and ave >= 71:
            grade = "B"

        elif ave <= 70 and ave >= 56:
            grade = "C"

        elif ave <= 55 and ave >= 40:
            grade = "D"

        else:
            grade = "F"

        print(grade)

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====\n1. Add Student\n2. Display Students\n3. Calculate Total")
    print("4. Calculate Average\n5. Find Highest Marks\n6. Find Lowest Marks\n7. Check Pass/Fail\n8. Display Grade\n9. Exit")

    choice = int(input("Enter the Choice: "))

    match choice:
        case 1:
            name = input("\nEnter the name: ")
            marks = list(map(int, input("Enter the 5 Marks: ").split()))

            print(add_student(students, name,marks))

        case 2:
            for name, marks in students.items():
                print(f"{name} = {marks}")

        case 3: 
            total(students)

        case 4:
            average(students)

        case 5:
            highest_marks(students)

        case 6:
            lowest_marks(students)

        case 7:
            result(students)

        case 8: 
            grade(students)

        case 9:
            print("Exit.....")
            break

        case _:
            print("Invalid choice, Try again....")

            
