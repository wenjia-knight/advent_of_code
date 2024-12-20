# def read_file(file_path: str) -> list:
#     with open(file_path, 'r') as input:
#         content = input.read().splitlines()
#         return content

# def get_instruction_and_network(a_list: list) -> str:
#     instructions, *network = content
#     instruction = [0 if x == 'L' else 1 for x in instructions ]
#     network = network[1:]
#     return instruction, network    

# def movement(a_string: str, number: int) -> str:
#     key = a_string
#     value = dictionary[key]
#     new_key = value[number]
#     return new_key


# if __name__ == "__main__":
#     content = read_file('./day_08/input.txt')
#     instruction, network = get_instruction_and_network(content)
#     print(instruction)
#     print(network)
#     nodes = [line[0:3] for line in network]
#     pair = [line[7:15].split(", ") for line in network]
#     dictionary = dict(zip(nodes, pair))
#     print(dictionary)
#     start = "AAA"
#     total = 0
#     while start != "ZZZ":
#         for i, direction in enumerate(instruction):
#             start = movement(start, direction)
#             total += 1
#             if start == "ZZZ":
#                 break
#     print(total)


def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read()
        return content

if __name__ == "__main__":
    content = read_file('./day_08/input.txt')
    steps, _, *rest = content.splitlines()
    print(steps)
    network = {}
    for line in rest:
        pos, targets = line.split(" = ")
        network[pos] = targets[1:-1].split(", ")
    print(network)

    step_count = 0
    current_pos = "AAA"
    while current_pos != "ZZZ":
        step_count += 1

        if steps[0] == "L":
            current_pos = network[current_pos][0]
        else:
            current_pos = network[current_pos][1]

        steps = steps[1:] + steps[0]
    print(step_count)