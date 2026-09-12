
class Table:
    def __init__(self, a):
        self.a = a

    def mul(self):
        for i in range(1,11):
            print(f"{self.a} * {i} = {self.a * i}")

class New(Table):
    def __init__(self, j):
        self.j = j

        super().__init__(j)
        

N1 = New(4)
N1.mul()


class Animal:
    def __init__(self, name):
       self.name = name

    def speak(self):
        print(self.name)


class Dog(Animal):
    def __init__(self,name):
        self.name = name

        super().__init__(name)

d1 = Dog("Rex")
d1.speak()



class Teacher:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def show(self):
        print(self.name, self.age)

class Student(Teacher):
    def _init__(self, stu, roll):
        self.stu = stu
        self.roll = roll

        super().__init__(stu, roll)

s1 = Student("Sid", 32)
s1.show()


class table:
    def __init__(self, num):
        self.num = num

    def show(self):
        for i in range(1,11):
            print(f"{self.num} * {i} = {self.num*i}")

class Num(table):
    def __init__(self, n):
        self.n = n

        table.__init__(self, n)
        super().__init__(n)

N1 = Num(5)
N1.show()
