def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read()
        return content

def find_s(content: list) -> tuple:
    for i, row in enumerate(content):
        for j, ch in enumerate(row):
            if ch == 'S':
                starting_row = i
                starting_column = j
                break
        else:
            continue
        break
    return (starting_row, starting_column)

def build_grid(width: int, height: int) -> list:
    return ['0'*width for x in range(height)]

if __name__ == "__main__":
    content = read_file('./day_10/example.txt').strip().splitlines()
    starting_row, starting_column = find_s(content)
    print(starting_row)
    print(starting_column)

