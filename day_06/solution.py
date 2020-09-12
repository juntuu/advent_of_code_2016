from collections import Counter
from collections import defaultdict


def frequency(lines):
    freq = defaultdict(Counter)
    for line in lines:
        for i, c in enumerate(line):
            freq[i][c] += 1
    return freq


def part1(freq):
    i = 0
    corrected = ""
    while i in freq:
        corrected += freq[i].most_common(1)[0][0]
        i += 1
    return corrected


def part2(freq):
    i = 0
    corrected = ""
    while i in freq:
        corrected += freq[i].most_common()[-1][0]
        i += 1
    return corrected


def main(inputs):
    print("Day 06")
    freq = frequency(map(str.strip, inputs))
    A = part1(freq)
    print(f"{A=}")
    B = part2(freq)
    print(f"{B=}")
