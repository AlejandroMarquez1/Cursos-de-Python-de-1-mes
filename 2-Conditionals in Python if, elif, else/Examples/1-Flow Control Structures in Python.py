#Flow Control Structures in Python: if, else, elif

nota = float(input("Enter your note:"))
if nota < 5:
    print("You are suspended")
else:
    print("You've passed, congratulations!")


nota2 = float(input("Enter your note:"))
if 0 <= nota2 and nota2 < 5:
    print("You are suspended")
elif 5 <= nota2 and nota2 < 7:
    print("Approved")
elif 7 <= nota2 and nota2 < 9:
    print("Remarkable")
elif nota2 <= 9 and nota2 <= 10:
    print("Outstanding")
else:
    print("Note out of range")
