
from collections import deque

ab = None
bb = None

instances = []

with open("input.txt") as in_file:
    for line in in_file:
        if line.startswith("Button A"):
            ls = line.split()
            yv = int(ls[-1].split("+")[-1])
            xv = int(ls[-2].strip(",").split("+")[-1])
            ab = (xv, yv)
        elif line.startswith("Button B"):
            ls = line.split()
            yv = int(ls[-1].split("+")[-1])
            xv = int(ls[-2].strip(",").split("+")[-1])
            bb = (xv, yv)
        elif line.startswith("Prize:"):
            ls = line.split()
            yv = int(ls[-1].split("=")[-1])
            xv = int(ls[-2].strip(",").split("=")[-1])
            instances.append((ab, bb, (xv + 10000000000000, yv + 10000000000000)))

def solve(ab, bb, p):
    ax, ay = ab
    bx, by = bb
    px, py = p
    det = ax * by - ay * bx
    a = px * by - py * bx % det
    b = py * ax - px * ay % det
    if a > 0 or b > 0:
        return 0
    return 3 * (px * by - py * bx) / det + (py * ax - px * ay) / det

res = 0
for ab, bb, p in instances:
    #print(ab, bb, p)
    res += solve(ab, bb, p)

print(res)