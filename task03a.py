import re

reg = re.compile("mul\\(\\d\\d?\\d?,\\d\\d?\\d?\\)")
acc = 0
with open("input.txt") as in_file:
    data = in_file.read()
    for r in reg.findall(data):
        splits = r[4:-1].split(",")
        acc += int(splits[0]) * int(splits[1])
print(acc)        
