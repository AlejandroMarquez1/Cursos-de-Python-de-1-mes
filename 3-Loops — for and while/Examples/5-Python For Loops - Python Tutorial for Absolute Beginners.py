#Python For Loops - Python Tutorial for Absolute Beginners\

for number in range(1, 10, 2):
    print(f"Attempt {number} {number * "."}")

print()

successful = True
for x in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempt 3 times and failed")

print()

for x in range(5):
    for y in range(3):
        print(f"({x} , {y})")

print()

for x in "Python":
    print(x)

print()
