def decompress_len_v2(data, start=0, end=None, *, v1=False):
    if v1:
        repeat = lambda _, a: a
    else:
        repeat = lambda i, a: decompress_len_v2(data, i, i+a)
    if end is None:
        end = len(data)
    total = 0
    i = start
    while (j := data.find("(", i, end)) != -1:
        total += j - i
        i = data.index(")", j, end)
        a, b = map(int, data[j+1:i].split("x"))
        total += repeat(i+1, a) * b
        i += 1 + a
    return total + end - i


def part1(data):
    return decompress_len_v2(data, v1=True)


def part2(data):
    return decompress_len_v2(data)


def main(inputs):
    print("Day 09")
    data = "".join(map(str.strip, inputs))
    A = part1(data)
    print(f"{A=}")
    assert A == 107035
    B = part2(data)
    print(f"{B=}")
    assert B == 11451628995
