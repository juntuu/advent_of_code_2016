def valid(triangle):
    big = max(triangle)
    return big < sum(triangle) - big


def part1(triangles):
    return sum(map(valid, triangles))


def group(n, it):
    return zip(*[iter(it)]*n)


def transpose(it):
    return zip(*it)


def part2(triangles):
    triangles = group(3, triangles)
    triangles = (t for group in triangles for t in transpose(group))
    return sum(map(valid, triangles))


def main(inputs):
    print("Day 03")
    triangles = [tuple(map(int, line.split())) for line in inputs]
    A = part1(triangles)
    print(f"{A=}")
    B = part2(triangles)
    print(f"{B=}")
