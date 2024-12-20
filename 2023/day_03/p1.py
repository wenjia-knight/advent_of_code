import typing

def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read().splitlines()
        return content

def is_special_char(a_string: str) -> bool:
    if a_string in "0123456789.":
        return False
    else:
        return True

def build_grid(width: int, height: int) -> list:
    return [[False] * width for _ in range(height)]

if __name__ == "__main__":
    a_list = read_file('./day_03/example.txt')
    # print(a_list)
    grid = build_grid(height=len(a_list),width=len(a_list[0]))
    for y, item in enumerate(a_list):
        for x, char in enumerate(item):
            print(x, y, char, is_special_char(char))
            if is_special_char(char):
                grid[y][x] = True
                grid[y][x-1] = True
                grid[y][x+1] = True
                grid[y-1][x] = True
                grid[y-1][x-1] = True
                grid[y-1][x+1] = True
                grid[y+1][x] = True
                grid[y+1][x-1] = True
                grid[y+1][x+1] = True
    print(grid)  

    for y, item in enumerate(a_list):
        digits_only = "".join(['.' if is_special_char(char) else char for char in item])
        print(digits_only.split('.'))
        numbers = ["" if value == "" else int(value) for value in digits_only.split(".")]
        print(numbers)

    



# print([[False] * 2 for _ in range(4)])