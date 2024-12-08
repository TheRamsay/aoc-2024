from collections import defaultdict
import math
from typing import Callable
from functools import cmp_to_key

grid = []

antenas = defaultdict(list)

with open("test.txt") as f:
    for line in f.readlines():
        row = []
        for cell in list(line.strip()):
            row.append(cell)

        grid.append(row)

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != ".":
            antenas[cell].append((x, y))


def find_antinodes(vec_scale_min: int, vec_scale_max: int):
    antinodes = set()

    for antena_name, positions in antenas.items():
        for i, (x1, y1) in enumerate(positions):
            for j, (x2, y2) in enumerate(positions[i + 1 :]):
                dx = x2 - x1
                dy = y2 - y1

                for i in range(vec_scale_min, vec_scale_max):
                    scaled_dx = dx * i
                    scaled_dy = dy * i

                    an1 = (x1 + scaled_dx, y1 + scaled_dy)
                    an2 = (x2 - scaled_dx, y2 - scaled_dy)

                    if (
                        an1[0] >= 0
                        and an1[0] < len(grid[0])
                        and an1[1] < len(grid)
                        and an1[1] >= 0
                    ):
                        antinodes.add(an1)

                    if (
                        an2[0] >= 0
                        and an2[0] < len(grid[0])
                        and an2[1] < len(grid)
                        and an2[1] >= 0
                    ):
                        antinodes.add(an2)

    return antinodes


def day1():
    return len(find_antinodes(2, 3))


def day2():
    # Random max scale just because it works 👺👺
    return len(find_antinodes(0, 100))


print(day1())
print(day2())
