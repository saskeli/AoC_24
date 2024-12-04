import re

reg = re.compile("(do(n't)?\\(\\)|mul\\(\\d\\d?\\d?,\\d\\d?\\d?\\))")
acc = 0
add = True
with open("input.txt") as in_file:
    data = in_file.read()
    for r in reg.findall(data):
        if r[0].startswith("don"):
            add = False
            continue
        if r[0].startswith("do"):
            add = True
            continue
        if add:
            splits = r[0][4:-1].split(",")
            acc += int(splits[0]) * int(splits[1])
print(acc)        
