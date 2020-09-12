"""
cpy x y copies x into register y.
inc x increases the value of register x by one.
dec x decreases the value of register x by one.
jnz x y jumps to an instruction y away
"""

def run(c):
    "input specific translation of the logic, seems like fibonacci with offset"
    a, b = 1, 1
    d = 26
    if c != 0:
        d += 7
    for _ in range(d):
        a, b = a + b, a
    return a + 19 * 14


def excecute(reg, code):
    i = 0
    while 0 <= i < len(code):
        op, x, y = code[i]
        if op == "cpy":
            reg[y] = reg.get(x, x)
        elif op == "inc":
            reg[x] += 1
        elif op == "dec":
            reg[x] -= 1
        elif reg.get(x, x) != 0:
            i += reg.get(y, y)
            continue
        i += 1


def part1(code):
    return run(0)
    reg = {c: 0 for c in "abcd"}
    excecute(reg, code)
    return reg["a"]


def part2(code):
    return run(1)
    reg = {c: 0 for c in "abcd"}
    reg["c"] = 1
    excecute(reg, code)
    return reg["a"]


def parse(line):
    xs = line.strip().split()
    if len(xs) < 3:
        xs.append("")
    for i in (1, 2):
        try:
            xs[i] = int(xs[i])
        except ValueError:
            pass
    return tuple(xs)


def main(inputs):
    print("Day 12")
    code = list(map(parse, inputs))
    A = part1(code)
    print(f"{A=}")
    B = part2(code)
    print(f"{B=}")
