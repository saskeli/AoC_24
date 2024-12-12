
grid = []

with open("input.txt") as in_file:
    for line in in_file:
        #print(line.strip())
        grid.append(line.strip())

def in_grid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])

acc = 0

def rec(x, y, s, indent):
    #print(indent, grid[x][y], "at", x, y)
    if grid[x][y] == "9":
        s.add((x, y))
        return
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    c_val = int(grid[x][y])
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if in_grid(nx, ny):
            n_val = int(grid[nx][ny])
            if c_val + 1 == n_val:
                rec(nx, ny, s, indent + "    ")

def climb(x, y):
    s = set()
    rec(x, y, s, "")
    return len(s)

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if (grid[x][y] == "0"):
            acc += climb(x, y)

print(acc)