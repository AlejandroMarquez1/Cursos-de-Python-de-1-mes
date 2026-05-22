# #Exercise 5 — Login system with function



def loing(user, password):
    if user == "alex" and password == "python123":
        return True
    else:
        return False

counter = 0


while counter < 3 :
    print("Welcome :)")
    print("Introduce your username and password")
    user = input('Enter your username :')
    password = input("Enter your password :")
    if loing(user, password):
        break
    else:
        counter += 1
        print("Try again")
