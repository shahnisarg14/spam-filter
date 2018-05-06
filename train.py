import os
path = os.getcwd() + os.path.sep + "resources" + os.path.sep + "english_big.txt"

spam_count = 0
ham_count = 0
with open(path, "r") as file:
    for line in file:
        line = line.replace("\n", "")
        tokens = line.split(",")
        if tokens[-1] == "spam":
            spam_count += 1
        else:
            ham_count += 1
print spam_count, ham_count
