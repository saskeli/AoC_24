bots = []

with open("input.txt") as in_file:
    for line in in_file:
        ss = line.split()
        p, v = ss[0], ss[1]
        bots.append((tuple(int(vv) for vv in p[2:].split(",")), tuple(int(vv) for vv in v[2:].split(","))))

width = 101
height = 103

ul = 0
ur = 0
ll = 0
lr = 0

for (px, py), (vx, vy) in bots:
    x = (px + vx * 100) % width
    y = (py + vy * 100) % height
    if x < width // 2:
        if y < height // 2:
            ul += 1
        elif y > height // 2:
            ll += 1
    elif x > width // 2:
        if y < height // 2:
            ur += 1
        elif y > height // 2:
            lr += 1

print(ul * ur * ll * lr)