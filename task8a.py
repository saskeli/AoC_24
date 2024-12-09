from collections import defaultdict

antennas = defaultdict(list)

x = 0
y = 0

with open("input.txt") as in_file:
    x = 0
    for line in in_file:
        y = 0
        for c in line.strip():
            if c != ".":
                antennas[c].append((x, y))
            y += 1
        x += 1

print(x, y)

#print(antennas)

antinodes = set()
for v in antennas.values():
    antinodes.update(v)

def in_grid(i, j):
    return 0 <= i < x and 0 <= j < y

for k, v in antennas.items():
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            dx = v[i][0] - v[j][0]
            dy = v[i][1] - v[j][1]
            #print(k, v[i], v[j])
            #print(" -> ", v[i][0] + dx, v[i][1] + dy)
            #print(" -> ", v[j][0] - dx, v[j][1] - dy)
            ai, aj = v[i][0] + dx, v[i][1] + dy
            while in_grid(ai, aj):
                antinodes.add((ai, aj))
                ai, aj = ai + dx, aj + dy
                
            ai, aj = v[j][0] - dx, v[j][1] - dy
            while in_grid(ai, aj):
                antinodes.add((ai, aj))
                ai, aj = ai - dx, aj - dy

print(len(antinodes))
