input = []


def get_input():
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2024/day02/DEMO.txt"
    ) as file:
        s = file.read().strip()

    for line in s.split("\n"):
        if line.strip():
            input.append(list(map(int, line.split())))

    return input
