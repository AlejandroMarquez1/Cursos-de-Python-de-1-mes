#Loops and Iterations - For / While
# "Continue" is used to stop a specific sentence and then continue with the rest.
# `break` is used to stop an entire sequence where you specify


for num in range(1,6):
    if num == 3:
        print("Found")
        continue
    print(num)

print()

for x in range(1,6):
    for l in "abc":
        print(f"{x} {l}")

print()

for i in range(1, 11):
    print(i)

print()

x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1


