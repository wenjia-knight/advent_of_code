def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read()
        return content

if __name__ == "__main__":
    content = read_file('./day_08/input.txt')
    steps, _, *rest = content.splitlines()
    network = {}
    for line in rest:
        pos, targets = line.split(" = ")
        network[pos] = targets[1:-1].split(", ")

    selected = {key: value for key, value in network.items() if key[2] == "A"}
    print(selected)
    step_count = 0
    print(len(selected.keys()))
    count = 0
    for item in selected:
        if item[2] == "Z":
            count += 1
    print(count)
    # while len(selected) != count:
    #     for each in selected:
    #         current_pos = each
    #         if steps[0] == 'L':
    #             current_pos = network[current_pos][0]
    #         else:
    #             current_pos = network[current_pos][1]
    #         steps = steps[1:] + steps[0]
    #         print(current_pos)

    # for each in selected:
    #     new_selected = {}
    #     print(selected)
    #     current_pos = each
    #     print(current_pos)
    #     if steps[0] == 'L':
    #         current_pos = network[current_pos][0]
    #     else:
    #         current_pos = network[current_pos][1]
    #     steps = steps[1:] + steps[0]
    #     current_pos_list = [x for x in selected]
    #     print(current_pos_list)
    #     end_with_z = [x for x in current_pos_list if x[2]=='Z']
    #     print(len(current_pos_list))
    #     print(len(end_with_z))


    # while len(end_with_z) != len(current_pos_list):
    #     step_count += 1
    
    # print(step_count)

    # step_count = 0
    # current_pos = "AAA"
    # while current_pos != "ZZZ":
    #     step_count += 1

    #     if steps[0] == "L":
    #         current_pos = network[current_pos][0]
    #     else:
    #         current_pos = network[current_pos][1]

    #     steps = steps[1:] + steps[0]
    # print(step_count)

