#Exercise 3 — Qualification List

qualification_list = [2, 3, 9, 10 ,4]

for qualification in qualification_list:
    if qualification >= 6:
        print(f"{qualification} -> Passed")
    else:
        print(f"{qualification} -> Failed")
