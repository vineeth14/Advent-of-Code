from process_input import get_input

def validate_num(number: int):
    if number < 10:
        return False


    number_str = str(number)
    half_length = len(number_str) // 2

    for chunk_size in range(1, half_length + 1):
        if len(number_str) % chunk_size == 0:
            unique_chunks = set()
            start, end = 0, chunk_size
            while end <= len(number_str):
                unique_chunks.add(number_str[start:end])
                start = end
                end += chunk_size
        if len(unique_chunks) == 1:
            return True

    return False

def validate_input():
    total_sum = 0
    input_ranges = get_input()

    for range_pair in input_ranges:
        start, end = range_pair
        for candidate in range(start, end + 1):
            if validate_num(candidate):
                total_sum += candidate
    return total_sum
print(validate_input())
