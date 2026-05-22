# Python Functions | Python Tutorial for Absolute Beginners #1
# Functions

def greet():
    print("Hi there")
    print("Welcome aboard")


greet()


# Arguments
def hello(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome")


hello("Alejandro", "Marquez")


# Type of functions
def greet2(name):
    print(f"Hi {name}")


# 1- Perform a task
# 2- Return a value
def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Alejandro")
print(message)


# Keyword Arguments

def increment(number, by):
    return number + by


result = increment(1, 2)
print(result)
print(increment(8, 9))

# Default Arguments

"""
def increment(number = 5, by = 1):
    return number + by
"""


# *args, wait, what?


def multiply(*numbers):
    total = 1
    for n in numbers:
        total *= n
    return total


print(multiply(3, 4, 4, 5))


# **args
def save_user(**user):
    print(user)


save_user(id=1, name="Alejandro", age=19)

# Scope

message = "a"


def greet(name):
    global message
    message = "b"


greet("Alex")
print(message)