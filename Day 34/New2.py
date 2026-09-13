class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} : {self.y}"


class Stu(Person):
    def __init__(self, name, age , year):
        self.name = name
        self.age = age

        super().__init__(name, age)
        self.graduation = year

    def welcome(self):
        print(f"Welcome {self.name}({self.age} : {self.graduation})")
        


s1 = Stu("Lalit", 22, 2025 )
print(s1)

s1.welcome()
print(str(s1))

class Kuja:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + {self.b} = {self.a + self.b}"

class name(Kuja):
    def __init__(self, j, k):
        self.j = j
        self.k = k

        super().__init__(j,k)
n = name(18 , 39)
print(n)




class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f"{self.a} + {self.b} = ",end =" ")

    def __str__(self):
        return f"{self.a + self.b}"


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
