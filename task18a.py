from collections import deque


grid = [[72*72] * 71 for _ in range(71)]

with open("input.txt") as in_file:
    for i in range(1024):
        l = in_file.readline()
        a, b = [int(v) for v in l.split(",")]
        grid[a][b] = -1

grid[0][0] = 0

q = deque()

def in_grid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

q.append((0, 0))

while len(q) > 0:
    x, y = q.popleft()
    val = grid[x][y] + 1
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x + dx, y + dy
        if in_grid(nx, ny) and grid[nx][ny] > val:
            grid[nx][ny] = val
            q.append((nx, ny))

print(grid[70][70])
