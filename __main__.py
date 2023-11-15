from mc_api_checker import check_availible
from word_checker import verify_word
from namelist import letter_combos

names = []

for combination in letter_combos():
    if verify_word("".join(combination)):
        if check_availible("".join(combination)):
            print("FOUND ONE! %s" % "".join(combination))
            names.append("".join(combination))

with open("names.txt", "w") as f:
    f.write(", ".join(names))