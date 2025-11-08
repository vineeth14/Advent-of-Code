def get_input():
    res = []
    with open("INPUT.txt") as f:
        for line in f:
            first, second = line.split(" ")
            first = list(map(int, first.split("=")[1].split(",")))
            second = list(map(int, second.split("=")[1].split(",")))
            res.append((first, second))
    return res
