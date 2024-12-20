def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        input = input.read().split("\n\n")
        return input
    
def check_horizontal(grid: list) -> int:
    for i in range(1, len(grid)):
        above = grid[:i]
        below = grid[i:]
        above_len = len(above)
        below_len = len(below)
        if above_len <= below_len:
            if above[::-1] == below[:above_len]:
                return i
                break
        elif above_len > below_len:
            if above[::-1][:below_len] == below:
                return i
                break
        else:
            return 0
    
if __name__ == "__main__":
    input = read_file('./day_13/input.txt')
    total = 0
    for block in input:
        grid = block.split("\n")
        if check_horizontal(grid) != None:
            row = check_horizontal(grid)
            total += row * 100
        else:
            swap = list(zip(*grid))
            row = check_horizontal(swap)
            total += row
    print(total)


