from collections import deque
from hashlib import md5


def doors(path, options):
    h = md5(path.encode()).hexdigest()
    for k, v in zip(h, "UDLR"):
        if k > "a" and v in options:
            yield v


def paths(key, maze, move):
    Q = deque([(0, 0, "")])
    while Q:
        i, j, path = Q.popleft()
        for door in doors(key + path, maze[i][j]):
            x, y = move[door]
            if i + x == j + y == 3:
                yield path + door
            else:
                Q.append((i + x, j + y, path + door))


def part1(key, maze, move):
    return next(paths(key, maze, move))


def part2(key, maze, move):
    return max(map(len, paths(key, maze, move)))


def main():
    print("Day 17")
    key = "pvhmgsws"

    maze = [
        ["DR", "DLR", "DLR", "DL"],
        ["DUR", "UDLR", "UDLR", "DUL"],
        ["DUR", "UDLR", "UDLR", "DUL"],
        ["UR", "ULR", "ULR", "UL"],
    ]

    move = {
        "D": (1, 0),
        "U": (-1, 0),
        "R": (0, 1),
        "L": (0, -1),
    }

    A = part1(key, maze, move)
    print(f"{A=}")
    B = part2(key, maze, move)
    print(f"{B=}")
