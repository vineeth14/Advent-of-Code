def get_input():
    grid = []
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2024/day08/DEMO.txt"
    ) as file:
        f = file.read().strip()
        for row in f.split():
            grid.append(list(row))

    return grid


get_input()
