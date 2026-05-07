#Exercise 3 — Basic calculator

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /) : ")
if operation == "+":
    print(f"The sum is: {number1 + number2}")
elif operation == "-":
    print(f"The subtraction is: {number1 - number2}")
elif operation == "*":
    print(f"The multiplication is: {number1 * number2}")
elif operation == "/":
    print(f"The division is: {number1 / number2}")
else:
    print("Incorrect sign, remember you only have these options (+, -, *, /)")




