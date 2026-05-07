# While loops in Python are easy!
# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You did nor enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}" )

print()

age = int(input("Enter your age: "))

while age <= 0 :
    print("Age can't be negative or 0")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")

print()

food = input("Enter a food you like (x to quit): ")

while not food == "x":
    print(f"You like {food}")
    food = input("Enter a food you like (x to quit): ")
print(f"Bye {name}")

print()

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))
print(f"Your number is {num}")