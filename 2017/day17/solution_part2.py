steps = 380


def get_solution(input_path):
    i, result, arr_len = 0, 0, 1

    for j in range(1, 50000000):
        i = ((i + steps) % arr_len) + 1

        if i == 1:
            result = j

        arr_len += 1

    return result
