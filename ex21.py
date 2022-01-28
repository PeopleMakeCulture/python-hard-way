def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a *b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30,5) # 35
height = subtract(78, 4) # 74
weight = multiply(90,2) # 180
iq = divide(100,2) # 50

print(f"Age: {age}, Height: {height}, Weight: {weight} IQ: {iq}")


print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2)))) # 35 + 74 - (25 * 180)

print("That becomes: ", what, "Can you do it by hand?" )
