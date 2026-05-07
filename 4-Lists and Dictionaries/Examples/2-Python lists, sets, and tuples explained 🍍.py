# Python lists, sets, and tuples explained 🍍
# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicate OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicate OK. FASTER

# LIST

fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))
# print(help(fruits))

# print(len(fruits)) # count the values in your list
# print("pineapple" in fruits) # Confirm if the value is in the list

# fruits[0] = "pineapple" # add a new value with the index marked
# fruits.append("pineapple") # add a new value but at the finally
# fruits.remove("apple") # removes the given value
# fruits.insert(0,"pineapple") # add a new value with the index marked
# fruits.sort()
# fruits.reverse() # reverse the list
# fruits.clear() # delete or clear the entire list
# print(fruits.index("apple")) # find the index of the value
# print(fruits.count("pineapple")) # Count how many times the value is present

# print(fruits[0]) # one value, numbers represent the index begin in 0
# print(fruits[0:3]) # A beginning and an end are placed.
# print(fruits[::]) # Print the entire list, or you can specify where it starts; you can also make it a negative list.

# for fruit in fruits: # Print the entire list
#    print(fruit)

print(fruits)


#SET

fruits = {"apple", "orange", "banana", "coconut"}

# print(dir(fruits))
# print(help(fruits))

# print(len(fruits)) # count the values in your list
# print("pineapple" in fruits) # Confirm if the value is in the list


# print(fruits[0]) # It gives an error because it doesn't have an index.
# fruits.add("pineapple") # add a new valor
# fruits.remove("apple") # removes the marked value
# fruits.pop() # removes the radom value
# fruits.clear() # removes all
print(fruits)


#TUPLE

fruits = ("apple", "orange", "banana", "coconut", "coconut")

# print(dir(fruits))
# print(help(fruits))

# print(len(fruits)) # count the values in your list
# print("pineapple" in fruits) # Confirm if the value is in the list
# print(fruits.index("apple"))
# print(fruits.count("coconut")) #It counts the same as how many values are there in the list
print(fruits)