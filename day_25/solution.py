def part1(code):
    i = 0;
    while i < 7 * 365:
        i = i << 2 | 0b10;
    return i - 7 * 365


def part2(code):
    ...


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
    A = part1(code)
    print(f"{A=}")
    B = part2(code)
    print(f"{B=}")
