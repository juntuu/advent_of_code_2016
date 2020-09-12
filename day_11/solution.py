"""
The first floor contains a promethium generator and a promethium-compatible microchip.
The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
The fourth floor contains nothing relevant.
"""

from typing import FrozenSet
from typing import NamedTuple
from typing import Tuple

from collections import Counter
from collections import defaultdict
from collections import deque

import heapq

import itertools as it


class Floor(NamedTuple):
    chips: int = 0
    generators: int = 0

    def moves_down(self, to):
        for c in bits(self.chips):
            f = self._replace(chips=self.chips ^ c)
            if b := to.valid(c, 0):
                yield f, b
                break
            if c & self.generators and (b := to.valid(c, c)):
                yield f._replace(generators=f.generators ^ c), b
                break
        else:
            for cs in it.combinations(bits(self.chips), 2):
                cs = OR(cs)
                f = self._replace(chips=self.chips ^ cs)
                if b := to.valid(cs, 0):
                    yield f, b
                    break
        for gs in it.chain(*(it.combinations(bits(self.generators), i) for i in (1, 2))):
            gs = OR(gs)
            f = self._replace(generators=self.generators ^ gs)
            if f.generators and (self.chips & gs):
                continue
            if b := to.valid(0, gs):
                yield f, b
                break

    def moves_up(self, to):
        for cs in it.combinations(bits(self.chips), 2):
            cs = OR(cs)
            f = self._replace(chips=self.chips ^ cs)
            if b := to.valid(cs, 0):
                yield f, b
                break
        for c in bits(self.chips & self.generators):
            f = self._replace(chips=self.chips ^ c, generators=self.generators ^ c)
            if b := to.valid(c, c):
                yield f, b
                break
        else:
            for c in bits(self.chips):
                f = self._replace(chips=self.chips ^ c)
                if b := to.valid(c, 0):
                    yield f, b
                    break
        for gs in it.chain(*(it.combinations(bits(self.generators), i) for i in (2, 1))):
            gs = OR(gs)
            f = self._replace(generators=self.generators ^ gs)
            if f.generators and (self.chips & gs):
                continue
            if b := to.valid(0, gs):
                yield f, b
                break

    def valid(self, chips, gens):
        new_c = self.chips | chips
        new_g = self.generators | gens
        if new_g and (new_c & ~new_g):
            return None
        return (f := Floor(new_c, new_g)) != self and f


def render(b):
    names = sorted(set(x for xs in it.chain(f.chips for f in b.floors) for x in xs))
    n = len(names)
    lines = []
    for i, f in enumerate(b.floors):
        e = ".E"[b.elevator == i]
        items = []
        for name in names:
            if name in f.generators:
                items.append(f"{name}G")
            else:
                items.append(". ")
            if name in f.chips:
                items.append(f"{name}M")
            else:
                items.append(". ")
        lines.append(f"F{i+1} {e}  " + " ".join(items))
    for line in reversed(lines):
        print(line)


class Building(NamedTuple):
    elevator: int
    floors: Tuple[Floor, Floor, Floor, Floor]

    def canonical(self):
        x = it.count(1)
        m = defaultdict(lambda: next(x))
        floors = 0
        for f in self.floors:
            floor = 0
            for i in bits(f.chips):
                floor |= 1 << m[i]
            floor <<= 8
            for i in bits(f.generators):
                floor |= 1 << m[i]
            floors <<= 16
            floors |= floor
        return floors << 2 | self.elevator

    def goal(self):
        chips, gens = 0, 0
        for f in self.floors:
            chips |= f.chips
            gens |= f.generators
        return Building(3, (Floor(), Floor(), Floor(), Floor(chips, gens),))

    def moves(self):
        e = self.elevator
        floors = self.floors
        a = floors[e]
        if e < len(floors) - 1:
            i = e + 1
            for new_a, new_b in a.moves_up(floors[i]):
                new_f = list(floors)
                new_f[e] = new_a
                new_f[i] = new_b
                yield Building(i, tuple(new_f))
        if e == 0 or all(sum(f) == 0 for f in floors[:e]):
            return
        i = e - 1
        for new_a, new_b in a.moves_down(floors[i]):
            new_f = list(floors)
            new_f[e] = new_a
            new_f[i] = new_b
            yield Building(i, tuple(new_f))


def part1(start):
    goal = start.goal().canonical()
    Q = deque([(0, start.canonical(), start)])
    # Q = list(Q)
    C = {start.canonical()}
    pop = deque.popleft
    push = deque.append
    # pop = heapq.heappop
    # push = heapq.heappush
    total = 1
    while Q:
        steps, c, state = pop(Q)
        if c == goal:
            print(f"{total=}")
            return steps
        steps += 1
        for new_state in state.moves():
            if (c := new_state.canonical()) not in C:
                total += 1
                C.add(c)
                push(Q, (steps, c, new_state))


def OR(bs):
    res = 0
    for b in bs:
        res |= b
    return res


def bits(n, C={}):
    if n not in C:
        x = []
        i = 1
        while i <= n:
            if n & i:
                x.append(i)
            i <<= 1
        C[n] = x
    return C[n]


building = Building(0, (
    Floor(1, 1),
    Floor(generators=0b11110),
    Floor(chips=0b11110),
    Floor(),
    ))


def part2(building):
    """
    First floor:
    An elerium generator.
    An elerium-compatible microchip.
    A dilithium generator.
    A dilithium-compatible microchip.
    """
    fs = building.floors
    elems = OR((1 << 6, 1 << 7))
    first = fs[0]._replace(chips=fs[0].chips | elems, generators=fs[0].generators | elems)
    return part1(building._replace(floors=(first, *fs[1:])))


example = Building(0, (
    Floor(chips=0b11),
    Floor(generators=1),
    Floor(generators=2),
    Floor(),
    ))


def test():
    x = part1(example)
    print(f"{x=}")
    assert x == 11

if __name__ == "__main__":
    test()


def main(inputs=None):
    print("Day 11")
    test()
    A = part1(building)
    print(f"{A=}")
    assert A == 33
    B = part2(building)
    print(f"{B=}")
    assert B == 57
