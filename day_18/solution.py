def trap(i, prev):
    if i == 0:
        return prev[1]
    elif i == len(prev) - 1:
        return prev[-2]
    return prev[i-1] ^ prev[i+1]


def part1(line, n=40):
    traps = sum(line)
    r = range(len(line))
    for i in range(n-1):
        line = [trap(i, line) for i in r]
        traps += sum(line)
    return n * len(line) - traps

def part2(line):
    return part1(line, 400000)

def main(inputs):
    print("Day 18")
    line = [c == "^" for c in "".join(inputs).strip()]
    A = part1(line)
    print(f"{A=}")
    assert A == 1963
    B = part2(line)
    print(f"{B=}")
    assert B == 20009568
