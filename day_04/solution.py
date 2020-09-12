from collections import Counter
from typing import Mapping
from typing import NamedTuple

class Room(NamedTuple):
    name: Mapping[str, int]
    id: int
    check_sum: str

    def real(self):
        c = Counter(self.name.replace("-", ""))
        x = sorted((-b, a) for a, b in c.items())
        return self.check_sum == "".join(a for b, a in x[:5])

    def decrypt(self):
        offset = ord("a")
        table = {i+offset: (i+self.id) % 26 + offset for i in range(26)}
        table[ord("-")] = " "
        return self.name.translate(table)


def room(line):
    line = line.strip()
    name, _, rest = line.rpartition("-")
    id, _, check = rest.partition("[")
    return Room(name, int(id), check.strip("]"))


def part1(rooms):
    return sum(room.id for room in rooms)


def part2(rooms):
    for room in rooms:
        name = room.decrypt()
        if all(word in name for word in ("north", "pole")):
            return room.id


def main(inputs):
    print("Day 04")
    rooms = list(filter(Room.real, map(room, inputs)))
    A = part1(rooms)
    print(f"{A=}")
    B = part2(rooms)
    print(f"{B=}")
