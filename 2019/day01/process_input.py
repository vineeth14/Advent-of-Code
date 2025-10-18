def get_input():
    res = []
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2019/day01/DEMO.txt"
    ) as file:
        for line in file:
            line = line.strip()
            res.append(int(line))
    return res


get_input()
