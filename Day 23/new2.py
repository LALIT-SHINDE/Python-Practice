import json

x = '{"Name":"Lalit", "Age":22, "City":"Nashik"}'
y = json.loads(x)

print(y)
print(y["Name"])
print(y["Age"])
print(y["City"])

x = {"Name":"Lalit", "Age":22, "City":"Nashik"}
print(x, type(x))

y = json.dumps(x)
print(y,type(y))

print(json.dumps([12,3,24,54,6,64,7,8,9]))
print(json.dumps((43,56,6,4,3,5)))
print(json.dumps("Lalit"))
print(json.dumps(43))
print(json.dumps(32.43))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
        "Name" : "Lalit",
        "Age" : 22,
        "Married" : True,
        "Divorced" : False,
        "Childern" : ("Billy","Tommy"),
        "Pets" : None,
        "Cars" : [{"Model":"BMW M60","mpg": 342, "Model":"Mercedes", "mpg":542}]
    }

print(json.dumps(x, sort_keys = True))

# Output
# {'Name': 'Lalit', 'Age': 22, 'City': 'Nashik'}
# Lalit
# 22
# Nashik
# {'Name': 'Lalit', 'Age': 22, 'City': 'Nashik'} <class 'dict'>
# {"Name": "Lalit", "Age": 22, "City": "Nashik"} <class 'str'>
# [12, 3, 24, 54, 6, 64, 7, 8, 9]
# [43, 56, 6, 4, 3, 5]
# "Lalit"
# 43
# 32.43
# true
# false
# null
# {"Age": 22, "Cars": [{"Model": "Mercedes", "mpg": 542}], "Childern": ["Billy", "Tommy"], "Divorced": false, "Married": true, "Name": "Lalit", "Pets": null}
