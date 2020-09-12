"""
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""

import itertools


def parse(line):
    parts = line.split()
    if parts[0] == "value":
        _, a, *_, b = parts
        return int(a), int(b)
    else:
        _, n, _, _, _, a, x, _, _, _, b, y = parts
        return int(n), (a[:3], int(x)), (b[:3], int(y))


class key_dict(dict):
    def __init__(self, factory):
        self.defaulfactory = factory

    def __missing__(self, key):
        self[key] = self.defaulfactory(key)
        return self[key]


class Bot:
    def __init__(self, number):
        self.id = number
        self.chips = []

    def add(self, chip):
        self.chips.append(chip)

    def give(self, out, lo, hi):
        if len(self.chips) != 2:
            return
        a, b = self.deal()
        la, lb = lo
        out[la][lb].add(a)
        ha, hb = hi
        out[ha][hb].add(b)

    def deal(self):
        a, b = sorted(self.chips)
        self.chips = []
        return a, b


def picky_bot(a, b):
    class Picky(Bot):
        def deal(self):
            x = super().deal()
            if x == (a, b):
                raise StopIteration(self.id)
            return x
    return Picky


def run(instructions, **res):
    try:
        for i in instructions:
            if len(i) == 3:
                b, lo, hi = i
                res["bot"][b].give(res, lo, hi)
            else:
                v, b = i
                res["bot"][b].add(v)
        for i in itertools.cycle(filter(lambda i: len(i) == 3, instructions)):
            b, lo, hi = i
            res["bot"][b].give(res, lo, hi)
    except StopIteration as e:
        return e.value


class Void:
    def __getitem__(self, _):
        return self

    def add(self, _):
        ...


def part1(instructions):
    return run(instructions, bot=key_dict(picky_bot(17, 61)), out=Void())


def picky_dict(vals):
    D = {}
    class Picky:
        def __getitem__(self, key):
            if key not in vals:
                return set()
            class S:
                def add(self, val):
                    vals.discard(key)
                    D[key] = val
                    if not vals:
                        raise StopIteration(D)
            return S()
    return Picky()


def part2(instructions):
    res = run(instructions, bot=key_dict(Bot), out=picky_dict({0, 1, 2}))
    p = 1
    for v in res.values():
        p *= v
    return p


def main(inputs):
    print("Day 10")
    instructions = list(map(parse, inputs))
    A = part1(instructions)
    print(f"{A=}")
    B = part2(instructions)
    print(f"{B=}")
