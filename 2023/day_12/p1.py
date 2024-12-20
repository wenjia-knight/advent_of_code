def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.readlines()
        return content

if __name__ == "__main__":
    content = read_file('./day_12/example.txt')
    print(content)

    for line in content:
        pattern, numbers = line.strip("\n").split()
        numbers = tuple(map(int, numbers.split(",")))
        print(numbers)