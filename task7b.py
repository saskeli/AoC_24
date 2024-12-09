
def rec(current, values, index, target):
    if current > target:
        return 0
    if index == len(values):
        return current if current == target else 0
    v = rec(current + values[index], values, index + 1, target)
    if v:
        return v
    v = rec(current * values[index], values, index + 1, target)
    if v:
        return v
    v = rec(int(str(current) + str(values[index])), values, index + 1, target)
    return v
    

def do_stuff(line):
    line = line.split()
    res = int(line[0][:-1])
    line = [int(v) for v in line[1:]]
    return rec(line[0], line, 1, res)

acc = 0

with open("input.txt") as in_file:
    for line in in_file:
        acc += do_stuff(line.strip())

print(acc)