from collections import deque


def neighbours(pos):
    x, y = pos
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def part1(space):
    goal = 31, 39
    Q = deque([(0, (1, 1))])
    visited = {(1, 1)}
    while Q:
        steps, pos = Q.popleft()
        for x in filter(space, neighbours(pos)):
            if x == goal:
                return steps + 1
            if x not in visited:
                Q.append((steps + 1, x))
                visited.add(x)


def part2(space):
    Q = deque([(0, (1, 1))])
    visited = {(1, 1)}
    while Q:
        steps, pos = Q.popleft()
        if steps >= 50:
            continue
        for x in filter(space, neighbours(pos)):
            if x not in visited:
                Q.append((steps + 1, x))
                visited.add(x)
    return len(visited)


def main(_=None):
    print("Day 13")
    number = 1362

    def space(pos):
        x, y = pos
        if x < 0 or y < 0:
            return False
        n = x*x + 3*x + 2*x*y + y + y*y + number
        return bin(n).count("1") % 2 == 0

    A = part1(space)
    print(f"{A=}")
    B = part2(space)
    print(f"{B=}")
