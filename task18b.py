from collections import deque


grid = [[72*72] * 71 for _ in range(71)]

def in_grid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

def reset_grid():
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            v = grid[x][y]
            if v > -1:
                grid[x][y] = 72 * 72

def bsf():
    grid[0][0] = 0
    q = deque()
    q.append((0, 0))
    while len(q) > 0:
        x, y = q.popleft()
        val = grid[x][y] + 1
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if in_grid(nx, ny) and grid[nx][ny] > val:
                grid[nx][ny] = val
                q.append((nx, ny))


with open("input.txt") as in_file:
    for l in in_file:
        a, b = [int(v) for v in l.split(",")]
        grid[a][b] = -1
        reset_grid()
        bsf()
        if grid[70][70] == 72 * 72:
            print(f"{a},{b}:", grid[70][70])
            break

