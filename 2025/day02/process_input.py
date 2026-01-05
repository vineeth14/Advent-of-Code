def get_input():
    input = []
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2025/day02/input.txt"
    ) as file:
        line = file.read().strip()
        line = line.split(",")
        for product_id in line:
            product_id = product_id.split("-")
            product_id = list(map(int, product_id))
            input.append(product_id)

    return input


get_input()
