def read_file(file_path: str) -> list:
    with open(file_path, 'r') as file:
        input = file.read().strip().split(",")
        return input

def hash_algorithm(a_string: str) -> int:
    current_value = 0
    remainder = 0
    for i, ch in enumerate(a_string):
        current_value = remainder + ord(ch)
        remainder = current_value*17%256
    return remainder

def cal_sums(a_list: list) -> int:
    total = 0
    for item in a_list:
        total += hash_algorithm(item)
    return total

if __name__ == "__main__":
    input = read_file('./day_15/input.txt')
    boxes = [[] for i in range(256)]
    focal_length = {}
    for each in input:
        if '-' in each:
            label = each[:-1]
            index = hash_algorithm(label)
            if label in boxes[index]:
                boxes[index].remove(label)
        else:
            label, length = each.split("=")
            length = int(length)
            index = hash_algorithm(label)
            if label not in boxes[index]:
                boxes[index].append(label)

            focal_length[label] = length
        total = []
        for i, item in enumerate(boxes):
            if len(item) != 0:
                focusing_power = 0
                for j, each in enumerate(item):
                    focusing_power += (i+1) * (j+1) * focal_length[each]
                total.append(focusing_power)
            else:
                focusing_power = 0
                total.append(focusing_power)
    print(total)
    print(sum(total))







