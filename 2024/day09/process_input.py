def get_input():
    grid = []
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2024/day09/INPUT.txt"
    ) as file:
        f = file.read().strip()
        for row in f.split():
            grid.append(list(map(int, list(row))))

    return grid


get_input()
