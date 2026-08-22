#1 Second Largest Number
def Second_Largest(num):
    n = list(num)
    maxi = n[0]

    for i in n:
        if maxi < i:
            maxi = i

    n.remove(maxi)

    maxi = n[0]
    for i in n:
        if maxi < i:
            maxi = i

    return maxi


r = 83,42,32,21,54,12
print(r)
print(f"The 2nd Larest No: {Second_Largest(r)}")

#or using sort
def sec_larg(num):
    a = sorted(num)
    print(a[-2])

r = [32,43,25,74,89,21]
sec_larg(r)

#String Analyzer
def analyze_string(a):

    #Length of string
    count = 0
    for _ in a:
        count += 1
    print(f"{a} : lenght is {count}")

    #num of vowels
    vowels = 0
    for i in a:
        if i in "aeiou":
            vowels += 1
    print(f"{vowels}: vowels in a {a}")

    # Number of consonants
    cons = 0
    for i in a:
        if i not in "aeiou" and not i.isdigit() and i.isalpha():
            cons += 1
    print(f"{cons}: consonants in a {a}")

    # Number of Digits
    digits = 0
    for i in a:
        if i.isdigit():
            digits += 1
    print(f"{digits}: Digits are in a {a}")

    #Number of spaces
    space = 0
    for i in a:
        if i == " ":
            space += 1
    print(F"{space}: spaces are in {a}")

    # Number of uppercase letters
    Upper = 0
    for i in a:
        if i.isupper():
            Upper += 1
    print(f"{Upper}: Uppercase latters in {a}")

    #Number of lowercase letters
    lower = 0
    for i in a:
        if i.islower():
            lower += 1
    print(f"{lower}: Lowercase latters in {a}")



name = "Lalit12@"
analyze_string(name)

# 3. Student Result Analyzer
def Result_Analyzer(stu):

    topper = ""
    high = 0 

    for name, marks in stu.items():

        total = 0

        mini = marks[0]
        maxi = marks[0]
        for i in marks:
            if maxi < i:
                maxi = i

            if mini > i:
                mini = i

            total += i
            average = total / len(marks)

            if average >= 40:
                result = "Pass"
            else:
                result = "Fail"

            if average >= 90:
                grade = "A+"
            elif average >= 80:
                grade = "A"
            elif average >= 65:
                grade = "B"
            elif average >= 50:
                grade = "C"
            elif average >= 40:
                grade = "D"
            else:
                grade = "F"
            
        if average > high:
            high = average
            topper = name
        
            # topper = marks.vaules(average)

        print(f"{name}: {marks} : \nTotal marks : {total}, Average : {average}, Highest marks: {maxi}, Lowest Marks: {mini}, Result: {result}, Grade: {grade}\n")

    print(f"The Class Topper: {topper} = {high}")
    


student = {
    "Amit": [92, 43, 52, 62, 82],
    "Priya": [32, 43, 92, 12, 72],
    "Deepak": [82, 73, 12, 92, 22],
    "Suman": [71, 17, 52, 62, 42]
}
Result_Analyzer(student)

#4 Remove Duplicates
def duplicates(num):
    new = []

    for i in num:
        if i not in new:
            new += [i]
    print(new)

a = [32,32,43,24,43,32,56]
duplicates(a)

#5 Password Checker
def Password_Checker(password):
    print(password)

    if len(password) >= 8:

        upper = False
        lower = False
        digit = False
        special = False

        for i in password:
            if i.isupper():
                upper = True

            if i.islower():
                lower = True

            if i.isdigit():
                digit = True

            if not i.isalnum():
                special = True

        return upper and lower and digit and special
  
    else:
        return False         
  
print(Password_Checker("La@it4tvb"))

#7. *args Challenge
def calculate(*num):
    total = 0
    maxi = num[0]
    mini = num[0]

    for i in num:
        total += i
        if maxi < i:
            maxi = i

        if mini > i:
            mini = i

    average = total/len(num)

    return num, total, average, maxi, mini


n,t, ave, maxx, minn = calculate(4,5,6,7,8)
print(f"{n}\nSum : {t}\nAverage : {ave}\nMaximum : {maxx}\nMinimum : {minn}")

#8. **kwargs Challenge
def student_info(**details):

    for name, info in details.items():
        print(f"{name} : {info}")
    
    if "Python" in details.values():
        print("Nice")    
    else:
        print("Sorry")
        
student_info(Name="Lalit", age = 21, Courese ="MCA",Language = "Python" )
