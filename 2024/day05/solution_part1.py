from typing import DefaultDict
from process_input import get_input


# since we need to check if each input is valid.
# First create an adjacency graph of prerequisites
# for each index you check if all previous indexes are not a prerequisite
def page_ordering_rules(prerequisites, inputs):
    adj = DefaultDict(set)
    for pre, num in prerequisites:
        adj[pre].add(num)

    flag = True
    total = 0
    for input in inputs:
        for r in range(0, len(input)):
            for i in range(0, r + 1):
                if input[i] in adj[input[r]]:
                    flag = False
        if flag:
            mid = len(input) // 2
            total += input[mid]
        if not flag:
            flag = True
    print(total)


prerequisites, input = get_input()
page_ordering_rules(prerequisites, input)
