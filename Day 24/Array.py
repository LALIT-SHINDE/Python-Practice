#1
a = [10,20,30,40,50]
print(a[3]) # Time complexity: O(1) constant time

#2
a = [10,20,30,40,50]
for i in a:
    print(i) # Time complexity: O(n) linear time

#3
a = [10,20,30,40,50]
for i in a:
    for j in a:
        print(i) # Time complexity: O(n**2) Quadratic Time

#4
a = [10,20,30,40,50] # here we have to check time complexity for entrie code 
for i in a:
    print(i) # O(n)



for j in a:
    print(j) # O(n)

# O(n) + O(n) = O(2n)


