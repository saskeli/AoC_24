room = []

moves = []

x = 0
y = 0

rep_map = {
    ".": "..",
    "@": "@.",
    "#": "##",
    "O": "[]"
}

with open("input.txt") as in_file:
    make_room = True
    cx = 0
    for line in in_file:
        l = line.strip()
        if len(l) == 0:
            make_room = False
        elif make_room:
            l = list("".join(rep_map[c] for c in l))
            for cy, c in enumerate(l):
                if c == "@":
                    x = cx
                    y = cy
            room.append(list(l))
        else:
            moves += list(l)
        cx += 1

def print_room():
    print("\n".join(["".join(l) for l in room]))

print_room()

print(x, y)

move_map = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

def push_lr(dy):
    global x, y
    qy = y + dy
    while room[x][qy] == "]" or room[x][qy] == "[":
        qy = qy + dy
    if room[x][qy] == ".":
        while qy != y:
            room[x][qy] = room[x][qy - dy]
            qy -= dy
        room[x][y] = "."
        y += dy

def can_move(nx, ny, dx):
    if room[nx][ny] == ".":
        return True
    if room[nx][ny] == "#":
        return False
    if room[nx][ny] == "[":
        return can_move(nx + dx, ny, dx) and can_move(nx + dx, ny + 1, dx)
    else:
        return can_move(nx + dx, ny, dx) and can_move(nx + dx, ny - 1, dx)

def move_ud(nx, ny, dx):
    if room[nx][ny] == "[":
        if room[nx + dx][ny] in "[]":
            move_ud(nx + dx, ny, dx)
        if room[nx + dx][ny + 1] == "[":
            move_ud(nx + dx, ny + 1, dx)
        room[nx + dx][ny] = "["
        room[nx + dx][ny + 1] = "]"
        room[nx][ny] = "."
        room[nx][ny + 1] = "."
    else:
        move_ud(nx, ny - 1, dx)
    

def push_ud(dx):
    global x, y
    nx = x + dx
    if can_move(nx, y, dx):
        move_ud(nx, y, dx)
        room[nx][y] = "@"
        room[x][y] = "."
        x = nx

def do_move(move):
    global x, y
    dx, dy = move_map[move]
    nx, ny = x + dx, y + dy
    if room[nx][ny] == "#":
        return
    if room[nx][ny] == ".":
        room[x][y] = "."
        room[nx][ny] = "@"
        x, y = nx, ny
        return
    qx, qy = nx + dx, ny + dy
    if dx == 0:
        push_lr(dy)
    else:
        push_ud(dx)


for move in moves:
    do_move(move)

print_room()

acc = 0

for i in range(len(room)):
    for j in range(len(room[i])):
        if room[i][j] == "[":
            acc += 100 * i + j

print(acc)