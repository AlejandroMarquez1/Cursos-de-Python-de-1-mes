#Flow Control Structures in Python: while, for, break, continue

counter = 3
while counter > 0:
    counter = counter - 1
    print(f"The counter's contents are: {counter}")

print()

for x in range (5):
    if x == 3:
        continue
    print(x)

print()

attempts = 3
while attempts > 0:
    if input("Enter your password: ") == "password":
        print("Welcome to the password locker!")
        break
    attempts = attempts - 1
    print("wrong password")
else:
    print("The attempts are over")