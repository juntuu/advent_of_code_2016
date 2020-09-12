class List:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def part1(n):
    return 2 * int(bin(n)[3:], 2) + 1


def p2(n):
    p = 1
    while 3 * p <= n:
        p *= 3
    if n == p:
        return n
    return n - p + max(n - 2 * p, 0)


def part2(n):
    return p2(n)
    x = List(n)
    p = x
    for i in range(1, n):
        p.next = List(i)
        p = p.next
        if i == n // 2:
            v = p
    p.next = x
    x = x.next
    assert x.val == 1

    while x is not x.next:
        v.next = v.next.next
        n -= 1
        if n % 2 == 0:
            v = v.next
        x = x.next
    return x.val


def main(_=None):
    print("Day 19")
    elves = 3017957
    A = part1(elves)
    print(f"{A=}")
    assert A == 1841611
    B = part2(elves)
    print(f"{B=}")
    assert B == 1423634
