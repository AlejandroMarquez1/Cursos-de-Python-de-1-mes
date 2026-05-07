#If statements in Python are easy (if, elif, else) 🤔

# If = Do some code only IF some condition is True
# Else do something else

age = int(input("Enter your age: "))
if age >= 100:#Remember, to evaluate conditions, put the conditions in order and which one you want to evaluate first.
    print("You are too old to sing up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sing up")

print("")

response = input("Would you like food? (Y/N): ")
if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")
print("")

name = input("Enter your name: ")
if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}!")
print("")

for_sale = True
if for_sale:
    print("This item is for sale!")
else:
    print("This item is NOT for sale!")