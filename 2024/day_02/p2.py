filepath = './day_02/input.txt'

with open (filepath, 'r') as f:
    data = [list(map(int, line.split())) for line in f]

def is_safe(a_list: list) -> bool:
    if a_list[0] < a_list[1]: # ascending order
        return all(1 <= a_list[i+1]-a_list[i] <= 3 for i in range(len(a_list)-1))
    else: # descending order
        return all(1 <= a_list[i]-a_list[i+1] <= 3 for i in range(len(a_list)-1))
    
def filter_data(lists: list[list]) -> list:
    safe_lists = []
    unsafe_lists = []
    for list in lists:
        if is_safe(list):
            safe_lists.append(list)
        else:
            unsafe_lists.append(list)
    return safe_lists, unsafe_lists

def find_dampener(lists: list) -> list:
    safe_lists, unsafe_lists = filter_data(lists = lists)
    for each in unsafe_lists:
        for i in range(len(each)):
            modified = each[:i] + each[i+1:]
            if is_safe(modified):
                safe_lists.append(modified)
                break
            else:
                continue
    return safe_lists
    
def count_total(a_list: list) -> int:
    return sum([is_safe(each) for each in a_list])

safe_lists = find_dampener(lists = data)
print(filter_data(lists = data))
print(len(safe_lists))

