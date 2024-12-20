import math

def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read().splitlines()
        return content

def get_combos(a_num: int, b_num: int) -> int:
    if a_num % 2 == 0:
        mid_point = int(a_num/2)
        score = 1
    else:
        mid_point = int((a_num+1)/2)
        score = 0
    num = 0
    for i in range(mid_point, 0, -1):
        result = i*(a_num-i)
        if result > b_num:
            num += 1
        else:
            break
    return 2*(num-1)+1*score

if __name__ == "__main__":
    a_list = read_file('./day_06/input.txt')
    # print(a_list)
    a_time = int(''.join(a_list[0].split(":")[1].strip().split()))
    # print(a_time)
    a_distance = int(''.join(a_list[1].split(":")[1].strip().split()))
    # print(a_distance)
    print(get_combos(a_time, a_distance))
