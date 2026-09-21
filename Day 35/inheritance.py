class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"{self.name} {self.age}")

class Student(Person):
    def __init__(self, name, age, course):
        self.name = name
        self.age = age 
        self.course = course

        print(self.course)

s1 = Student("lalit", 22, "Mca")
s1.show()
