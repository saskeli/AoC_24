
acc = 0
with open("input.txt") as in_file:
    for line in in_file.readlines():
        vals = [
            int(v) for 
            v in line.split(" ")
        ]
        if len(vals) == 1:
            acc += 1
        elif len(vals) > 1:
            if vals[0] > vals[1]:
                safe = True
                for i in range(1, len(vals)):
                    if not (0 < vals[i - 1] - vals[i] <= 3):
                        safe = False
                        break
                if safe:
                    acc += 1
            elif vals[1] > vals[0]:
                safe = True
                for i in range(1, len(vals)):
                    if not (0 < vals[i] - vals[i - 1] <= 3):
                        safe = False
                        break
                if safe:
                    acc += 1
print(acc)