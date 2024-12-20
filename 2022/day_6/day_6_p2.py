def get_input(file_name: str) -> str:
    with open(file_name) as file:
        input_string = file.read()
    return list(input_string)


def find_character(a_list):
    for i in range(len(a_list)):
        if len(a_list[i : i + 14]) == len(set(a_list[i : i + 14])):
            return i + 14


print(find_character(a_list=get_input("input.txt")))
