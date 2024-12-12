
grid = []

x = 0
y = 0

with open("input.txt") as in_file:
    lx = 0
    for line in in_file:
        #print(line.strip())
        gl = []
        ly = 0
        for c in line.strip():
            if c in ".":
                gl.append(0)
            elif c in "#":
                gl.append(1)
            elif c in "^":
                gl.append(0)
                x = lx
                y = ly
            ly += 1
        grid.append(gl)
        lx += 1

def in_grid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

nextdir = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

di_bit = {
    (-1, 0): 0b10,
    (0, 1): 0b100,
    (1, 0): 0b1000,
    (0, -1): 0b10000
}

change_stack = []

def print_grid():
    print("Grid:")
    for r in grid:
        for v in r:
            if v == 0:
                print("  .   ", end="")
            elif v == 1:
                print("  #   ", end="")
            else:
                rep = bin(v)[2:]
                rep = "0" * (5 - len(rep)) + rep + " "
                print(rep, end="")
        print()

loopers = 0

def unroll():
    while len(change_stack) > 0:
        i, j, ov = change_stack.pop()
        grid[i][j] = ov

def walk(i, j, di):
    ni, nj = i + di[0], j + di[1]
    while in_grid(ni, nj):
        if grid[i][j] & di_bit[di] > 0:
            return 1
        change_stack.append((i, j, grid[i][j]))
        grid[i][j] |= di_bit[di]
        if grid[ni][nj] == 1:
            di = nextdir[di]
            ni, nj = i + di[0], j + di[1]
        else:
            i, j = ni, nj
            ni, nj = i + di[0], j + di[1]
    return 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            change_stack.append((i, j, 0))
            grid[i][j] = 1
            loopers += walk(x, y, (-1, 0))
            unroll()
    print(i, "->", loopers)

print(loopers)