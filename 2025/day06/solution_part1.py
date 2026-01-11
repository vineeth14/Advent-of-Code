import os
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_input(filename="input.txt"):
    filepath = os.path.join(BASE_DIR, filename)
    number_map = defaultdict(list)

    with open(filepath) as file:
        for line in file:
            numbers = line.strip().split()
            for i,a in enumerate(numbers):
                number_map[i].append(a)
    return number_map

print(get_input())

def solution():
    number_map = get_input()

    res = 0

    for num_list in number_map.values():
        multiply = add = False
        if num_list[-1] == "*":
            multiply = True
            total = 1
        else:
            add = True
            total = 0
        for num in num_list[:-1]:
            num = int(num)
            if add:
                total += num 
            else:
                total *= num
        res += total
    return res
print(solution())


