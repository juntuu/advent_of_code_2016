class Screen:
    def __init__(self, width, height):
        self.pixels = [[0]*width for _ in range(height)]

    """
    rect AxB
    rotate row y=A by B
    rotate column x=A by B
    """

    def rect(self, x, y):
        for row in range(y):
            for col in range(x):
                self.pixels[row][col] = 1

    def rot_row(self, row, n):
        n %= len(self.pixels[0])
        x = self.pixels[row]
        self.pixels[row] = x[-n:] + x[:-n]

    def rot_col(self, col, n):
        n %= len(self.pixels)
        x = [row[col] for row in self.pixels]
        x = iter(x[-n:] + x[:-n])
        for row in self.pixels:
            row[col] = next(x)

    def do(self, what):
        _, key, *rest = what.split()
        if key in "row column":
            a, _, b = rest
            a = int(a.split("=")[-1])
            b = int(b)
            if key == "row":
                self.rot_row(a, b)
            else:
                self.rot_col(a, b)
        else:
            x, y = map(int, key.split("x"))
            self.rect(x, y)

    def __repr__(self):
        lines = []
        for row in self.pixels:
            lines.append("".join(" #"[p] for p in row))
        return "\n".join(lines)


def part1(s):
    return sum(sum(row) for row in s.pixels)


def part2(s):
    # TODO: identify the letters programmatically, or maybe not
    class X:
        def __repr__(self):
            return f"\n{s}"
    return X()


def main(inputs):
    print("Day 08")
    s = Screen(50, 6)
    for line in inputs:
        s.do(line)
    A = part1(s)
    print(f"{A=}")
    B = part2(s)
    print(f"{B=}")
