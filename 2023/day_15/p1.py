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
    print(cal_sums(input))