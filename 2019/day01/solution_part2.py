from process_input import get_input

input = get_input()


def process(num):
    total = 0
    while num >= 0:
        num = (num // 3) - 2
        if num > 0:
            total += num
    return total


def solution_part2(input):
    total = 0
    for n in input:
        total += process(n)
    print(total)

    return total


solution_part2(input)
