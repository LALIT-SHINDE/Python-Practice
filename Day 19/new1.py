
def calculate_result(marks):
    print(marks)

    total = 0
    for i in marks:
        total += i
    print(f"Total marks : {total}")

    average = total / len(marks)
    print(f"Average : {average}")

    for i in marks:
        if i >= 40:
            re = True
        else:
            re = False
    if re:
        print("Result : Pass")
    else:
        print("Result : Fail")


    if average > 90:
        print("Grade A+")
    elif average > 80:
        print("Grade A")
    elif average > 60:
        print("Grade B")
    elif average > 50:
        print("Grade C")  
    elif average >= 40:
        print("Grade D")
    else:
        print("Fail")


m = [42,52,75,89,92]  
calculate_result(m)

Find Second Largest
def Secound_largest(m):
    maxi = m[0]
   

    for i in m:
        if maxi < i:
            maxi = i
    m.remove(maxi)
    

    maxi_2nd = m[0]
    
    for i in m:
        if maxi_2nd < i:
            maxi_2nd = i

    return maxi_2nd

marks = [10,50,40,30,80]
print(f"{marks} : 2nd largest is {Secound_largest(marks)}")

#Count Vowels
def vowels(text):
    text = text.lower()
    count = 0
    for i in text:
        if i in "aeiou":
            count += 1
        
    return count

name = "Lalit"
print(f"{vowels(name)} vowles are in {name}")

#Remove Duplicates
def remove_duplicates(numbers):
    new = []
    for i in numbers:
        if i not in new:
            new += [i]
    return new

num = [10,50,30,50,20,10,40,50,60,70]
print(remove_duplicates(num))


#Find Common Elements
def comman(list1, list2):
    new = []
    for i in list1:
        for j in list2:
            if i == j:
                new += [i]
    return new

l = [10,20,30,40,50,60]
ll = [20,40,60]
print(comman(l,ll))

#Word Counter
def word_count(sen):
    count = 1
    for i in sen:
        if i == " ":
            count+=1
    return count
py = "My name is lalit shinde"
print(word_count(py))

#7. Palindrome Function
def palindrome(obj):
    if type(obj) == int:
        reverse = 0
        o = obj

        while obj != 0:
            current = obj % 10
            reverse = reverse * 10 + current
            obj //= 10
        if reverse == o:
            return True
        else:
            return False
        
    else:
        o = obj.lower()
        reverse = o[::-1]
        if o == reverse:
            return True
        else:
            return False
k = 32423
j = "LalitLasi"

print(palindrome(k))
print(palindrome(j))

#Prime number
def is_prime(num):
    if num <= 1:
        prime = False
    else:
        prime = True
        for i in range(2,num):
            if num % i == 0:
                prime = False
    if prime:
        return "Yes"
    else:
        return "No"
n = 3
print(is_prime(n))
nu = 7
print(is_prime(nu))
nk = 8
print(is_prime(nk))

#output
# [42, 52, 75, 89, 92]
# Total marks : 350
# Average : 70.0
# Result : Pass
# Grade B
# [10, 50, 40, 30, 80] : 2nd largest is 50
# 2 vowles are in Lalit
# [10, 50, 30, 20, 40, 60, 70]
# [20, 40, 60]
# 5
# True
# False
# Yes
# Yes
# No
