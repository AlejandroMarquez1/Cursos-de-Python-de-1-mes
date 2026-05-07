#Exercise 5 — Login system with attempts

attempts = 4
while attempts > 0:
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    if user == "alex" and password == "python123":
        print("Welcome Alex!")
        break
    else:
        attempts -= 1
        print(f"Wrong credentials. {attempts} attempts left.")
else:
    print("Account blocked")

