def part1(rules):
    start = 0
    for s, e in rules:
        if s > start:
            return start
        start = max(start, e + 1)


def part2(rules):
    available = 0
    start = 0
    for s, e in rules:
        if s > start:
            available += s - start
        start = max(start, e + 1)
    return available + max(2 ** 32 - start, 0)


def main(inputs):
    print("Day 20")
    rules = sorted(tuple(map(int, line.split("-"))) for line in inputs)
    A = part1(rules)
    print(f"{A=}")
    B = part2(rules)
    print(f"{B=}")
