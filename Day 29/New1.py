class Myclass:
    x = 10

class new:
    pass
    
a = Myclass()
b = Myclass 
c = Myclass

print(a.x)
print(b.x)
print(c.x)
print(a)

del a 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

obj = Person("Jhon",32)
print(obj.name, obj.age)
