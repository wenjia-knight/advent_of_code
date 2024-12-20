def get_input(filename: str) -> list:
    with open(filename) as file:
        lines = file.readlines()
        moves = [line.strip() for line in lines]
    return moves


# need to separate the input into two sections. Before the empty line, it's stacks.
# After the empty line, it's moving instructions.


def steps_of_move(instruction: str) -> tuple:
    words_list = instruction.split()
    numbers = words_list[1::2]
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])
    return (a, b, c)


def move_crate(crate_stacks: list, move_instruction: tuple) -> list:
    how_many_boxes_to_move = move_instruction[0]
    from_index = move_instruction[1] - 1
    to_index = move_instruction[2] - 1
    new_stack = crate_stacks[from_index][0:(-how_many_boxes_to_move)]
    boxes_to_be_moved = crate_stacks[from_index][
        len(crate_stacks[from_index]) - how_many_boxes_to_move :
    ]
    crate_stacks[to_index].extend(boxes_to_be_moved)
    crate_stacks[from_index] = new_stack
    return crate_stacks


def move_crates(crate_stacks: list, move_instructions: list) -> list:
    for move_instruction in move_instructions:
        steps = steps_of_move(move_instruction)
        new_crates = move_crate(crate_stacks=crate_stacks, move_instruction=steps)
    return new_crates


def top_crates(crates: list) -> str:
    top_crates = []
    for crate in crates:
        top_crate = crate[-1]
        top_crates.append(top_crate)
    return "".join(top_crates)


"""
[M]                     [N] [Z]    
[F]             [R] [Z] [C] [C]    
[C]     [V]     [L] [N] [G] [V]    
[W]     [L]     [T] [H] [V] [F] [H]
[T]     [T] [W] [F] [B] [P] [J] [L]
[D] [L] [H] [J] [C] [G] [S] [R] [M]
[L] [B] [C] [P] [S] [D] [M] [Q] [P]
[B] [N] [J] [S] [Z] [W] [F] [W] [R]
"""
crate_stacks = [
    ["B", "L", "D", "T", "W", "C", "F", "M"],
    ["N", "B", "L"],
    ["J", "C", "H", "T", "L", "V"],
    ["S", "P", "J", "W"],
    ["Z", "S", "C", "F", "T", "L", "R"],
    ["W", "D", "G", "B", "H", "N", "Z"],
    ["F", "M", "S", "P", "V", "G", "C", "N"],
    ["W", "Q", "R", "J", "F", "V", "C", "Z"],
    ["R", "P", "M", "L", "H"],
]

moves = get_input("input.txt")

print(top_crates(move_crates(crate_stacks=crate_stacks, move_instructions=moves)))
