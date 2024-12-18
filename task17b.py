
a = 0
b = 0
c = 0
prog = None

with open("input.txt") as in_file:
    a = int(in_file.readline().split()[-1])
    b = int(in_file.readline().split()[-1])
    c = int(in_file.readline().split()[-1])
    _ = in_file.readline()
    prog = [int(v) for v in in_file.readline().split()[-1].split(",")]

print(a, b, c)
print(prog)

pq = []

pc = 0

def combo(ope):
    if ope == 7:
        raise Exception("invalid combo operand")
    if ope == 4:
        return a
    if ope == 5:
        return b
    if ope == 6:
        return c
    return ope

def adv(ope):
    global a
    ope = combo(ope)
    a = a // 2**ope

def bxl(ope):
    global b
    b ^= ope

def bst(ope):
    global b
    ope = combo(ope)
    b = ope & 7

def jnz(ope):
    global a, pc
    pc = pc if a == 0 else ope

def bxc(ope):
    global b, c
    b ^= c

def out(ope):
    ope = combo(ope)
    pq.append(ope & 7)

def bdv(ope):
    global a, b
    ope = combo(ope)
    b = a // 2**ope

def cdv(ope):
    global a, c
    ope = combo(ope)
    c = a // 2**ope

op_map = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

vals = [0] * 16

def run(i):
    states = set()
    global a, b, c, pc
    a = i
    pc = 0
    pq.clear()
    while pc < len(prog):
        states.add((a, b, c, pc))
        op = prog[pc]
        ope = prog[pc + 1]
        pc += 2
        op_map[op](ope)

def rec(digit):
    for i in range(8):
        vals[digit] = i
        val = 0
        for v in vals:
            val *= 8
            val += v
        run(val)
        print(f"{val}, {digit}:")
        print(prog)
        print(pq)
        if len(pq) == len(prog) and all(a == b for a, b in zip(pq, prog)):
            exit(0)

        ok = True
        for i in range(len(prog) - 1 - digit, len(prog)):
            if len(pq) <= i or pq[i] != prog[i]:
                ok = False
        if ok:
            rec(digit + 1)

rec(0)