room = []

moves = []

x = 0
y = 0

with open("input.txt") as in_file:
    make_room = True
    cx = 0
    for line in in_file:
        l = line.strip()
        if len(l) == 0:
            make_room = False
        elif make_room:
            l = list(l)
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
    while room[qx][qy] == "O":
        qx, qy = qx + dx, qy + dy
    if room[qx][qy] == "#":
        return
    room[qx][qy] = "O"
    room[x][y] = "."
    room[nx][ny] = "@"
    x, y = nx, ny


for move in moves:
    do_move(move)

print_room()

acc = 0

for i in range(len(room)):
    for j in range(len(room[i])):
        if room[i][j] == "O":
            acc += 100 * i + j

print(acc)