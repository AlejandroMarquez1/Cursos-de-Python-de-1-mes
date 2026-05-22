#Exercise 4 — BMI with message

def bmi_calculate(weight, height):
    bmi = weight / (height ** 2)
    if 0 > bmi < 18.5:
        return "Underweight"
    elif 18.5 > bmi <= 24.9:
        return "Normal weight"
    elif 25 > bmi <= 30:
        return "Overweight"
    elif bmi > 35:
        return "Obese"

person1 = bmi_calculate(65, 1.65)
print(person1)
person2 = bmi_calculate(30, 1.70)
print(person2)
person3 = bmi_calculate(200, 1.75)
print(person3)
