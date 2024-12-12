
stuff = None

with open("input.txt") as in_file:
    stuff = in_file.readline().split()

r_dict = dict()

def compute(v, d, indent):
    if (v, d) in r_dict:
        #print(indent, "mem", v, d, r_dict[(v, d)])
        return r_dict[(v, d)]
    if d == 75:
        #print(indent, v, d, 1, "OnE")
        return 1
    if v == 0:
        r = compute(1, d + 1, indent + "   ")
        #print(indent, v, d, "to 1", r)
        r_dict[(v, d)] = r
        return r
    if len(str(v)) % 2 == 0:
        sv = str(v)
        half = len(sv) // 2
        r = compute(int(sv[:half]), d + 1, indent + "    ")
        r += compute(int(sv[half:]), d + 1, indent + "    ")
        r_dict[(v, d)] = r
        #print(indent, v, d, "split", r)
        return r
    r = compute(v * 2024, d + 1, indent + "    ")
    #print(indent, v, d, "mul", r)
    r_dict[(v, d)] = r
    return r

acc = 0

for v in stuff:
    r = compute(int(v), 0, "")
    #print(v, r)
    acc += r

print(acc)