#Exercise 2 — Countdown
age = int(input("Enter your age: "))
while age < 0 or age > 120:
    print("Your age must be between 0 and 120")
    age = int(input("Enter your age: "))

print(f"Valid age:{age}")

