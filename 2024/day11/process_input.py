def get_input():
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2024/day11/INPUT.txt"
    ) as file:
        res = []
        f = file.read()
        for num in f.split(" "):
            res.append(int(num))

    return res


get_input()
