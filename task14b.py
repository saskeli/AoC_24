from collections import deque

bots = []

with open("input.txt") as in_file:
    for line in in_file:
        ss = line.split()
        p, v = ss[0], ss[1]
        bots.append((tuple(int(vv) for vv in p[2:].split(",")), tuple(int(vv) for vv in v[2:].split(","))))

width = 101
height = 103

steps = 0

def flood(grid, x, y):
    s = {x, y}
    q = deque()
    q.append((x, y))
    while len(q) > 0:
        px, py = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = (px + dx) % width
            ny = (py + dy) % height
            if grid[ny][nx] == "#" and (nx, ny) not in s:
                s.add((nx, ny))
                q.append((nx, ny))
    return len(s)

def make_grid():
    grid = [[" " for _ in range(width)] for _ in range(height)]
    max_clump = 0
    for (x, y), _ in bots:
        grid[y][x] = "#"
        cs = flood(grid, x, y)
        max_clump = max(cs, max_clump)
    return grid, max_clump

def print_grid(grid):
    print("\n".join(["".join(l) for l in grid]))

stop = ""
while len(stop) == 0:
    grid, clump = make_grid()
    print(steps, clump)
    if clump > 100:
        print_grid(grid)
        stop = input("Stop?")
    bots = [
        (((x + dx) % width, (y + dy) % height), (dx, dy))
        for (x, y), (dx, dy) in bots
    ]
    steps += 1
