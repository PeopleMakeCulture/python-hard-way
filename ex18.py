# indent all lines of code in the function four spaces
# `*args` tells Python to take all the arguments to the function and put them in args
def print_two(*args):
    arg1, arg2 = args # what if we give more or less than 2 args?
    print(f"arg1: {arg1}\narg2: {arg2}")

#refactored
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}\narg2: {arg2}")


def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing.")

print_two("z", "s")
print_two_again("z", "s")
print_one("1st")
print_none()
