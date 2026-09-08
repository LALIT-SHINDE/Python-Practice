class person:
    def __init__(self, name, age ,city,goal):
        self.name = name
        self.age = age
        self.city = city
        self.goal = goal

    def show(self):
        print(f"Name: {self.name}\nCity: {self.city}\nGoal: {self.goal}\nAge: {self.age}\n")

s = person("amit",23,"Nashik","gg")
s.show()

p = person("sumit",21,"Pune","ff")
p.show()
