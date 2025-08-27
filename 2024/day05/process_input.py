def get_input():
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2024/day05/INPUT.txt"
    ) as file:
        f = file.read().strip()
        sections = f.split("\n\n")
        first_sec = sections[0]
        second_sec = sections[1]
        prerequisites = []
        input = []

        for row in first_sec.split("\n"):
            left, right = row.split("|")
            prerequisites.append([int(left), int(right)])

        for row in second_sec.split("\n"):
            input.append(list(map(int, row.split(","))))

        return prerequisites, input


get_input()
