#Python dictionaries are easy 📙
# dictionary = a collection of {Key:Value} pairs
# ordered and changeable. No duplicate

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA")) # find or print the value of the key you assigned
# print(capitals.get("Japan))


# if capitals.get("Japan"):
#    print("That capital exists")
# else:
#    print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China") #remove the key
# capitals.popitem() #remove the last key

# keys = capitals.keys() # It only prints the keys

# for key in capitals.keys():
#    print(key)

# values = capitals.values() # It only prints the key values
# for value in capitals.values():
#    print(value)

items = capitals.items() # Print the entire dictionary, keys, and values.
for key, value in capitals.items():
    print(f"{key} -> {value}")