import typing

def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.readlines()
        return content

def get_value(a_list: list) -> int:
    sum = 0
    for item in a_list:
        digits = [char for char in item if char.isnumeric()]
        first_digit = digits[0]
        last_digit = digits[-1]
        sum += int(first_digit + last_digit)
    return sum

if __name__ == "__main__":
    a_list = read_file('./day_01/input.txt')
    print(get_value(a_list=a_list))
