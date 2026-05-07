#Data
#Four data type
#String = "Hey my name is alex"
#Int = 90 or -10
#Float = 2.344 or -10.45
#Boolean = True and False

#To print a message, use print and needs one argument.
print("Hello Alex")
print("Hello Alex", 56, 10.39, False)
print("")

#Comments

#Type the data
print(type("Hello Alex"))
print("")

#Variable
#It's like a box where you can store whatever you put in it.
box = "hi"
print(box)
print("")
#You can not with a number when you begin.
#1variable = 3 = Mistake

#Operators
#Operators are used to work with the data
number1 = 3
number2 = 2
print(f"Addition: {number1 + number2}")
print(f"Subtraction: {number1 - number2}")
print(f"Multiplication: {number1 * number2}")
print(f"Division: {number1 / number2}")
print(f"Remainder: {number1 % number2}")
print(f"Exponent: {number1 ** number2}")
print(f"Floor: {number1 // number2}")
print("")

#If you want to specify an order, use parentheses.
#Before
print(1 + 1 * 4)
#After
print((1 + 1) * 4)
print("")

#Relational operators
"""
>
<
==
>=
<=
"""
print(f"Greater than:{1 > 2}")
print(f"Less than:{1 < 2}")
print(f"Equal to:{1 == 2}")
print(f"Greater than or equal to:{1 >= 2}")
print(f"Less than or equal to:{1 <=2 }")
print(f"Different than{1 != 2}")
print("")

#Logical operators
print(not True)
print(not False)
print("")
#It does the opposite

print("")
print(False or False)
print(True or True)
print(True or False)

print("")
print(True and True)
print(True and False)
print(False or True)
print("")
#Table of operators and their functions
#https://ellibrodepython.com/operadores-logicos
#Order is important

#Example:

average = (8 + 8 + 9)/3
print(f"Note:{average}")
print(f"it's remarkable? {average >= 8 and average <= 10}")