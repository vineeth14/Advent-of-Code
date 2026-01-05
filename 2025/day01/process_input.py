def get_input():
    res = []
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2025/day01/demo.txt"
    ) as file:
        lines = file.read().splitlines()
        for line in lines:
            if line[0] == "L":
                res.append((-1) * int(line[1:]))
            else:
                res.append(int(line[1:]))
    return res


get_input()
