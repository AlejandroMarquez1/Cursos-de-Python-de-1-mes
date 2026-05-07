# Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs

student = { "name": "John", "age": 25, "courses": ["Math", "CompSci"]}
# print(student["courses"])
# print(student["name"])

# student["name"] = "Jane"
# student["phone"] = "5555-5555-5555"
# print(student.get("phone", "Not found"))

# student.update({"name": "Jane", "age": 26, "phone": "5555-5555-5521"})
# del student["age"]
# age = student.pop("age")

# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())

for key, value in student.items():
    print(key, value)