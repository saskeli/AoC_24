from queue import PriorityQueue

w_map = ([], [], [], [])

v_map = {
    "#": -1,
    ".": -2,
    "S": -2,
    "E": -2
}

start_x = 0
start_y = 0

goal_x = 0
goal_y = 0

with open("input.txt") as in_file:
    i = 0
    for line in in_file:
        line = line.strip()
        layer = []
        for j, c in enumerate(line):
            if c == "S":
                start_x = i
                start_y = j
            if c == "E":
                goal_x = i
                goal_y = j
            layer.append(v_map[c])
        for layer_n in range(len(w_map)):
            w_map[layer_n].append([v for v in layer])
        i += 1

w_map[0][start_x][start_y] = 0

def print_map():
    for i, d in enumerate(["East", "South", "West", "North"]):
        print(d)
        print("\n".join("".join(f"{1 if ll >= 0 else 0}" for ll in l) for l in w_map[i]))

turn_map = {
    0: (1, 3),
    1: (0, 2),
    2: (1, 3),
    3: (0, 2)
}

d_map = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0)
}

q = PriorityQueue()
q.put((0, 0, start_x, start_y))

while q.qsize() > 0:
    dist, layer, x, y = q.get()
    if x == goal_x and y == goal_y:
        print_map()
        print(dist)
        break
    if w_map[layer][x][y] < dist:
        continue
    dx, dy = d_map[layer]
    nx, ny = x + dx, y + dy
    val = w_map[layer][nx][ny]
    if val == -2 or val > dist + 1:
        w_map[layer][nx][ny] = dist + 1
        q.put((dist + 1, layer, nx, ny))
    for nl in turn_map[layer]:
        val = w_map[nl][x][y]
        if val == -2 or val > dist + 1000:
            w_map[nl][x][y] = dist + 1000
            q.put((dist + 1000, nl, x, y))
