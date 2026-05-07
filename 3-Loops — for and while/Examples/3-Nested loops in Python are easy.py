# Nested loops in Python are easy
# nested loop = A loop within another loop (outer, inner)
# outer loop:
#    inner loop:

for x in range(1,10):
    print(x, end="")# The `end` function is used to print everything on the same line.

print()

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()# line break

print()

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()


