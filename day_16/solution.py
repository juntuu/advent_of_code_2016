def double(a):
    b = a[::-1]
    return a + "0" + b.translate({ord("1"): "0", ord("0"): "1"})


def check_sum(s):
    while len(s) % 2 == 0:
        s = "".join("01"[a == b] for a, b in zip(*[iter(s)]*2))
    return s


def part1(state):
    n = 272
    while len(state) < n:
        state = double(state)
    return check_sum(state[:n])


def part2(state):
    n = 35651584
    while len(state) < n:
        state = double(state)
    return check_sum(state[:n])


def main(_=None):
    print("Day 16")
    state = "01111010110010011"
    A = part1(state)
    print(f"{A=}")
    B = part2(state)
    print(f"{B=}")
