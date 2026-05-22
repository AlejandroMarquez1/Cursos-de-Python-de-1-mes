#Exercise 3 — Note Sorter

def classify(grade):
    if grade < 6 :
        print("Failed")
    elif grade <= 7.9 :
        print("Passed")
    elif grade <= 9.4 :
        print("Remarkable")
    elif grade >= 9.5 and grade < 10:
        print("Outstanding")
    else :
        print("invalid value")

classify(5.9)
classify(7)
classify(8)
classify(11)
