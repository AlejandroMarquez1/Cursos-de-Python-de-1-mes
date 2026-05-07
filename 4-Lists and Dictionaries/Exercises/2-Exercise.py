#Exercise 2 — Dictionary of your profile

profile = {"Name": "Alejandro", "Age": 19, "Gpa": 9.2, "City": "E.U"}

for person, items in profile.items():
    print(f"{person}: {items}")

profile.update({"Gpa": 9.8})

print(profile)
