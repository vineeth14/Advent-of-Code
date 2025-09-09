from process_input import get_input

input_map = get_input()


def backtrack(idx, curTotal, input, target):
    if idx == len(input) - 1 and curTotal == target:
        return True
    if idx >= len(input) - 1 and curTotal != target:
        return False

    if backtrack(idx + 1, curTotal + input[idx + 1], input, target):
        return True
    if backtrack(idx + 1, curTotal * input[idx + 1], input, target):
        return True

    numb = int(str(curTotal) + str(input[idx + 1]))
    if backtrack(idx + 1, numb, input, target):
        return True

    return False


res = 0
for target, input in input_map.items():
    for row in input:
        if backtrack(0, row[0], row, target):
            res += target
