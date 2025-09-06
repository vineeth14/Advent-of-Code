from collections import defaultdict


def get_input():
    input_map = defaultdict(list)
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2024/day07/INPUT.txt"
    ) as file:
        f = file.read().strip()
        for row in f.split("\n"):
            target, values = row.split(":")
            target = int(target.strip())
            values = list(map(int, values.strip().split()))
            input_map[target].append(values)
        return input_map


get_input()
