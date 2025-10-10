# Imagine a circle with 5 positions: [0, 1, 2, 3, 4]
# If you're at position 3 and move forward 4 steps:
#
# Without wrapping: 3 + 4 = 7 (but position 7 doesn't exist!)
# With wrapping: You go 3→4→0→1→2
#
# The modulo operation (3 + 4) % 5 = 7 % 5 = 2 automatically gives you position 2!


def circular_buffer(input, steps):
    arr = [0]
    i = 0

    for j in range(1, 2018):
        i = ((i + steps) % len(arr)) + 1
        arr.insert(i, j)

    print(arr[i + 1])


circular_buffer(2017, 380)
