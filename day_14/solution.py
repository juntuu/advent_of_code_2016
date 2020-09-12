import re
from itertools import count
from hashlib import md5


def triple(s, r=re.compile(r"(.)\1{2}")):
    m = r.search(s)
    return m and m.group(1)


def fives(s, r=re.compile(r"(.)\1{4}")):
    return r.findall(s)


def base_hash(key):
    return lambda i: md5((key + str(i)).encode()).hexdigest()


def stretch_hash(key, window, times):
    cache = {}
    base = base_hash(key)

    def hash(i):
        if i not in cache:
            s = base(i)
            for _ in range(times):
                s = md5(s.encode()).hexdigest()
            cache[i] = s
        if i > window:
            cache.pop(i - window, None)
        return cache[i]

    return hash


def solve(hash_fn, window):
    horizon = {k: -1 for k in "0123456789abcdef"}

    def update_horizon(i):
        for c in fives(hash_fn(i)):
            horizon[c] = i

    for i in range(1, window+1):
        update_horizon(i)

    keys = 0
    for i in count():
        h = hash_fn(i)
        if (t := triple(h)) and horizon[t] > i:
            print(t, end="", flush=True)
            keys += 1
            if keys == 64:
                print()
                return i
        update_horizon(i + window)


def part1(key):
    return solve(base_hash(key), 1000)


def part2(key):
    return solve(stretch_hash(key, 1000, 2016), 1000)


def main(_=None):
    key = "qzyelonm"
    # key = "abc"
    A = part1(key)
    print(f"{A=}")
    assert A == 15168
    B = part2(key)
    print(f"{B=}")
    assert B == 20864
