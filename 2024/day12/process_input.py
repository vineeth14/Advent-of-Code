def get_input():
    grid = []
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2024/day12/INPUT.txt"
    ) as file:
        f = file.read().strip()
        for row in f.split("\n"):
            grid.append(list(row))
    return grid


get_input()
