
data = []

with open("input.txt") as in_file:
    file_id = 0
    is_file = True
    for c in in_file.readline():
        for i in range(int(c)):
            data.append(file_id if is_file else -1)
        file_id += is_file
        is_file = not is_file

a = 0
b = len(data) - 1

res = 0

while a < b:
    if data[a] != -1:
        res += a * data[a]
        a += 1
        continue
    if data[b] == -1:
        b -= 1
        continue
    data[a] = data[b]
    data[b] = -1
    res += a * data[a]
    a += 1

print(res)    