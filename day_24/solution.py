import heapq
from collections import defaultdict
from functools import lru_cache


class Node:
    def __init__(self, val):
        self.val = val
        self.con = {}

    def __lt__(self, other):
        return id(self) < id(other)

    def __iter__(self):
        return iter(self.con.items())

    def __repr__(self):
        return str(self.val)

    def simplify(self):
        if self.val != ".":
            return
        if len(self.con) == 1:
            x, = self.con
            self.con.clear()
            self.val = " "
            x.con.pop(self, None)
            x.simplify()
        elif len(self.con) == 2:
            (a, x), (b, y) = self.con.items()
            self.con.clear()
            self.val = " "
            a.con.pop(self, None)
            b.con.pop(self, None)
            a.con[b] = x + y
            b.con[a] = x + y
            a.simplify()


def parse(lines):
    nodes = []
    prev = []
    nums = set()
    zero = None
    for line in lines:
        r = []
        for c in line.strip():
            if c == "#":
                r.append(c)
                continue
            n = Node(c)
            nodes.append(n)
            if c == "0":
                zero = n
            nums.add(c)
            up = prev[len(r)]
            left = r[-1]
            for x in (up, left):
                if x != "#":
                    n.con[x] = 1
                    x.con[n] = 1
            r.append(n)
        prev = r
    nums.discard(".")
    for node in nodes:
        node.simplify()
    return zero, nums


@lru_cache(None)
def find(start, goal):
    Q = [(0, start)]
    D = defaultdict(lambda big=float("inf"): big)
    D[start] = 0
    pop = heapq.heappop
    push = heapq.heappush
    while Q:
        steps, node = pop(Q)
        if node.val == goal:
            return steps, node
        for con, cost in node:
            if steps + cost < D[con]:
                D[con] = steps + cost
                push(Q, (steps + cost, con))


def part1(start, goal):
    Q = [(0, len(goal), goal - {start.val}, start)]
    pop = heapq.heappop
    push = heapq.heappush
    while Q:
        steps, x, rem, node = pop(Q)
        if not rem:
            return steps
        for r in rem:
            cost, con = find(node, r)
            push(Q, (steps + cost, x - 1, rem - {r}, con))


def part2(start, goal):
    Q = [(0, len(goal), goal - {start.val}, start)]
    pop = heapq.heappop
    push = heapq.heappush
    while Q:
        steps, x, rem, node = pop(Q)
        if not rem:
            return steps
        for r in rem:
            cost, con = find(node, r)
            if len(rem) == 1:
                y, _ = find(con, start.val)
                cost += y
            push(Q, (steps + cost, x - 1, rem - {r}, con))


def main(inputs):
    print("Day 24")
    zero, nums = parse(inputs)
    A = part1(zero, nums)
    print(f"{A=}")
    assert A == 490
    B = part2(zero, nums)
    print(f"{B=}")
    assert B == 744
