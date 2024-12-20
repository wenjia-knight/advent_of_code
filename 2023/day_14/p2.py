def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        input = input.read().splitlines()
        return input

def swap_rows_and_cols(input: list) -> list:
    cols = [[] for r in range(len(input))]  
    for c in range(len(input)):
        for r, row in enumerate(input):
            cols[c].append(input[r][c])
    grid = ["".join(x) for x in cols]
    return grid

def make_new_grid(grid: list) -> list:
    new_grid = []
    for row in grid:
        new_row = []
        for item in row.split("#"):
            re_order = sorted(list(item), reverse=True)
            new_row.append("".join(re_order))
        joined = "#".join(new_row)
        new_grid.append(joined)
    return new_grid

def calculate_total(grid: list) -> int:
    total = 0
    for r, row in enumerate(grid):
        print(row.count('O'))
        total += row.count('O') * (len(grid) - r)
    return total

if __name__ == "__main__":
    input = read_file('./day_14/example.txt')
    grid = swap_rows_and_cols(input)
    new_grid = swap_rows_and_cols(make_new_grid(grid))
    print(grid)
    print(new_grid)