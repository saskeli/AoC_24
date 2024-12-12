
grid = []

with open("input.txt") as in_file:
    for line in in_file:
        grid.append([c for c in line.strip()])

x = -1
y = -1
cont = True
for i in range(len(grid)):
    for j in range(len(grid[x])):
        if (grid[i][j] in "^v<>"):
            x = i
            y = j
            cont = False
            break
    if not cont:
        break

def in_grid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

dirmap = {
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0)
}

nextdir = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

direction = dirmap[grid[x][y]]

steps = 1
grid[x][y] = "x"
nx, ny = x + direction[0], y + direction[1]
while (in_grid(nx, ny)):
    if (grid[nx][ny] == '#'):
        direction = nextdir[direction]
        nx, ny = x + direction[0], y + direction[1]
    if (grid[nx][ny] == '.'):
        steps += 1
        grid[nx][ny] = 'x'
    x, y = nx, ny
    nx, ny = x + direction[0], y + direction[1]
print(steps)