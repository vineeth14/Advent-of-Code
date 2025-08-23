import collections


def get_input():
    list1 = []
    list2 = []
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2024/day01/INPUT.txt", "r"
    ) as file:
        for line in file:
            line = line.split()
            list1.append(line[0])
            list2.append(line[1])
    return list1, list2


def total_distance():
    list1, list2 = get_input()
    list1.sort()
    list2.sort()
    res = 0

    for id1, id2 in zip(list1, list2):
        res += abs(int(id1) - int(id2))
    return res


def similarity_calc():
    list1, list2 = get_input()
    count_list2 = collections.Counter(list2)
    res = 0

    for num in list1:
        similarity = count_list2[num]
        print(similarity, num)
        res += int(num) * similarity
    print(res)
    return res


total_distance()
similarity_calc()
