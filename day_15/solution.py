import math


def parse(line):
    parts = line.split()
    return int(parts[3]), int(parts[-1].strip(".\n"))


def lcm(a, b):
    c = math.gcd(a, b)
    return a * b // c


def passes(t, d):
    n, s = d
    return (s + t) % n == 0


def part1(discs):
    x = 1
    t = 0
    for i, d in enumerate(discs, 1):
        while not passes(t + i, d):
            t += x
        x = lcm(x, d[0])
    return t


def part2(discs, begin):
    x = 1
    for n, _ in discs:
        x = lcm(x, n)
    t = begin
    while not passes(t + len(discs) + 1, (11, 0)):
        t += x
    return t


def main(inputs):
    print("Day 15")
    discs = list(map(parse, inputs))
    A = part1(discs)
    print(f"{A=}")
    assert A == 376777
    B = part2(discs, A)
    print(f"{B=}")
    assert B == 3903937
