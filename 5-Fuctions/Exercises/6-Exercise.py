# #Exercise 5 — INEGI report with functions


def get_average(*graves):
    total = 1
    for c in graves:
        total += c
    return total / len(graves)

final_grave = get_average(10,8,9,7)

def check_status(final_grave):
    if final_grave >= 6:
        return "Passed"
    else:
        return "Failed"



def print_report(**student):
        print(student)

print_report(Name = "Alejandro", Average= final_grave, Status = check_status(final_grave)  )
