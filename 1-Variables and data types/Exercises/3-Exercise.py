#Exercise 3 — Technology Store

keyboard = 350.50
mouse = 199.99
earphones = 899.00

total = keyboard + mouse + earphones
print(f"The total is ${total}")
print(f"Can you buy it?: {total <= 1000}")
print("If it's positive you have too many, and if it's negative you don't have enough.")
print(f"Difference:{1000-total}")