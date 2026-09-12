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

class Num(Add):
    def __init__(self, j, k):
        self.j = j
        self.k = k

        super().__init__(j, k)

N1 = Num(54,46)
print(N1)




class Multiplication:
    def __init__(self, a):
        self.a = a

    def table(self):
        for i in range(1,11):
            print(f"{self.a} * {i} = {self.a * i} ")

class Number(Multiplication):
    def __init__(self,j):
        self.j = j

        super().__init__(j)

n1 = Number(12)
n1.table()

