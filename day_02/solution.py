"""
1 2 3
4 5 6
7 8 9

Suppose your instructions are:

    ULL
    RRDDD
    LURDL
    UUUUD
"""

KEYPAD_A = {
    -1 +  1j: 1, 0 +  1j: 2, 1 +  1j: 3,
    -1 +  0j: 4, 0 +  0j: 5, 1 +  0j: 6,
    -1 + -1j: 7, 0 + -1j: 8, 1 + -1j: 9,
}

KEYPAD_B = {
                          2 + 2j: 1,
               1 + 1j: 2, 2 + 1j: 3, 3 + 1j: 4,
    0 + 0j: 5, 1 + 0j: 6, 2 + 0j: 7, 3 + 0j: 8, 4 + 0j: 9,
               1 + -1j: "A", 2 + -1j: "B", 3 + -1j: "C",
                          2 + -2j: "D",
}

"""
    1
  2 3 4
5 6 7 8 9
  A B C
    D
"""

DIRECTION = {
    "U":  0 +  1j,
    "D":  0 + -1j,
    "L": -1 +  0j,
    "R":  1 +  0j,
}


def decode(key, keypad, directions):
    for d in directions:
        step = DIRECTION[d]
        if key + step in keypad:
            key += step
    return key


def key(lines, keypad):
    key = 0 + 0j
    keys = []
    for line in lines:
        key = decode(key, keypad, line)
        keys.append(keypad[key])
    return "".join(map(str, keys))


def part1(lines):
    return key(lines, KEYPAD_A)


def part2(lines):
    return key(lines, KEYPAD_B)


def main(inputs):
    print("Day 02")
    lines = list(map(str.strip, inputs))
    A = part1(lines)
    print(f"{A=}")
    B = part2(lines)
    print(f"{B=}")
