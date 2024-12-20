def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read()
        return content
    
content = read_file('./day_09/input.txt')
lines = []
for line in content.splitlines():
    new_line = [int(x) for x in line.split()]
    lines.append(new_line)

total = 0
for line in lines:
    list = line
    original_list = line
    result = len(list)==len([x for x in list if x==0])
    steps = 0
    first_number = []
    last_number = []
    while result == False:
        new_list = [list[i+1]-list[i] for i in range(0, len(list)-1)]
        list = new_list
        first_number.append(list[0])
        last_number.append(list[-1])
        result = len(list)==len([x for x in list if x==0])
        steps+=1
    first_number = first_number[::-1]
    print(first_number)
    sum = 0
    first_number.insert(0,0)
    print(first_number)
    num = first_number[0] - first_number[1]
    for i in range(len(first_number)-2):
        num = first_number[i+2] - num
    num = original_list[0]-num
    total += num
print(total)