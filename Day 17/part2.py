#27
x = 100
def my():
    return x
print(my())

#28
def my1():
    a = 43
    return a
print(my1())
# print(a)

a = 53
def my2():
    a = 89
    return a
print("Function's Inside: ",my2())
print("Function's Outside: ",a)

#30
count = 0
print(count)
def my3():
 
    global count
    count += 1
    return count

print(my3())
print(my3())
print(my3())
print(count)
