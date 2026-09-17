class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get(self):
        return self.__age

p1 = Person("lalit", 22)
print(p1.name)
print(p1.get())

class Student:
    def __init__(self,  name, id):
        self.name = name
        self.__id = id

    def get(self):
        return self.__id

s1 = Student("Lalit", 22)
print(s1.name)
print(s1.get())



    
