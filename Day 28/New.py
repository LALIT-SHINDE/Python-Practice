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
