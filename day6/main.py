from collections import defaultdict
from functools import cmp_to_key


heh = {"^": 0, ">": 1, "v": 2, "<": 3}
hah = ["^", ">", "v", "<"]

dirs = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}

grid = []
start_x, start_y = -1, -1

with open("input.txt") as f:
    for y, line in enumerate(f.readlines()):
        line = line.strip()
        brr = []
        for x, char in enumerate(line):
            if char in hah:
                bx, by = (x, y)
            brr.append(char)

        grid.append(brr)

# assert start_x != -1 and start_y != -1, "KEWJKEFJWEKFK"


ss = grid[by][bx]


def check_ahead(x: int, y: int, grid: list[list[int]], symbol: str, d: int):
    if d >= 4:
        raise Exception("XD")

    dx, dy = dirs[symbol]
    if grid[y + dy][x + dx] != "#":
        return symbol, dx, dy

    while True:
        symbol = hah[(heh[symbol] + 1) % 4]
        return check_ahead(x, y, grid, symbol, d + 1)


def get_path(start_x, start_y):
    prev_cur = set()
    running = True
    path = [(start_x, start_y)]

    while running:
        symbol = grid[start_y][start_x]
        dx, dy = dirs[symbol]
        prev = start_x, start_y

        if grid[start_y + dy][start_x + dx] != "#":
            grid[start_y][start_x] = "."
            start_x += dx
            start_y += dy
        else:
            try:
                symbol, dx, dy = check_ahead(start_x, start_y, grid, symbol, 0)
            except Exception:
                print("WATAFAK")
                break

            grid[start_y][start_x] = "."
            start_x += dx
            start_y += dy

        grid[start_y][start_x] = symbol

        pc = (prev, (start_x, start_y))

        if pc in prev_cur:
            raise Exception("HEH?")

        prev_cur.add(pc)
        path.append((start_x, start_y))

        if (
            start_x == 0
            or start_x == len(grid[0]) - 1
            or start_y == 0
            or start_y == len(grid) - 1
        ):
            running = False

    return path


count = 0

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if (x, y) == (bx, by):
            continue
        if grid[y][x] == "#":
            continue

        grid[y][x] = "#"

        try:
            get_path(bx, by)
        except Exception as e:
            # print(e)
            count += 1

        grid[by][bx] = ss
        grid[y][x] = "."

print(count)
