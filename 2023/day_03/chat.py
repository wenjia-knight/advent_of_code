
def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read()
        return content

def get_adjacents(x, y, width, height):
    out = []

    for dx in range(-1, 2):
        print('dx: ', dx)
        for dy in range(-1, 2):
            print('dy: ', dy)
            if dx == 0 and dy == 0:
                continue

            nx = x + dx
            print('nx: ', nx)
            ny = y + dy
            print('ny: ', ny)

            if nx >= 0 and nx < width and ny >= 0 and ny < height:
                out.append((nx, ny))
    print("out: ", out)
    return out

def main() -> None:
    data = read_file('./day_03/example.txt')

    grid = data.split("\n")
    print("grid: ", grid)

    width = len(grid[0])
    print("width: ", width)
    height = len(grid)
    print("height: ", height)

    t = 0
    for y in range(height):
        x = 0
        while x < width:
            print('x: ', x)
            if not grid[y][x].isdigit():
                print('y= ', y)
                print('x= ', x)
                print("grid[y][x]: ", grid[y][x])
                x += 1
                continue

            checks = get_adjacents(x, y, width, height)
            print("checks", checks)
            num = grid[y][x]
            print("num: ", num)

            for i in range(x + 1, width):
                if not grid[y][i].isdigit():
                    break

                num += grid[y][i]
                checks.extend(get_adjacents(i, y, width, height))
                print("checks", checks)
                x += 1

            if any(grid[ny][nx] != "." and not grid[ny][nx].isdigit() for nx, ny in checks):
                t += int(num)

            x += 1

    print(t)

if __name__ == "__main__":
    main()