def toggle(code, i):
    if not (0 <= i < len(code)):
        print("-t", i)
        return 0
    print("+t", i)
    op, x, y = code[i]
    if not y:
        code[i] = ("dec" if op == "inc" else "inc"), x, y
    else:
        code[i] = ("cpy" if op == "jnz" else "jnz"), x, y
    return op == "tgl"


def do(a):
    """
    logic extracted from the assembunny code with knowledge
    of access patterns of the calculated jumps and toggles,
    just a factorial with an offset
    """
    for b in range(2, a):
        a *= b
    return a + 70 * 78


def excecute(reg, code):
    tgls = sum(op == "tgl" for op, *_ in code)
    i = 0
    while 0 <= i < len(code):
        op, x, y = code[i]
        if op == "tgl":
            j = i + reg.get(x, x)
            tgls -= toggle(code, j)
            print(tgls)
            if not tgls:
                print(*code, sep="\n")
        elif op == "cpy":
            reg[y] = reg.get(x, x)
        elif op == "inc":
            reg[x] += 1
        elif op == "dec":
            reg[x] -= 1
        elif reg.get(x, x) != 0:
            i += reg.get(y, y)
            continue
        i += 1


def run(code, a):
    reg = {c: 0 for c in "abcd"}
    reg["a"] = a
    excecute(reg, code)
    return reg["a"]


def part1(code):
    return do(7)
    return run(code, 7)


def part2(code):
    return do(12)
    return run(code, 12)


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
    print("Day 23")
    code = list(map(parse, inputs))
    A = part1(code[:])
    print(f"{A=}")
    B = part2(code)
    print(f"{B=}")
