from typing import Iterable
from typing import NamedTuple

class Instruction(NamedTuple):
    turn: complex
    steps: int


def instruction(raw: str) -> Instruction:
    turn = {"L": 1j, "R": -1j}
    raw = raw.strip()
    return Instruction(turn[raw[0]], int(raw[1:]))


def move(instructions: Iterable[Instruction], *, start=0+0j, direction=1j, max_step=None):
    yield start
    position = start
    direction = 1j
    for i in instructions:
        direction *= i.turn
        if max_step is None:
            position += direction * i.steps
            yield position
        else:
            steps = i.steps
            while steps:
                step = min(max_step, steps)
                position += direction * step
                yield position
                steps -= step


def part1(instructions: Iterable[Instruction]):
    for position in move(instructions):
        ...
    return abs(int(position.real)) + abs(int(position.imag))


def part2(instructions: Iterable[Instruction]):
    visited = set()
    for position in move(instructions, max_step=1):
        if position in visited:
            return abs(int(position.real)) + abs(int(position.imag))
        visited.add(position)


def main(inputs):
    print("Day 01")
    instructions = list(map(instruction, "".join(inputs).split(",")))
    A = part1(instructions)
    print(f"{A=}")
    B = part2(instructions)
    print(f"{B=}")
