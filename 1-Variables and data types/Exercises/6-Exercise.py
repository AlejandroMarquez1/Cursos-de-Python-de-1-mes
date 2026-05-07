#Exercise 6 — GPA Real
english = 10
programming = 10
calculation_of_variables = 7
optimization = 8
AI = 9
gpa = (english + programming + calculation_of_variables + optimization + AI)/5
print(f"Your GPA is {gpa}")
print(f"Did I pass them all?: {english >= 6 and programming >= 6 and 
calculation_of_variables >= 6 and optimization >= 6 and AI >= 6}")
print(f"Are you eligible for a scholarship?: {gpa >= 8.5}")
print("If it's positive you have too many, and if it's negative you don't have enough.")
print(f"How many points do you need or how many do you need for a scholarship?: {gpa - 8.5}")
