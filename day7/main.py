from collections import defaultdict
from typing import Callable
from functools import cmp_to_key


data = []

with open("input.txt") as f:
    for line in f.readlines():
        res, operands = line.strip().split(": ")
        data.append((int(res), [int(o) for o in operands.split(" ")]))


def find_configuration(
    operands: list[int], operators: dict[str, Callable[[int, int], int]]
):
    paths = {op: action(operands[0], operands[1]) for op, action in operators.items()}

    if len(operands) == 2:
        return paths

    for o in operands[2:]:
        new_paths = {}
        for s, p in paths.items():
            for op, action in operators.items():
                new_paths[s + op] = action(p, o)

        paths = new_paths

    return paths


def run(operators: dict[str, Callable[[int, int], int]]) -> int:
    sum = 0

    for res, operands in data:
        paths = find_configuration(operands, operators)
        if res in paths.values():
            sum += res

    return sum


def day1():
    operators = {
        "*": lambda a, b: a * b,
        "+": lambda a, b: a + b,
    }

    return run(operators)


def day2():
    operators = {
        "*": lambda a, b: a * b,
        "+": lambda a, b: a + b,
        "||": lambda a, b: int(str(a) + str(b)),
    }

    return run(operators)


print(day1())
print(day2())
