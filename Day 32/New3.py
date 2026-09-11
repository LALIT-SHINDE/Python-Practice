
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(f"{self.name} ({self.age})")

class Student(person):
    def __init__(self, course):
        self.course = course

    def ko(self):
        print(f"{self.name} ({self.age}) {self.course}")
    
    
