# l = [10,20,30,40,50,60]

# it = iter(l)

# print(next(it))
# print(next(it))


# string = "Hello"
# i = iter(string)

# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# for i in string:
#     print(i)

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class num:
#     def __iter__(n):
#         n.a = 1
#         return n

#     def __next__(n):
#         x = n.a
#         n.a += 1
#         return x

# myclass = num()
# i = iter(myclass)

# for i in myclass:
#     if i < 100:
#         print(i)


class number:
   def __iter__(n):
      n.a = 1
      return n

   def __next__(n):
      if n.a <= 20:
        x = n.a
        n.a += 1
        return x
      
      else:
        raise StopIteration
        


i = iter(number())   

print(next(i))
print(next(i))

# for i in number():
#     print(i)

# l = [1,2,3]
# print(next(iter(l)))
