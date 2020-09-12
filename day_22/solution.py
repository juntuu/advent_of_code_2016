class Node:
    stats = {"min": float("inf"), "g": -1}
    def __init__(self, key, size, used, avail):
        assert size == used + avail
        assert used >= 0
        assert avail >= 0
        assert size >= 0
        self.key = key
        self.size = size
        self.used = used
        self.avail = avail
        self.wall = True

    def __str__(self):
        if self.wall:
            return "#"

        if self.key == self.stats["g"]:
            return "G"
        if self.key == 0+0j:
            return "X"
        return "._"[self.used == 0]


def part1(nodes):
    total = 0
    for n in nodes.values():
        for m in nodes.values():
            if n is not m and 0 < n.used <= m.avail:
                n.wall = m.wall = False
                total += 1
    return total


def print_map(nodes, g, width):
    at = 0+0j
    Node.stats["g"] = g
    while at in nodes:
        row = "".join(str(nodes[at + i]) for i in range(width))
        print(row)
        at += 1j


def part2(nodes, x):
    # TODO: implement the search, with assumptions made from the image
    # 215
    print(x)
    print_map(nodes, x-1+0j, x)
    return 215


def main(inputs):
    print("Day 22")
    next(inputs), next(inputs)
    nodes = {}
    high_x = 0
    for n, s, u, a, _ in map(str.split, inputs):
        n, _, y = n.rpartition("-y")
        _, _, x = n.rpartition("-x")
        x = int(x)
        key = complex(x, int(y))
        high_x = max(high_x, x)
        nodes[key] = Node(key, int(s[:-1]), int(u[:-1]), int(a[:-1]))
    A = part1(nodes)
    print(f"{A=}")
    B = part2(nodes, high_x)
    print(f"{B=}")
