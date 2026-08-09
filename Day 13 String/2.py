#26
name = input("Enter your name: ")
print(name[0], name[-1])
l = len(name)
print(l)

#27
print(name[-1::-1])

#28
if '@' in name:
    print(True)
else:
    print(False)

#29
sentence = "I am learning Python"
if 'python' in sentence:
    print(f"Python is present in {sentence}")
else:
    print(f"Python is not present in {sentence}")

#30
print(name+" "+sentence)
