#Exercise 5 — Access Verifier

user = input("Enter your user name: ")
password = input("Enter your password: ")

if user == "alex" and password == "python123":
    print("Welcome Alex !")
elif user == "alex" and password != "python123":
    print("Wrong password !")
else:
    print("User not found")
