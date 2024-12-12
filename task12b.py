
grid = []

with open("input.txt") as in_file:
    for line in in_file:
        grid.append(list(line.strip()))

def print_grid():
    for line in grid:
        print("".join(line))

#print_grid()

def in_grid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

def rec(x, y, locs, v_parts, h_parts):
    locs.add((x, y))
    a = 1

    # down:
    nx, ny = x + 1, y
    if (nx, ny) in locs:
        pass
    elif not in_grid(nx, ny) or grid[nx][ny] != grid[x][y]:
        h_parts.append((nx, y))
    else:
        a += rec(nx, ny, locs, v_parts, h_parts)
    
    # up:
    nx, ny = x - 1, y
    if (nx, ny) in locs:
        pass
    elif not in_grid(nx, ny) or grid[nx][ny] != grid[x][y]:
        h_parts.append((x, y))
    else:
        a += rec(nx, ny, locs, v_parts, h_parts)

    # right:
    nx, ny = x, y + 1
    if (nx, ny) in locs:
        pass
    elif not in_grid(nx, ny) or grid[nx][ny] != grid[x][y]:
        v_parts.append((ny, x))
    else:
        a += rec(nx, ny, locs, v_parts, h_parts)

    # right:
    nx, ny = x, y - 1
    if (nx, ny) in locs:
        pass
    elif not in_grid(nx, ny) or grid[nx][ny] != grid[x][y]:
        v_parts.append((y, x))
    else:
        a += rec(nx, ny, locs, v_parts, h_parts)
    
    return a

def check_break(a1, a2, b1, b2):
    if not in_grid(a1[0], a1[1]):
        return False
    if not in_grid(a2[0], a2[1]):
        return False
    if not in_grid(b1[0], b1[1]):
        return False
    if not in_grid(b2[0], b2[1]):
        return False
    if grid[a1[0]][a1[1]] == grid[a2[0]][a2[1]]:
        return False
    if grid[b1[0]][b1[1]] == grid[b2[0]][b2[1]]:
        return False
    return True

def compute(x, y):
    locs = set()
    v_parts = []
    h_parts = []
    a = rec(x, y, locs, v_parts, h_parts)
    #print(x, y, grid[x][y])
    
    e = 1
    h_parts.sort()
    v_parts.sort()
    #print(h_parts)
    #print(v_parts)
    i = 0
    ca, cb = h_parts[0]
    while i + 1 < len(h_parts):
        na, nb = h_parts[i + 1]
        if ca != na or cb + 1 != nb:
            #print("h split", i, i + 1)
            e += 1
        elif check_break((ca - 1, cb), (ca - 1, cb + 1), (ca, cb), (ca, cb + 1)):
            #print("h split", i, i + 1)
            e += 1
        i += 1
        ca, cb = na, nb
    e += 1
    i = 0
    ca, cb = v_parts[0]
    while i + 1 < len(v_parts):
        na, nb = v_parts[i + 1]
        if ca != na or cb + 1 != nb:
            #print("v split", i, i + 1)
            e += 1
        elif check_break((cb, ca - 1), (cb + 1, ca - 1), (cb, ca), (cb + 1, ca)):
            #print("v split", i, i + 1)
            e += 1
        i += 1
        ca, cb = na, nb
    #print("->", a, e, a * e)
    for loc in locs:
        grid[loc[0]][loc[1]] = '0'
    return a * e

acc = 0

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] != '0':
            acc += compute(x, y)

print(acc)