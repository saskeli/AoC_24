
from collections import defaultdict

t_dict = defaultdict(list)

patterns = []

with open("input.txt") as in_file:
    for line in in_file:
        if len(t_dict) == 0:
            towels = [s.strip() for s in line.split(",")]
            for towel in towels:
                t_dict[towel[0]].append(towel)
        elif len(line) <= 1:
            continue
        else:
            patterns.append(line.strip())

r_dict = {}

def make(pattern, i=0):
    if pattern[i:] in r_dict:
        return r_dict[pattern[i:]]
    if i == len(pattern):
        return True
    for towel in t_dict[pattern[i]]:
        ok = True
        for j in range(len(towel)):
            if len(pattern) <= i + j or pattern[i + j] != towel[j]:
                ok = False
        if ok and make(pattern, i + len(towel)):
            r_dict[pattern[i:]] = True
            return True
    r_dict[pattern[i:]] = False
    return False

acc = 0
for pattern in patterns:
    acc += make(pattern)

print(acc)