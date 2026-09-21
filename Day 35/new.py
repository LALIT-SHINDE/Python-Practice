# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     def get(self):
#         print(f"Name : {self.name}\nAge : {self.__age}")

#     def set(self, age):
#         if self.__age < 18:
#             self.__age = age


# p1 = Person("Lalit", 42)
# p1.get()
# p1.set(23)
# p1.get()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)

    def set(self, age):
        if age > 18:
            self.__age = age

        else:
            print(F"age should be greater than 18")

s1 = Student("Lalit", 12)
s1.set(43)
s1.show()

