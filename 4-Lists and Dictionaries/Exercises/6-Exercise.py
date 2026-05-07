#Exercise 6 — INEGI mini database

INEGI =[
    {"Name": "Alex", "Age": 19, "salary": 9200, "work": True},
    {"Name": "Maria", "Age": 78, "salary": 0,"work": False },
    {"Name": "Juan", "Age": 90, "salary": 7000, "work": False},
    {"Name": "Pepe", "Age": 28, "salary": 19000, "work": True}
]

box = 0

for person in INEGI:
    if person["Age"] >= 18 and person["work"] :
        print(f"You meet the requirements:{person["Name"]}")
        box += 1

print(f"The people who meet the requirements are: {box}")

