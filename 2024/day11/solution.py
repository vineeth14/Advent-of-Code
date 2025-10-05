from process_input import get_input
import math
from collections import Counter, defaultdict


def process_stone(stones):
    result = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            result[1] += count
        else:
            digits = int(math.log10(stone)) + 1
            if digits % 2 == 0:
                mid = digits // 2
                left = stone // 10**mid
                right = stone % 10**mid
                result[left] += count
                result[right] += count
            else:
                new_stone = stone * 2024
                result[new_stone] += count

    return result


stones = get_input()
stones = Counter(stones)

for i in range(75):
    stones = process_stone(stones)

print(sum(stones.values()))
