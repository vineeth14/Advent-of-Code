def get_input():
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2024/day04/INPUT.txt"
    ) as file:
        s = file.read().strip()
        grid = [list(row) for row in s.split()]
    return grid


get_input()
