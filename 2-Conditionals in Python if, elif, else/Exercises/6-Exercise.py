#Exercise 6 — Applicant profile for INEGI

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))
know = input("Do you know Python? (S/N): ")


if age >= 18 and age <= 25:
    age = True
else:
    age = False
if gpa>=8 and gpa<=10:
    gpa = True
else:
    gpa = False
if know == "S":
    know = True
else:
    know = False

if age == True and gpa == True and know == True:
    print(f"Congratulations {name}, you meet all the requirements")

if age == False and gpa== False and know == False:
    print("You do not meet any of the requirements to join the company")

if not age :
    print("Your age is not efficient in the company")
if not gpa:
    print("Your GPA is not efficient in the company")
if not know:
    print("You need to know Python to be able to join the company")

