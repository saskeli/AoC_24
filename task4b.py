
acc = 0

def match_ex(lines, i, j):
    if i == 0 or j == 0 or i == len(lines) - 1 or j == len(lines[i]) - 1:
        return False
    a = lines[i - 1][j - 1] == 'M' and lines[i + 1][j + 1] == 'S'
    b = lines[i - 1][j - 1] == 'S' and lines[i + 1][j + 1] == 'M'
    c = lines[i - 1][j + 1] == 'M' and lines[i + 1][j - 1] == 'S'
    d = lines[i - 1][j + 1] == 'S' and lines[i + 1][j - 1] == 'M'
    return (a or b) and (c or d)

def match(lines, i, j):
    return match_ex(lines, i, j)

with open("input.txt") as in_file:
    lines = in_file.readlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'A':
                pm = match(lines, i, j)
                acc += pm

print(acc)