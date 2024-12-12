
acc = 0

offsets = []

for a in [-1, 0, 1]:
    for b in [-1, 0, 1]:
        if a != 0 or b != 0:
            offsets.append((a, b))

def match_off(lines, i, j, dx, dy):
    ma = "MAS"
    for ci in range(len(ma)):
        i += dx
        j += dy
        if not (0 <= i < len(lines)) or not (0 <= j < len(lines[i])) or lines[i][j] != ma[ci]:
            return 0
    return 1

def match(lines, i, j):
    return sum(
        match_off(lines, i, j, o[0], o[1]) 
        for o in offsets
    )

with open("input.txt") as in_file:
    lines = in_file.readlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'X':
                pm = match(lines, i, j)
                acc += pm

print(acc)