
def inc_skip(vals, loc):
    if loc != 0 and loc != len(vals) - 1:
        if not (0 < vals[loc - 1] - vals[loc + 1] <= 3):
            return False
    for i in range(loc + 2, len(vals)):
        if not (0 < vals[i - 1] - vals[i] <= 3):
            return False
    return True

def inc(vals):
    for i in range(1, len(vals)):
        if not (0 < vals[i - 1] - vals[i] <= 3):
            return inc_skip(vals, i - 1) or inc_skip(vals, i)
    return True

def dec_skip(vals, loc):
    if loc != 0 and loc != len(vals) - 1:
        if not (0 < vals[loc + 1] - vals[loc - 1] <= 3):
            return False
    for i in range(loc + 2, len(vals)):
        if not (0 < vals[i] - vals[i - 1] <= 3):
            return False
    return True

def dec(vals):
    for i in range(1, len(vals)):
        if not (0 < vals[i] - vals[i - 1] <= 3):
            return dec_skip(vals, i - 1) or dec_skip(vals, i)
    return True

acc = 0
with open("input.txt") as in_file:
    for line in in_file.readlines():
        vals = [
            int(v) for 
            v in line.split(" ")
        ]
        if len(vals) == 1:
            acc += 1
        elif inc(vals) or dec(vals):
            #print(vals, "is safe")
            #input()
            acc += 1
        #else:
        #    print(vals, "is unsafe")
        #    input()
print(acc)