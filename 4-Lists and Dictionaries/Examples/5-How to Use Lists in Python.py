#How to Use Lists in Python

"""
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combine = zeros + letters
numbers = list(range(20))
chars = list("Hello World")
print(numbers)
print(chars)
print(len(chars))

"""

#Accessing Items

"""
letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0])
print(letters[-1])
print(letters)
print(letters[:3])
print(letters[::2])

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])
"""

#Looping over lists

"""
letters = ["a", "b", "c"]

for letter in enumerate(letters):
    print(letter[0], letter[1])

"""

#Adding/Removing items

"""
letters = ["a", "b", "c"]

#add
letters.append("d")
letters.insert(0, "-")
print(letters)


#remove
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)
"""

#Finding items

letters = ["a", "b", "c"]
print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))
print(letters.index("a"))
