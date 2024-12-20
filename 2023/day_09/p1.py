def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read()
        return content
    
content = read_file('./day_09/example.txt')
lines = []
for line in content.splitlines():
    new_line = [int(x) for x in line.split()]
    lines.append(new_line)

print(lines)
total = 0
for line in lines:
    list = line
    original_list = line
    result = len(list)==len([x for x in list if x==0])
    steps = 0
    last_number = []
    while result == False:
        new_list = [list[i+1]-list[i] for i in range(0, len(list)-1)]
        print("new list: ", new_list)
        list = new_list
        last_number.append(list[-1])
        print(last_number)
        result = len(list)==len([x for x in list if x==0])
        steps+=1
    total += sum(last_number)+original_list[-1]
print(total)