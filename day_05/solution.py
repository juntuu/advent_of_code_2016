import hashlib
from itertools import count


def md5(string):
    return hashlib.md5(string.encode()).hexdigest()


class Hasher:
    def __init__(self, key):
        self.key = key
        ok = lambda s: s.startswith("00000")
        self.hashes = filter(ok, (md5(key + str(i)) for i in count()))
        self.cache = []

    def __iter__(self):
        def do():
            yield from self.cache
            for h in self.hashes:
                self.cache.append(h)
                yield h

        return do()


def part1(hashes):
    password = ""
    print("_"*8, end="\r")
    for _ in range(8):
        password += next(hashes)[5]
        print(password[-1], end="", flush=True)
    print()
    return password


def part2(hashes):
    password = ["_"] * 8
    print("".join(password), end="\r", flush=True)
    for h in hashes:
        i = "01234567".find(h[5])
        if i != -1 and password[i] == "_":
            password[i] = h[6]
            print("".join(password), end="\r", flush=True)
            if "_" not in password:
                break
    print()
    return "".join(password)


def main():
    key = "cxdnnyjw"
    hasher = Hasher(key)
    A = part1(iter(hasher))
    print(f"{A=}")
    B = part2(iter(hasher))
    print(f"{B=}")
