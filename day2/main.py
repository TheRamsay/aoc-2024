import numpy as np

data = []

with open("input.txt") as f:
    for line in f.readlines():
        line = line.split()
        line = [int(x) for x in line]
        data.append(line)


def is_safe(logs: np.ndarray) -> bool:
    mask1 = logs[:] > logs[1:]
    mask1 = [logs[i] < logs[i + 1] for i in range(len(logs) - 1)]
    mask2 = [logs[i] > logs[i + 1] for i in range(len(logs) - 1)]

    difs = [abs(logs[i] - logs[i + 1]) for i in range(len(logs) - 1)]
    mask3 = [diff <= 3 and diff >= 1 for diff in difs]

    if all(mask1) and all(mask3):
        return True

    if all(mask2) and all(mask3):
        return True

    return False


def part1():
    count = 0
    for logs in data:
        if is_safe(logs):
            count += 1

    print(count)


def part2():
    count = 0
    for logs in data:
        if is_safe(logs):
            count += 1
            continue

        for i in range(len(logs)):
            new_logs = [x for x in logs]
            del new_logs[i]
            if is_safe(new_logs):
                count += 1
                break

    print(count)


part1()
part2()
