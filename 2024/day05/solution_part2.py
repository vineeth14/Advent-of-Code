from typing import DefaultDict
from process_input import get_input


def page_ordering_rules(prerequisites, inputs):
    adj = DefaultDict(set)
    for pre, num in prerequisites:
        adj[pre].add(num)

    flag = True
    total_part1 = 0
    total_part2 = 0

    for input in inputs:
        for r in range(0, len(input)):
            for i in range(0, r + 1):
                if input[i] in adj[input[r]]:
                    flag = False

        if flag:
            mid = len(input) // 2
            total_part1 += input[mid]

        if not flag:
            reordered = reorder_list_dfs(input, adj)
            mid = len(reordered) // 2
            total_part2 += reordered[mid]
            flag = True

    print(total_part2)


""" Topological sort: repeatedly find pages with no prerequisites
    in the remaining set, place them next, then repeat.
    Works because no circular dependencies are guaranteed."""


def reorder_list_dfs(input, adj):
    visit = set()
    cycle = set()
    res = []

    def dfs(page):
        if page in visit:
            return True
        if page in cycle:
            return False

        cycle.add(page)

        # Visit all dependencies first
        for next_page in adj[page]:
            if next_page in input:
                if not dfs(next_page):
                    return False

        cycle.remove(page)
        visit.add(page)  # Mark as completely processed
        res.append(page)  # Add to result AFTER dependencies
        return True

    for page in input:
        if page not in visit:
            if not dfs(page):
                return []
    # the result is in postorder,
    return res[::-1]


# Kahn's Algorithm
def reorder_list(input, adj):
    reorder = []
    l = 0

    while input:
        for page in input:
            has_prereq = False
            for other_page in input:
                if page in adj[other_page]:
                    has_prereq = True
                    break
            if not has_prereq:
                reorder.append(page)
                input.remove(page)
                break
    return reorder


prerequisites, input = get_input()
page_ordering_rules(prerequisites, input)
