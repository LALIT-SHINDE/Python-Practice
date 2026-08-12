student = {"Amit":{ 
                "Math" : 92,
                "Science" : 43,
                "Python" : 52,
                "English" : 62,
                "History" : 82 },

            "Priya":{
                "Math" : 32,
                "Science" : 43,
                "Python" : 92,
                "English" : 12,
                "History" : 72
            },

            "Deepak":{
                "Math" : 82,
                "Science" : 73,
                "Python" : 12,
                "English" : 92,
                "History" : 22
            },

            "Suman":{
                "Math" : 71,
                "Science" : 17,
                "Python" : 52,
                "English" : 62,
                "History" : 42
            }
        }



def travers(m):
    print("\n----- Subjects Marks -----")
    n = ["Math: ", "Science: ","Python: ","English: ", "Histroy: "]
    for i in range(len(n)):
        print(f"{n[i]} : {m[i]}")
    print()
    print("----- Progress -----")


def total_marks(m):
    total = 0
    for i in m:
        total += i
    return total

def average(m):
    count = 0
    for i in m:
        count += i
    average = count / len(m)
    return average

def max_marks(m):
    maxi = m[0]
    for i in m:
        if maxi < i:
            maxi = i

    return maxi

def min_marks(m):
    mini = m[0]
    for i in m:
        if mini > i:
            mini = i

    return mini

def result1(m):
    for i in m:
        if i < 40:
            return "Fail"
    return "Pass"

def grade(ave):
    if ave >= 90 :
        return "A+"
    elif ave >= 80:
        return "A"
    elif ave >= 70:
        return "B"
    elif ave >= 60:
        return "C"
    elif ave >= 50:
        return "D"
    elif ave >= 40:
        return "E"
    else:
        return "F"

print("\n=========== Student Marks Analyzer ===========")

for i,j in student.items():
    print(f"\n**** Student Name: {i} ****\n")

    print("----- Student = subjects : Marks -----\n")

    for k, l in j.items():
        print(f"{k} : {l}")

    print("\n----- Student Record -----\n")
    marks = list(j.values())

    a = average(marks)

    print(f"Total marks: {total_marks(marks)}")
    print(f"Average marks: {average(marks)}")
    print(f"Maximum marks: {max_marks(marks)}")
    print(f"Minimum marks: {min_marks(marks)}")
    print(f"Result: {result1(marks)}")
    print(f"Gard: {grade(a)}")
