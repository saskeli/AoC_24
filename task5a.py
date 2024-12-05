from collections import defaultdict

r_dict = defaultdict(list)

def validate(vals):
    forbidden = set()
    for v in vals:
        if v in forbidden:
            return 0
        forbidden.update(r_dict[v])
    return vals[len(vals) // 2]

acc = 0

with open("input.txt") as in_file:
    for line in in_file:
        if len(line) < 2:
            continue
        if "|" in line:
            s = line.split("|")
            r_dict[int(s[1])].append(int(s[0]))
        else:
            acc += validate([int(v) for v in line.split(",")])

print(acc)