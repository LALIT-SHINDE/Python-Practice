
def add(*n):
    total = 0
    for i in n:
        total += i

    return f"Addition of {n}: {total}"

def subtract(*n):
    total = n[0]
    for i in n:
        total -= i

    return f"Substration of {n}: {total}"

def multiply(*n):
    total = 1
    for i in n:
        total *= i
    return f"Multification of {n}: {total}"

def divide(*n):
    total = n[0]
    try:
        for i in n[1:]:
            total /= i
        return f"Divison of {n}: {total}"

    except ZeroDivisionError:
        print("Error: Can not Divided BY Zero")
