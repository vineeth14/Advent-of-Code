import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

"""
Call the number of batteries we can activate in each bank d. So d=2 for part 1 and d=12 for part 2.
We want a function j(b, d) which gives the maximum joltage from d batteries for a given input bank b(represented as a string).

We know we'll always use the left-most battery of the highest power-level in the bank 
(making sure to leave enough room for the other d-1 selections), so we find its index, call it m. 
Then we want to maximise the joltage from the batteries to the right of m, and we have d-1 batteries left to choose. 
So we make a recursive call to j(b[m+1:], d - 1). The base case occurs when d=1, where we are just picking any of the most powerful batteries.

def get_input(filename="input.txt"):
    filepath = os.path.join(BASE_DIR, filename)
    number_strings = []
    with open(filepath) as f:
        for line in f:
            number_strings.append(list(line.strip()))
    return number_strings


# we want a function that given a string:-batteries and length d 
# it needs to return the max such that d-1 remains in length of string
"""
def process_batteries(d, battery):
    if d == 1:
        return max(battery)

    partition_idx = len(battery) - (d-1)
    index = battery.index(max(battery[:partition_idx]))
    max_b = battery[index]

    return max_b + process_batteries(d-1,battery[index+1:])


def solution():
    batteries = get_input()
    total = 0
    for battery in batteries:
        total += int(process_batteries(12,battery))
    return total
print(solution())


