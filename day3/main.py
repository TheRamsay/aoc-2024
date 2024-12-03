import re

mul_r = r"mul\((\d{1,3}),(\d{1,3})\)"
do_r = r"do\(\)"
dont_r = r"don't\(\)"

data = []

with open("input.txt", "r") as f:
    text = f.read()


def part1():
    mul_matches = re.finditer(mul_r, text)
    count = 0
    for a in mul_matches:
        a, b = [int(x) for x in a.group().replace(")", "")[4:].split(",")]
        count += a * b

    return count


def part2():
    mul_matches = re.finditer(mul_r, text)
    do_idx = [mlem.start() for mlem in re.finditer(do_r, text)]
    dont_idx = [mlem.start() for mlem in re.finditer(dont_r, text)]

    count = 0
    for a in mul_matches:
        l, r = a.start(), a.end()
        a, b = [int(x) for x in a.group().replace(")", "")[4:].split(",")]

        most_recent_do = [idx for idx in do_idx if idx < l]
        most_recent_dont = [idx for idx in dont_idx if idx < l]

        if not any(most_recent_do) and not any(most_recent_dont):
            count += a * b
            continue

        if not any(most_recent_do) and any(most_recent_dont):
            continue

        if any(most_recent_do) and any(most_recent_dont):
            if most_recent_do[-1] > most_recent_dont[-1]:
                count += a * b
            else:
                continue

    return count


print(part1())
print(part2())
