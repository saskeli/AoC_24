
data = []

with open("input.txt") as in_file:
    start = 0
    file_id = 0
    is_file = True
    for c in in_file.readline():
        data.append([start, int(c), file_id if is_file else -1])
        file_id += is_file
        is_file = not is_file
        start += int(c)

idx = len(data) - 1
res = 0

def printall():
    print(data)
    for _, le, f_id in data:
        prb = str(f_id) if f_id != -1 else "."
        print(prb * le, end="")
    print()

while idx >= 0:
    if data[idx][2] == -1:
        idx -= 1
        continue
    moved = False
    for trg in range(idx):
        if data[trg][2] == -1 and data[trg][1] >= data[idx][1]:
            for i in range(data[idx][1]):
                res += (data[trg][0] + i) * data[idx][2]
            data[trg][0] += data[idx][1]
            data[trg][1] -= data[idx][1]
            moved = True
            idx -= 1
            break
    if moved:
        continue
    for i in range(data[idx][1]):
        res += (data[idx][0] + i) * data[idx][2]
    idx -= 1

print(res)    