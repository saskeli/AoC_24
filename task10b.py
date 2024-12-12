
grid = []

with open("input.txt") as in_file:
    for line in in_file:
        #print(line.strip())
        grid.append(line.strip())

def in_grid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])

acc = 0

def rec(x, y, indent):
    #print(indent, grid[x][y], "at", x, y)
    if grid[x][y] == "9":
        return 1
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    c_val = int(grid[x][y])
    res = 0
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if in_grid(nx, ny):
            n_val = int(grid[nx][ny])
            if c_val + 1 == n_val:
                res += rec(nx, ny, indent + "    ")
    return res

def climb(x, y):
    return rec(x, y, "")

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if (grid[x][y] == "0"):
            acc += climb(x, y)

print(acc)