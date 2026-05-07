# Learn Python for loops in 5 minutes!
# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, ect.

for x in range(1,11):
    print(x)

print()

for x in reversed(range(1,11)):# This function is used to change the order in which the sequence goes.
    print(x)
print("HAPPY NEW YEAR")

print()

for x in range(1,11,2):# Count by twos
    print(x)

print()

credit_card = "1234-56789-1011-1213"
for x in credit_card:
    print(x)

print()

for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)