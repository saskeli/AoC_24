
grid = []

with open("input.txt") as in_file:
    for line in in_file:
        grid.append(list(line.strip()))

def print_grid():
    for line in grid:
        print("".join(line))

def in_grid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

def rec(x, y, locs):
    locs.add((x, y))
    a = 1
    e = 0
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in locs:
            continue
        if not in_grid(nx, ny) or grid[nx][ny] != grid[x][y]:
            e += 1
        else:
            aa, ae = rec(nx, ny, locs)
            a += aa
            e += ae
    return a, e

def compute(x, y):
    locs = set()
    a, e = rec(x, y, locs)
    #print(x, y, grid[x][y], a * e)
    for loc in locs:
        grid[loc[0]][loc[1]] = '0'
    #print_grid()
    return a * e

acc = 0

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] != '0':
            acc += compute(x, y)

print(acc)