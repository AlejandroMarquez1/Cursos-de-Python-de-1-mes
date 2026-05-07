#Logical operators in Python are easy 🔣

# Logical operators = used on conditional statements
# and = checks two oe more conditions if True
# or = checks if at least one condition is True
# not = True if condition is False, and vice versa


#And
temp = 25

if temp > 0 and temp < 30:
    print("The temperature is good")
else :
    print("The temperature is bad")
print("")


#Or
temp2 = 80
if temp2 <= 0 or temp2 >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")
print("")

#Not

sunny = False
if not sunny: #What happens with not, it inverts the negation for the condition
    print("It is cloudy outside")
else:
    print("It is sunny outside")
