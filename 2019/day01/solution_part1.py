from process_input import get_input

input = get_input()


def solution_part1(input):
    total = 0
    for num in input:
        num = num // 3
        total += num - 2

    print(total)
    return total


solution_part1(input)
