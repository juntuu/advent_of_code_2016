def name(f):
    return f
    def wrap(*a, **kw):
        res = f(*a, **kw)
        res.name = f.__qualname__ + "(" + ", ".join(map(repr, a)) + ")"
        return res
    return wrap


def ident(xs, **_):
    return xs


@name
def rotate(steps, direction="right"):
    if steps == 0:
        return ident
    d = 1 if direction == "left" else -1
    def do(xs, *, reverse=False):
        n = d * steps % len(xs)
        if reverse:
            n *= -1
        return xs[n:] + xs[:n]
    return do

@name
def rotate_char(c):
    def do(xs, *, reverse=False):
        i = xs.index(c)
        if reverse:
            x = xs[:]
            for j in range(len(xs)):
                x = rotate(1, "left")(x)
                if rotate_char(c)(x[:]) == xs:
                    return x
        return rotate(i + 1 + (i >= 4))(xs)
    return do


@name
def reverse(a, b):
    if a == b:
        return ident
    if b < a:
        a, b = b, a
    def do(xs, *, reverse=False):
        return xs[:a] + xs[a:b+1][::-1] + xs[b+1:]
    return do


@name
def move(a, b):
    if a == b:
        return ident
    def do(xs, *, reverse=False):
        if reverse:
            xs.insert(a, xs.pop(b))
        else:
            xs.insert(b, xs.pop(a))
        return xs
    return do


@name
def swap(a, b):
    if a == b:
        return ident
    def do(xs, *, reverse=False):
        xs[a], xs[b] = xs[b], xs[a]
        return xs
    return do


@name
def swap_char(a, b):
    if a == b:
        return ident
    def do(xs, *, reverse=False):
        return swap(xs.index(a), xs.index(b))(xs)
    return do


def parse(line):
    parts = line.split()
    if parts[0] == "swap":
        _, t, x, _, _, y = parts
        if t == "position":
            return swap(int(x), int(y))
        elif t == "letter":
            return swap_char(x, y)
    elif parts[0] == "move":
        _, _, x, _, _, y = parts
        return move(int(x), int(y))
    elif parts[0] == "reverse":
        _, _, x, _, y = parts
        return reverse(int(x), int(y))
    elif parts[0] == "rotate":
        if parts[1] == "based":
            return rotate_char(parts[-1])
        else:
            _, d, x, _ = parts
            return rotate(int(x), d)


def part1(pw, ops):
    for op in ops:
        pw = op(pw)
    return "".join(pw)


def part2(pw, ops):
    for op in reversed(ops):
        pw = op(pw, reverse=True)
    return "".join(pw)


def main(inputs):
    print("Day 21")
    ops = list(map(parse, inputs))
    A = part1(list("abcdefgh"), ops)
    print(f"{A=}")
    B = part2(list("fbgdceah"), ops)
    print(f"{B=}")
