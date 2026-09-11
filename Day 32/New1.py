class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(f"{self.name} ({self.age})")

class Student(person):
    # def __init__(self, course):
    #     self.course = course

    # def ko(self):
    #     print(f"{self.name} ({self.age}) {self.course}")
    pass
    
# p1 = person("Lalit", 21)
# p1.printname()

s1 = Student("Lalit", 21)
s1.printname()


class person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(f"{self.name}, {self.age} ")

class student(person1):
    def __init__(self, name, age):
        self.course = name
        self. name = age

        person1.__init__(self, name, age )

s = student("Mike", 43)
s.printname()
