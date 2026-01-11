import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_input(filename="input.txt"):
    filepath = os.path.join(BASE_DIR, filename)
    ranges = []
    ingredient_ids = []

    with open(filepath) as f:
        sections = f.read().strip().split("\n\n")
        for line in sections[0].split('\n'):
            interval =list(map(int, line.strip().split('-')))
            ranges.append(interval)
        for line in sections[1].split('\n'):
            ingredient_ids.append(int(line))
    return ranges, ingredient_ids


def merge_intervals(intervals):
    intervals.sort()

    prev = intervals[0]
    merged_intervals = [prev]
    for interval in intervals[1:]:
        if prev[1] >= interval[0]:
            prev[1] = max(prev[1],interval[1])
        else:
            merged_intervals.append(interval)
            prev = interval
    return merged_intervals



def solution():
    intervals, ingredient_ids = get_input()
    merged_intervals = merge_intervals(intervals)
    total = 0
    
    for ids in ingredient_ids:
        flag = False
        for interval in merged_intervals:
            if ids in range(interval[0], interval[1]+1):
                flag = True
        if flag:
            total += 1
    return total


print(solution())

