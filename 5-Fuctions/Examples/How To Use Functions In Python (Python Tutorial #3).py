def function():
    print("Ahhhhhh")
    print("ahhh2 ")


print("this is outside the function")
function()


def function2(x):
    return 2 * x


result = function2(5)
print(result)


def function3(x, y):
    return x + y


result = function3(5, 3)
print(result)


def function4(x):
    print(x)
    print("still in this fuction")
    return 3 * x


result = function4(4)
print(result)


def function5(some_argument):
    print(some_argument)
    print("weee")


function5(5)


# BMI calculator
def bmi_calculator(h, w):
    return w/(h*h)
person1 = bmi_calculator(2, 90)
person2 = bmi_calculator(1.8, 70)
person3 = bmi_calculator(2.5, 160)
print(f"Your BMI is {person1}")
print(f"Your BMI is {person2}")
print(f"Your BMI is {person3}")