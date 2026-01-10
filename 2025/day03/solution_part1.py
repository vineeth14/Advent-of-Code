# Solution: For each number string, find the max digit (excluding last position), then find the max digit from that position onwards to form a two-digit result.
# Uses two max heaps to efficiently find these maximum values.

import os
import heapq

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_input(filename="input.txt"):
    filepath = os.path.join(BASE_DIR, filename)
    number_strings = []
    with open(filepath) as f:
        for line in f:
            number_strings.append(line.strip())
    return number_strings


def calculate_joltage(digit_string: str):
    string_length = len(digit_string)
    max_heap = []
    result = ""

    for i in range(string_length - 1):
        heapq.heappush(max_heap, (-1 * int(digit_string[i]), i))

    neg_first_max, first_max_index = heapq.heappop(max_heap)

    result += str(-neg_first_max)
    max_heap = []

    for i in range(first_max_index + 1, string_length):
        heapq.heappush(max_heap, (-1 * int(digit_string[i]), i))
    result += str(-heapq.heappop(max_heap)[0])
    print(result)
    return int(result)


def total_output_joltage():
    number_strings = get_input()
    total_joltage = 0

    for digit_string in number_strings:
        total_joltage += calculate_joltage(digit_string)
    return total_joltage


print(total_output_joltage())


# ============================================================
# O(n) SOLUTION - Optimized version
# Uses two linear scans instead of heaps to find max digits
# ============================================================


def calculate_joltage_optimized(digit_string: str):
    string_length = len(digit_string)

    # Find max digit in all positions except the last
    first_max = -1
    first_max_index = -1

    for i in range(string_length - 1):
        digit = int(digit_string[i])
        if digit > first_max:
            first_max = digit
            first_max_index = i

    # Find max digit from after first_max to end
    second_max = -1

    for i in range(first_max_index + 1, string_length):
        digit = int(digit_string[i])
        if digit > second_max:
            second_max = digit

    result = first_max * 10 + second_max
    print(result)
    return result


def total_output_joltage_optimized():
    number_strings = get_input()
    total_joltage = 0

    for digit_string in number_strings:
        total_joltage += calculate_joltage_optimized(digit_string)
    return total_joltage


# Uncomment to run optimized version:
# print(total_output_joltage_optimized())
