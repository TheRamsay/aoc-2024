from collections import defaultdict


def sort_arr_by_rules(arr, rules):
    temp = []
    rule_violation = False
    for el in arr:
        must_be_before = rules[el]
        temp.append(el)
        for heh in must_be_before:
            try:
                pos = temp.index(heh)
                rule_violation = True
                del temp[pos]
                temp.append(heh)
            except Exception as e:
                continue

    return temp, rule_violation


rules = defaultdict(list)
updates = []

with open("input.txt") as f:
    x, y = f.read().split("\n\n")
    for line in x.strip().split("\n"):
        a, b = [x for x in line.split("|")]
        rules[a].append(b)

    updates = [l.split(",") for l in y.strip().split("\n")]


def part2():
    middles = []
    for u in updates:
        violated_first_time = False
        sorted_arr, violated = sort_arr_by_rules(u, rules)
        violated_first_time = violated

        while violated:
            sorted_arr, violated = sort_arr_by_rules(sorted_arr, rules)

        if violated_first_time:
            middles.append(sorted_arr[len(sorted_arr) // 2])

    return middles


def part1():
    middles = []
    for u in updates:
        violated_first_time = False
        sorted_arr, violated = sort_arr_by_rules(u, rules)
        violated_first_time = violated

        while violated:
            sorted_arr, violated = sort_arr_by_rules(sorted_arr, rules)

        if not violated_first_time:
            middles.append(u[len(u) // 2])

    return middles


def get_sum(arr):
    return sum(int(x) for x in arr)


print(get_sum(part1()))
print(get_sum(part2()))
