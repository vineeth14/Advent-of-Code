from process_input import get_input


def get_password():
    input = get_input()
    end = 50
    count = 0
    for rotation in input:
        end = (end + rotation) % 100
        print(end)
        if end == 0:
            count += 1
    print(count)
    return count


get_password()
