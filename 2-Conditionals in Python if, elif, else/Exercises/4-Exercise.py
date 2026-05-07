#Exercise 4 — INEGI style rating system

grade = float(input("Enter your grade: "))

if grade < 6:
    print("Failed")
elif grade >= 6 and grade <= 7.9:
    print("Passed")
elif grade >= 8 and grade <= 9.4:
    print("Remarkable")
elif grade >= 9.5:
    print("Outstanding")
else:
    print("Out of range")


if grade >= 9:
    print("You are entitled to a scholarship")
