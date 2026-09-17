#Getter Method
class Person:
    def __init__(self, name, id,age):
        self.name = name
        self.id = id
        self.__age = age

    def get(self):
        return self.__age
        

p1 = Person("Lalit", 60 ,22)
print("Name :",p1.name)
print("ID :",p1.id)

# print(p1.__age)
# This will cause error because __age is a private property and we can't
# Direclty accessed it
# TO Access private property we have to use Getter method (get())

print("Age :",p1.get())



#Setter Method
class Stu:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get(self):
        return self.__age

    def set(self):
        if self.__age > 18:
            return self.__age
        else:
            return f"Not Eligible"

s1 = Stu("Lalit", 12)
print(s1.name)
print(s1.get())
print(s1.set()) 
# To modify a private property, you can create a setter method.
# The setter method can also validate the value before setting it:
    
