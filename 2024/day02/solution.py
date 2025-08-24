from process_input import get_input


def is_safe(line):
    increasing = all(a > b for a, b in zip(line, line[1:]))
    decreasing = all(a < b for a, b in zip(line, line[1:]))

    if not (increasing or decreasing):
        return False

    for a, b in zip(line, line[1:]):
        if abs(b - a) > 3 or abs(b - a) < 1:
            return False

    return True


def safe_report(input):
    res = 0
    for line in input:
        if is_safe(line):
            res += 1
            continue

        safe_removal = False

        for i in range(len(line)):
            dampened_line = line[:i] + line[i + 1 :]
            if is_safe(dampened_line):
                safe_removal = True
                break
        if safe_removal:
            res += 1
    print(res)
    return res


input = get_input()
safe_report(input)
