#Conditionals and Booleans - If, Else, and Elif Statements

# Comparisons:
# Equal:  ==
# Not equal:  !=
# Greater than:  >
# Less than:  <
# Greater or equal:  >=
# Less or equal:  <=



if True:
    print("Conditional was True")
print("")

language = "Java"
if language == "Python":
    print("Language is python")
elif language == "Java":
    print("Language is java")
elif language == "JavaScript":
    print("Language is javascript")
else:
    print("No match")
print("")


# and
# or
# not

user = "admin"
logged_in = False

if user == "admin" and logged_in:
    print("Admin page")
else:
    print("Bad creds")

if user == "admin" or logged_in:
    print("Admin page")
else:
    print("Bad creds")


if not logged_in:
    print("Please log in")
else:
    print("Welcome")
print("")



# Advice
# False values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, "", (), [] .
# Any empty mapping. For example, {}.
