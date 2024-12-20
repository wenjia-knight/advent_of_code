def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read()
        return content

def find_galaxy_coordinate(input: list) -> tuple:
    coordinates = []
    for r, row in enumerate(input):
        for c, ch in enumerate(row):
            if ch == '#':
                coordinates.append((r, c))
    return coordinates

def find_empty_rows(input: list) -> tuple:
    empty_rows = []
    for r, row in enumerate(input):
        if all(row[c] == '.' for c in range(len(row))):
            empty_rows.append(r)
    return empty_rows

def find_empty_columns(input: list) -> tuple:
    empty_columns = []
    for j in range(len(content[0])):
        if all(input[i][j] == '.' for i in range(len(content))):
            empty_columns.append(j)
    return empty_columns
    
if __name__ == "__main__":
    content = read_file('./day_11/input.txt').strip().splitlines()
    galaxies = find_galaxy_coordinate(content)
    print(galaxies)
    empty_rows = find_empty_rows(content)
    empty_cols = find_empty_columns(content)

    # sort_by_rows = sorted(galaxies)
    # sort_by_cols = sorted(galaxies, key=lambda x: x[1])
    
    total = 0
    scale = 1000000

    for i, (x1, x2) in enumerate(galaxies):
        # print(i)
        # print(x1, x2)
        for (y1, y2) in galaxies[:i]:
            for r in range(min(x1,y1), max(x1, y1)):
                if r in empty_rows:
                    total += scale
                else:
                    total += 1
            for c in range(min(x2, y2), max(x2, y2)):
                if c in empty_cols:
                    total += scale
                else:
                    total += 1
    
    print(total)