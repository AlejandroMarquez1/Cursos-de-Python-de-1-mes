#Exercise 4 — Guess the number

secret_num = 7
num = int(input("Guess the secret number: "))
while num != secret_num:
    if num > secret_num:
        print("Your guess is too high.")
        num = int(input("Guess the secret number: "))
    elif num < secret_num:
        print("Your guess is too low.")
        num = int(input("Guess the secret number: "))
print("You guessed right!")
