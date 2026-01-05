# 2 heaps. 1 from 0index to len(num)-1 and whereever that max is to the end.
# you maintain the heap as a tuple of index and value
#

import os
import heapq

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_input(filename = "input.txt"):
    filepath = os.path.join(BASE_DIR, filename)
    input = []
    with open(filepath) as f:
        for line in f:
            input.append(line.strip())
    return input

def calculate_joltage(num:str):
    len_num = len(num)
    maxHeap = []
    res = ""

    for i in range(len_num-1):
        heapq.heappush(maxHeap , (-1*int(num[i]),i))

    first_digit, idx = heapq.heappop(maxHeap)

    res += str(-first_digit)
    maxHeap = []

    for i in range(idx+1,len_num):
        heapq.heappush(maxHeap, (-1*int(num[i]),i))
    res += str(-heapq.heappop(maxHeap)[0])
    print(res)
    return int(res)

def total_output_joltage():
    input = get_input()
    total = 0

    for num in input:
        total += calculate_joltage(num)
    return total


print(total_output_joltage())
    







