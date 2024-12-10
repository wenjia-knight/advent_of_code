filepath = './day_02/input.txt'

with open (filepath, 'r') as f:
    data = [list(map(int, line.split())) for line in f]

def is_safe(a_list: list) -> bool:
    if a_list[0] < a_list[1]: # ascending order
        return all(1 <= a_list[i+1]-a_list[i] <= 3 for i in range(len(a_list)-1))
    else: # descending order
        return all(1 <= a_list[i]-a_list[i+1] <= 3 for i in range(len(a_list)-1))

def count_total(a_list: list) -> int:
    return sum([is_safe(each) for each in a_list])

print(count_total(a_list = data))
