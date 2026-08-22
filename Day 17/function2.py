#1
def higest_sales(sales):
    maxi = sales[0]
    for i in sales:
        if maxi < i:
            maxi = i
    return maxi
sales = [1200, 800, 1500, 500, 2000, 750, 900]
print(higest_sales(sales))

#2
correct_username = "admin"
correct_password = "1234"
username = input("Enter your username: ")
if correct_username == username:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Login Successful.")
    else:
        print("Invalid username or password..")
else:
    print("Invalid username or password.")

#3
ages = [22, 17, 31, 15, 28, 19, 16, 40]
count = 0
for i in ages:
    if i > 18:
        count += 1
print(count)

#4
transactions = [500, -200, 1000, -150, 300, -50]
deposit = 0
total_Balance = 0
for i in transactions:
    total_Balance += i

print(total_Balance)


def size(n):
    count = 0
    for i in n:
        count += 1
    print(count)

size("Lalit")

#6
def pali(name):
    n = name.lower()
    a = list(n)

    l = 0
    r = len(a) - 1

    while l < r:
        temp = a[l]
        a[l] = a[r]
        a[r] = temp

        l += 1
        r -= 1

    reverse = "".join(a)

    if n == reverse:
        return "Palindrome"
    else:
        return "No Palindrome"

print(pali("Lalit"))
print(pali("Madam"))

#7 Duplicate Usernames
usernames = ["Lalit", "Rahul", "Amit", "Lalit", "Priya", "Amit"]
new = []
for i in usernames:
    if i not in new:
        new += [i]

print(new)

#8 Payment System
def payment(tra):
    deposite = 0
    withdrawals = 0
    final_Balance = 0

    for i in tra:
        if i >= 0:
            deposite += i
        else:
            withdrawals += -i

        final_Balance += i

    print( deposite)
    print(withdrawals )
    print(final_Balance)

    

transactions = [500, 200, -100, 1000, -50, 300]
payment(transactions)

#9 Employee Salary System
def bonus(n):
    new = []
    for i in n:
        if i >= 40000:
            i += 5000
        new += [i]
    return new
salaries = [25000, 42000, 18000, 55000, 32000, 47000] 
print(bonus(salaries))

#10 Customer Data
def find_a_names(name):
    new = []

    for i in name:
        if i[0] == "A" or i[0] == "a":
            new += [i]

    return new

customers = ["LaliAt", "Amit", "Rahul", "Ankit", "Priya", "Ajay"]
print(find_a_names(customers))

#11
def evaluate_scores(scores):
    new = []
    for i in scores:
        if i >= 90:
            i = "Excellent"
        elif 60 <= i:
            i = "Good"
        else:
            i = "Needs Improvement"
        new += [i]

    return new

# scores = [85, 42, 76, 91, 55, 38, 67, 95]
# print(evaluate_scores(scores))

#12
def calculate_prices(orders):
    dicount = 0
    new = []
    for i in orders:
        if i >= 1500:
            discount = (20*i)/100
            i -= discount
            i = int(i)
    
        elif i >= 1000:
            discount = (10*i)/100
            i -= discount
            i = int(i)

        new += [i]
    return new

orders = [500, 1200, 750, 2000, 300, 1500]
print(calculate_prices(orders))
    
#13
def tra(balance,withdrawal_amount):
    
    if withdrawal_amount <= 0:
        print("Invalid amount")
    elif withdrawal_amount > balance:
        print("Insufficient amount")
    else:
        balance -= withdrawal_amount 
        print(f"Remaining Balance: ",balance)

    
b = 10000
w = int(input("Enter withdrawal: "))
tra(b,w)

#14
def register(username, password):
    if len(username) >= 5 and len(password) >= 8:
        return "Registraction successful."
    else:
        return "Error"

a = input("Enter the username: ")
b = input("Enter the password: ")
print(register(a,b)) 

def search_employee(em, name):

    for i in em:
        if i == name:
            return "Employee Found"
    return "Employee Not Found"
        
employees = ["Lalit", "Rahul", "Amit", "Priya", "Ankit"]
print(search_employee(employees, "Amit"))

#15
def count_transaction(tr, amount):
    count = 0
    for i in tr:
        if i == amount:
            count += 1
    return count

transactions = [100, 200, 100, 500, 100, 300, 200]
print(count_transaction(transactions, 100))

#16
def max_2nd(sa):
    maxi = sa[0]
    
    for i in sa:
        if maxi < i:
            maxi = i

    sa.remove(maxi)

    maxi_2nd = sa[0]

    for j in sa:
        if maxi_2nd < j:
            maxi_2nd = j
    return maxi_2nd

salaries = [25000, 45000, 30000, 55000, 40000, 50000]
print(max_2nd(salaries))

#17
def calculate_result(m):
    pass_ = 0
    total = 0
    fail = 0
    for i in m:
        total += i
        if i >= 40:
            pass_ += 1
        else:
            fail += 1

    print(f"Total Marks: {total}")
    print(f"Passed: {pass_}")
    print(f"Failed: {fail}")
    
marks = [85, 42, 76, 91, 55, 38, 67, 95]
calculate_result(marks)
