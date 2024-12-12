from collections import defaultdict

r_dict = defaultdict(list)

def validate(vals):
    forbidden = set()
    for i in range(len(vals)):
        v = vals[i]
        if v in forbidden:
            return i
        forbidden.update(r_dict[v])
    return 0

def fix(vals, vr):
    tmp = vals[vr]
    vals[vr] = vals[vr - 1]
    vals[vr - 1] = tmp
    vr = validate(vals)
    while vr != 0:
        tmp = vals[vr]
        vals[vr] = vals[vr - 1]
        vals[vr - 1] = tmp
        vr = validate(vals)
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
            vals = [int(v) for v in line.split(",")]
            vr = validate(vals)
            if vr == 0:
                continue
            acc += fix(vals, vr)

print(acc)