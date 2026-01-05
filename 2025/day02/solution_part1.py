from process_input import get_input


def validate_num(num:int):
    if num < 10:
        return False


    num = str(num)
    mid = len(num)//2
    
    if len(num) % 2 == 0:
        first_half = num[:mid]
        second_half = num[mid:]
        return first_half == second_half


def validate_input():
    res = 0
    inputs = get_input()

    for input in inputs:
        l,r = input
        for num in range(l,r+1):
            if validate_num(num):
                res += num 
    return res
print(validate_input())
