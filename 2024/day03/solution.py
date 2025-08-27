from process_input import get_input
import re


def toboggan_rental(line):
    matches = re.findall(r"mul\((\d+),(\d+)\)", line)
    res = 0

    for a, b in matches:
        res += int(a) * int(b)
    print(res)
    return res


input = get_input()
toboggan_rental(input)

