from process_input import get_input

input_map = get_input()

res, sol = [], []


def backtrack(idx, curTotal, input, target):
    if idx == len(input) - 1 and curTotal == target:
        return True
    if idx >= len(input) - 1 and curTotal != target:
        return False

    if backtrack(idx + 1, curTotal + input[idx + 1], input, target):
        return True

    if backtrack(idx + 1, curTotal * input[idx + 1], input, target):
        return True
    return False


res = 0
for target, input in input_map.items():
    for row in input:
        if backtrack(0, row[0], row, target):
            res += target
print(res)
