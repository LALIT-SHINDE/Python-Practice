class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(self):
    print(self.name, self.age)

class student(Person):
  def __init__(self, name, age):
    self.name = name
    self.age = age 

    super().__init__(name, age)

s1 = student("Sumit", 23)
s1.show()
