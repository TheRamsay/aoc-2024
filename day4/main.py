data = []

with open("input.txt") as f:
    for line in f.readlines():
        data.append(list(line.strip()))


def check_for_word(
    word: str, grid: list[list[str]], dir: tuple[int, int], pos: tuple[int, int]
):
    dx, dy = dir
    new_x, new_y = pos

    for i in range(len(word)):
        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
            return False

        if not grid[new_y][new_x] == word[i]:
            return False

        new_x = new_x + dx
        new_y = new_y + dy

    return True


def part1():
    dirs = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]

    count = 0

    for y in range(len(data)):
        for x in range(len(data[0])):
            for dir in dirs:
                if check_for_word("XMAS", data, dir, (x, y)):
                    count += 1

    return count


def part2():
    dirs = [
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]

    count = 0
    centers = set()

    for y in range(len(data)):
        for x in range(len(data[0])):
            for dir in dirs:
                if check_for_word("MAS", data, dir, (x, y)):
                    a_pos = (x + dir[0], y + dir[1])
                    if a_pos in centers:
                        count += 1
                    else:
                        centers.add(a_pos)
    return count


print(part1())
print(part2())
